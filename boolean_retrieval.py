#For user interface and web scraping
from flask import Flask, render_template, request, redirect, url_for
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

		data = cur.fetchall()
		for row in data:
			documents.append(row['content'].lower())

		#Tokenizing the document
		tokens = []
		for doc in documents:
			tokens.extend(word_tokenize(doc))

		#Getting the list of stop words
		stop_words = set(stopwords.words('english'))

		#eliminating stop words from the documents
		terms = [word for word in tokens if not word in stop_words]

		print(tokens) #contains stop words

		terms = list(set(terms))
		print(terms) #doesnt contain stop words

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

		return matrix, terms

	else:
		logger("No data found, cannot create matrix!")

	

def get_query_results(query, terms, matrix):
	'''
		SUPPORTS 
			A AND B
			A OR B
	'''
	qterms = query.lower().split(" ")
	
	if len(qterms) == 1:
		term1 = qterms[0]
		term2 = qterms[0]
		operator = 'and'
	
	else:
		term1 = qterms[0]
		term2 = qterms[2]
		operator = qterms[1]

	
	docs_term1 = []
	docs_term2 = []
	relevant_docs = []

	#getting the postings index for both the query terms
	index1 = terms.index(term1)
	index2 = terms.index(term2)

	#Getting the relevant documents for individual query terms
	for j in range(len(matrix[index1])):
		if matrix[index1][j] == 1:
			docs_term1.append(j)

	for j in range(len(matrix[index2])):
		if matrix[index2][j] == 1:
			docs_term2.append(j)

	#getting the desired doc ids
	if operator == 'and':
		#The filter takes each sublist's item and checks to see if it's in the source list doc_terms1, the list comprehension is executed for each sublist in docs_terms2
		relevant_docs = set(docs_term1).intersection(docs_term2)

	elif operator == 'or':
		relevant_docs = set(docs_term1 + docs_term2)

	if len(relevant_docs) == 0:
		print("No matching documents found!")
	else:
		print("The relevant documents are: ", end = " ")
		for i in relevant_docs:
			print("Document:" + str(i+1), end = " ")
	print()

	return relevant_docs

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		query = request.form['query']

		matrix, terms = create_term_matrix()
		relevant_docs = get_query_results(query=query, terms=terms, matrix=matrix)
		data_dict = {}
		cur = mysql.connection.cursor()
		for doc in relevant_docs:
			cur.execute("select title, link from data where id = %s",[doc+1])
			data = cur.fetchone()
			data_dict[data['title']] = data['link']

		cur.close()

		return render_template('home.html', data_dict = data_dict)


	return render_template('home.html')

@app.route('/index', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		#Indexing the entered document
		link = request.form['url']
		req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
		f = urllib.request.urlopen(req).read()
		soup = BeautifulSoup(f)
		body = ""
		for page in soup.find_all('p'):
			body += page.get_text() + " "

		logger(body)

		title = soup.find("meta",  property="og:title")
		title = title["content"]
		
		logger(title)

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


def logger(msg):
	print("**********************")
	print("\n\n\n")
	print(msg)
	print("\n\n\n")
	print("**********************")


if __name__ == '__main__':
	app.run(debug=True)



'''
FOR MULTIPLE OPERATORS

def evaluate_query_infix(qterms):
	term_stack = [], op_stack = [], ctr = 0
	oplist = ['and', 'or'] #not?
	while(qterms):
		term = qterms[ctr]
		ctr += 1
		if (term not in oplist):
			#We have a query term or a left paranthesis
			term_stack.append(term)
		elif term == '(':
			op_stack.append(term)

'''