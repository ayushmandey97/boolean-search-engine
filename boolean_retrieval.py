#For user interface and web scraping
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import urllib

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
	documents = []

	doc1 = "The students like the subject information retrival a lot because they want to understand how stuff like google works"
	doc2 = "The students dont like to study operating systems because that shit is wack"

	documents.append(doc1.lower())
	documents.append(doc2.lower())

	#Tokenizing the document
	tokens = []
	for doc in documents:
		tokens.extend(word_tokenize(doc))

	#Getting the list of stop words
	stop_words = set(stopwords.words('english'))

	#eliminating stop words from the documents
	terms = [word for word in tokens if not word in stop_words]

	print(tokens) #contains stop words
	print(terms) #doesnt contain stop words

	#Generating the term-document incidence matrix
	matrix = [[0 for x in range(len(documents))] for y in range(len(terms))]
	for i,term in enumerate(terms):
		for j,doc in enumerate(documents):
			matrix[i][j] = 1 if term in doc else 0

	#Displaying the matrix
	for i in range(len(terms)):
		for j in range(len(documents)):
			print(matrix[i][j], end = " ")
		print("")

	return matrix, terms

def get_query_results(query, terms, matrix):
	qterms = query.lower().split(" ")

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
	#if request.method == 'POST':
		# print("HELOOOOOOOOO")
		# link = request['url']
		# f = urllib.urlopen(link)
		# soup = BeautifulSoup(f)

		# for tag in soup.find_all('p'):
		# 	print(tag)
	

	query = input("Enter query")
	matrix, terms = create_term_matrix()
	relevant_docs = get_query_results(query=query, terms=terms, matrix=matrix)


	return render_template('index.html', docs = relevant_docs)



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