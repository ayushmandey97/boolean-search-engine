#For user interface and web scraping
from flask import Flask, render_template, request, redirect, url_for, flash
from bs4 import BeautifulSoup
import urllib
from beautifultable import BeautifulTable

#MySQL database
from flask_mysqldb import MySQL

#For linguistic preprocessing
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#creating the app engine
app = Flask(__name__)

#configuring sql settings
from sql_config import configure
configure(app)
mysql = MySQL(app)


def create_term_matrix():
	table = BeautifulTable()
	cur = mysql.connection.cursor()
	result = cur.execute("select content from data")
	if result > 0:
		documents = []

		#Getting the content from stored documents
		data = cur.fetchall()
		for row in data:
			documents.append(row['content'].lower())

		#Tokenizing the document
		tokens = []
		for doc in documents:
			tokens.extend(word_tokenize(doc))

		print(tokens) #contains stop words
		
		#Getting the list of stop words
		stop_words = set(stopwords.words('english'))

		#eliminating stop words from the documents
		terms = [word for word in tokens if not word in stop_words]
		terms = list(set(terms))
		
		print(terms) #doesnt contain stop words

		#Conforming term document incidence matrix header to BeautifulTable format
		doc_headers = ["Terms"]
		for i in range(len(documents)):
			s = "DocID:" + str(i+1)
			doc_headers.append(s)

		table.column_headers = doc_headers

		#Generating the term-document incidence matrix
		matrix = [[0 for x in range(len(documents))] for y in range(len(terms))]
		for i,term in enumerate(terms):
			for j,doc in enumerate(documents):
				matrix[i][j] = 1 if term in doc else 0
			l = []
			l.append(term)
			l.extend(list(matrix[i]))
			
			table.append_row(l)

		#Displaying the matrix
		print(table)

		#Returning the TDI matrix and the list of terms generated through indexed documents
		return matrix, terms

	else:
		logger("No data found, cannot create matrix!")

def get_query_results(query, terms, matrix):
	
	'''
		SUPPORTS
			A (single term query)
			A AND B
			A OR B

			where A/B can be replaced by NOT A / NOT B
	'''
	qterms = query.lower().split(" ")

	#Flag = False indicates that the term is in NOT form
	flag1 = True
	flag2 = True
	
	#If it's a query containing NOT
	if 'not' in qterms:
		if qterms.count('not') == 2:
			flag1 = False
			flag2 = False
			qterms.remove('not')
			qterms.remove('not')

		else:
			if qterms[0] == 'not':
				flag1 = False
			else:
				flag2 = False

			#removing the not terms after marking the flags
			qterms.remove('not')

	#If it's a single term query
	if len(qterms) == 1:
		#not case for single term query
		if flag1 == False or flag2 == False:
			flag1 = False
			flag2 = False
		
		#using a bi-gram query system by making the two terms from the same one
		term1 = qterms[0]
		term2 = qterms[0]
		operator = 'and'

	#Two term query
	else:
		term1 = qterms[0]
		term2 = qterms[2]
		operator = qterms[1]

	logger(str(flag1) + str(flag2))
	
	#getting the index for both the query terms in matrix
	if term1 in terms:
		index1 = terms.index(term1)
	else:
		index1 = -1

	if term2 in terms:
		index2 = terms.index(term2)
	else:
		index2 = -1

	#Postings lists
	docs_term1 = []
	docs_term2 = []

	#Getting the relevant documents for individual query terms (postings)
	if index1 >= 0:
		for j in range(len(matrix[index1])):
			if flag1 == False:
				if matrix[index1][j] == 0:
					docs_term1.append(j)
			else:
				if matrix[index1][j] == 1:
					docs_term1.append(j)

	#Handling case for when the term entered doesnt exist in the term list
	else:
		if flag1 == False:
			for i in range(len(matrix[0])):
				docs_term1.append(i)
	
	if index2 >= 0:
		for j in range(len(matrix[index2])):
			if flag2 == False:
				if matrix[index2][j] == 0:
					docs_term2.append(j)
			else:
				if matrix[index2][j] == 1:
					docs_term2.append(j)
	else:
		if flag2 == False:
			for i in range(len(matrix[0])):
				docs_term2.append(i)

	logger(docs_term1)
	logger(docs_term2)
	
	relevant_docs = []

	#getting the desired doc ids
	if operator == 'and':
		relevant_docs = set(docs_term1).intersection(docs_term2)

	elif operator == 'or':
		relevant_docs = set(docs_term1 + docs_term2)

	if len(relevant_docs) == 0:
		print("No matching documents found!")
		return False, query
	else:
		print("The relevant documents are: ", end = " ")
		for i in relevant_docs:
			print("Document:" + str(i+1), end = " ")
	print()

	#Returning the list of relevant docs
	return relevant_docs, query

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		query = request.form['query']

		matrix, terms = create_term_matrix()
		relevant_docs, query = get_query_results(query=query, terms=terms, matrix=matrix)
		
		if relevant_docs == False:
			return render_template('home.html', msg = "No relevant documents found", query = query)
		
		data_dict = {}
		cur = mysql.connection.cursor()

		#Getting the list of relevant documents to be displayed as search results
		for doc in relevant_docs:
			cur.execute("select title, link from data where id = %s",[doc+1])
			data = cur.fetchone()
			data_dict[data['title']] = data['link']

		cur.close()

		return render_template('home.html', data_dict = data_dict, query = query)

	return render_template('home.html')

