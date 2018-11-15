#For user interface and web scraping
from flask import Flask, render_template, request, redirect, url_for, flash
from bs4 import BeautifulSoup
import urllib
from beautifultable import BeautifulTable
import os
import csv

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

#for map-reduce tasks
from mrjob.job import MRJob

stop_words = set(stopwords.words('english')) #Getting the list of stop words
existing_terms = set() #To not include the terms reoccurring in the same document
term_dict = {} #used as the inverted index for all the terms
document_list = set() # Contains the names of all documents

## Function to read from file and parse data from it as -> (title, author, content)
def parse_document(doc_title):
	f = open(doc_title,'r')
	lines = f.readlines()
	title = str(lines[0])
	author = str(lines[1])
	author = author[1:-2]

	content = ""
	for line in lines[2:]:
		content += line

	return (title, author, content)



#Query parser
def get_query_results(query):
	
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

	#### EXPERIMENTAL

	#List of documents relevant to term1 and term2 respectively
	doc_term1 = []
	doc_term2 = []
	
	if term1 in term_dict:
		if flag1 == True:
			doc_term1 = term_dict[term1]
		else:
			doc_term1 = [doc for doc in document_list if doc not in term_dict[term1]]

	if term2 in term_dict:
		if flag2 == True:
			doc_term2 = term_dict[term2]
		else:
			doc_term2 = [doc for doc in document_list if doc not in term_dict[term2]]

	
	relevant_docs = []
	
	#Applying the boolean operator to retreive the relevant documents
	if operator == 'and':
		relevant_docs = set(doc_term1).intersection(doc_term2)

	elif operator == 'or':
		relevant_docs = set(doc_term1 + doc_term2)

	if len(relevant_docs) == 0:
		print("No matching documents found!")
		return False, query
	else:
		print("The relevant documents are: ")
		for doc in relevant_docs:
			print(doc)
	print()


	#Returning the list of relevant docs
	return relevant_docs, query

@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		query = request.form['query']

		#matrix, terms = create_term_matrix()
		#MRInvertedIndexer.run() #builds the inverted index and gets the terms

		## Getting the list of documents
		cur = mysql.connection.cursor()
		res = cur.execute("select doc_name from documents")
		if res > 0:
			data = cur.fetchall()
			for row in data:
				document_list.add(row['doc_name'])

		#Retreiving the inverted index
		res = cur.execute("select * from inverted_index")
		if res > 0:
			data = cur.fetchall()
			for row in data:
				if row['term'] in term_dict:
					term_dict[row['term']].append(row['doc'])
				else:
					term_dict[row['term']] = [row['doc']]

		cur.close()
		#print(term_dict)
		#Applying the boolean query parser over the inverted index
		docs, query = get_query_results(query=query)

		relevant_docs = {}
		for doc in docs:
			title, author, content = parse_document("docs/" + doc + ".txt")
			relevant_docs[title] = [author, content[:200]]
		
		if relevant_docs == False:
			return render_template('home.html', msg = "No relevant documents found", query = query)

		return render_template('home.html', relevant_docs = relevant_docs, query = query)

	#For GET request
	return render_template('home.html')


@app.route('/document/<string:doc_title>')
def document(doc_title):
	title, author, content = parse_document("docs/" + doc_title + ".txt")
	return render_template('document.html', title = title, author = author, content = content)


#To pring helpful messages
def logger(msg):
	print("**********************")
	print("\n\n\n")
	print(msg)
	print("\n\n\n")
	print("**********************")


if __name__ == '__main__':
	app.run(debug=True)


# @app.route('/index', methods = ['GET', 'POST'])
# def index():
# 	if request.method == 'POST':
		
# 		#Indexing the entered document
# 		link = request.form['url']

# 		####### NEW SCRAPE METHOD #########
# 		# url = link
# 		# source_code = requests.get(url)
# 		# plain_text = source_code.content
# 		# soup = BeautifulSoup(plain_text, "lxml")
# 		# links = soup.findAll('a', {'class': 'a-link-normal s-access-detail-page a-text-normal'})
# 		# print len(links)
# 		# for link in links:
# 		#     title = link.get('title')
# 		#     print title
# 		###################################
		
# 		try:
# 			req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
# 			f = urllib.request.urlopen(req).read()
# 		except Exception:
# 			cur = mysql.connection.cursor()
# 			res = cur.execute("select title, link from data")
# 			data_dict = {}
# 			if res > 0:
# 				data = cur.fetchall()
# 				for row in data:
# 					data_dict[row['title']] = row['link']
# 			cur.close()
# 			return render_template('index.html', data_dict=data_dict, msg = "Invalid URL entered", url = link)
		
# 		soup = BeautifulSoup(f)
# 		body = ""

		

# 		#Getting the document body from the p tags
# 		for page in soup.find_all('p'):
# 			body += page.get_text() + " "

# 		logger(body)

# 		#Getting the document title from the meta-title tags
# 		title = soup.find("meta",  property="og:title")
# 		title = title["content"]
		
# 		logger(title)

# 		#Storing indexed document into database for faster retrieval
# 		cur = mysql.connection.cursor()
# 		cur.execute("insert into data (title, link, content) values (%s, %s, %s)", (title, link, body))
# 		mysql.connection.commit()

# 		#getting the updated indexed data
# 		res = cur.execute("select title, link from data")
# 		data_dict = {}
# 		if res > 0:
# 			data = cur.fetchall()
# 			for row in data:
# 				data_dict[row['title']] = row['link']
# 		cur.close()
# 		logger(data_dict)
# 		return render_template('index.html', data_dict=data_dict)
	
# 	#getting the indexed data
# 	cur = mysql.connection.cursor()
# 	res = cur.execute("select title, link from data")
# 	data_dict = {}
# 	if res > 0:
# 		data = cur.fetchall()
# 		for row in data:
# 			data_dict[row['title']] = row['link']
# 	cur.close()
# 	logger(data_dict)
# 	return render_template('index.html', data_dict=data_dict)





# def create_term_matrix():
# 	table = BeautifulTable()
# 	cur = mysql.connection.cursor()
# 	result = cur.execute("select content from data")
# 	if result > 0:
# 		documents = []

# 		#Getting the content from stored documents
# 		data = cur.fetchall()
# 		for row in data:
# 			documents.append(row['content'].lower())

# 		#Tokenizing the document
# 		tokens = []
# 		for doc in documents:
# 			tokens.extend(word_tokenize(doc))

# 		print(tokens) #contains stop words
		
# 		#Getting the list of stop words
# 		stop_words = set(stopwords.words('english'))

# 		#eliminating stop words from the documents
# 		terms = [word for word in tokens if not word in stop_words]
# 		terms = list(set(terms))
		
# 		print(terms) #doesnt contain stop words

# 		#Conforming term document incidence matrix header to BeautifulTable format
# 		doc_headers = ["Terms"]
# 		for i in range(len(documents)):
# 			s = "DocID:" + str(i+1)
# 			doc_headers.append(s)

# 		table.column_headers = doc_headers

# 		#Generating the term-document incidence matrix
# 		matrix = [[0 for x in range(len(documents))] for y in range(len(terms))]
# 		for i,term in enumerate(terms):
# 			for j,doc in enumerate(documents):
# 				matrix[i][j] = 1 if term in doc else 0
# 			l = []
# 			l.append(term)
# 			l.extend(list(matrix[i]))
			
# 			table.append_row(l)

# 		#Displaying the matrix
# 		print(table)

# 		#Returning the TDI matrix and the list of terms generated through indexed documents
# 		return matrix, terms

# 	else:
# 		logger("No data found, cannot create matrix!")

