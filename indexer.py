#MySQL database
from flask_mysqldb import MySQL

from flask import Flask

#creating the app engine
app = Flask(__name__)

#configuring sql settings
from sql_config import configure
configure(app)
mysql = MySQL(app)

#for map-reduce tasks
from mrjob.job import MRJob

import os
import csv

#For linguistic preprocessing
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english')) #Getting the list of stop words
existing_terms = set() #To not include the terms reoccurring in the same document
document_list = set() # Contains the names of all documents

term_dict = {} #used as the inverted index for all the terms

class MRInvertedIndexer(MRJob):
	
	#Need to get (term, docID) yield
	def mapper(self, _, line):
		doc_name = os.environ['map_input_file']
		doc_name = doc_name[5:-4] # to skip 'docs/' and '.txt' from search results
		document_list.add(doc_name)

		#Getting the content from stored documents
		tokens = word_tokenize(line)

		print(tokens) #contains stop words
		
		#eliminating stop words from the documents
		terms = [word for word in tokens if not word in stop_words]
		terms = list(set(terms))
		
		print(terms) #doesnt contain stop words

		for term in terms:
			if (term, doc_name) not in existing_terms:
				yield(term, doc_name)
				existing_terms.add((term, doc_name))

	
	#need to reduce the (term -> [doc list]) yield
	def reducer(self, term, docs):
		lister = []
		lister.extend(docs)
		yield(term, lister)

		#(term -> [doc_list]) dictionary
		term_dict[term] = lister


def index_docs():
	cur = mysql.connection.cursor()
	#document_list = set()
	#term_dict = {}

	document_list.add("work")
	term_dict["hello"] = ['hello', 'bob']	

	for key, value in term_dict.items():
		for v in value:
			cur.execute("insert into inverted_index (term, doc) values (%s, %s)", (key, str(v)))
			mysql.connection.commit()

	for doc in document_list:
		cur.execute("insert into documents (doc_name) values (%s)", [str(doc)])
		mysql.connection.commit()
	
	print("###### DONE ######")
	cur.close()

@app.route("/")
def home():
	MRInvertedIndexer.run() #builds the inverted index and gets the terms
	index_docs()
	return '<h1 align = "center">Data successfully indexed into cache database</h1>'

if __name__ == '__main__':
	app.run(debug=True)
	
	

	

	