@app.route('/index', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		
		#Indexing the entered document
		link = request.form['url']

		####### NEW SCRAPE METHOD #########
		# url = link
		# source_code = requests.get(url)
		# plain_text = source_code.content
		# soup = BeautifulSoup(plain_text, "lxml")
		# links = soup.findAll('a', {'class': 'a-link-normal s-access-detail-page a-text-normal'})
		# print len(links)
		# for link in links:
		#     title = link.get('title')
		#     print title
		###################################
		
		try:
			req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
			f = urllib.request.urlopen(req).read()
		except Exception:
			cur = mysql.connection.cursor()
			res = cur.execute("select title, link from data")
			data_dict = {}
			if res > 0:
				data = cur.fetchall()
				for row in data:
					data_dict[row['title']] = row['link']
			cur.close()
			return render_template('index.html', data_dict=data_dict, msg = "Invalid URL entered", url = link)
		
		soup = BeautifulSoup(f)
		body = ""

		

		#Getting the document body from the p tags
		for page in soup.find_all('p'):
			body += page.get_text() + " "

		logger(body)

		#Getting the document title from the meta-title tags
		title = soup.find("meta",  property="og:title")
		title = title["content"]
		
		logger(title)

		#Storing indexed document into database for faster retrieval
		cur = mysql.connection.cursor()
		cur.execute("insert into data (title, link, content) values (%s, %s, %s)", (title, link, body))
		mysql.connection.commit()

		#getting the updated indexed data
		res = cur.execute("select title, link from data")
		data_dict = {}
		if res > 0:
			data = cur.fetchall()
			for row in data:
				data_dict[row['title']] = row['link']
		cur.close()
		logger(data_dict)
		return render_template('index.html', data_dict=data_dict)
	
	#getting the indexed data
	cur = mysql.connection.cursor()
	res = cur.execute("select title, link from data")
	data_dict = {}
	if res > 0:
		data = cur.fetchall()
		for row in data:
			data_dict[row['title']] = row['link']
	cur.close()
	logger(data_dict)
	return render_template('index.html', data_dict=data_dict)

#To pring helpful messages
def logger(msg):
	print("**********************")
	print("\n\n\n")
	print(msg)
	print("\n\n\n")
	print("**********************")


if __name__ == '__main__':
	app.run(debug=True)
