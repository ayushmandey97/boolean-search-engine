#For map reduce
import os
from mrjob.job import MRJob

#For linguistic preprocessing
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Getting the list of stop words
stop_words = set(stopwords.words('english'))
existing_terms = set()
term_dict = {} #used as the inverted index for all the terms
document_list = set()

class MRWordCount(MRJob):
	
	#Need to get (term, docID) yield
	def mapper(self, _, line):
		doc_name = os.environ['map_input_file']
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
		#return False, query
	else:
		print("The relevant documents are: ")
		for doc in relevant_docs:
			print(doc)
	print()


	#Returning the list of relevant docs
	#return relevant_docs, query

if __name__ == '__main__':
	print("###### Building the inverted index ######")
	MRWordCount.run()
	print(term_dict)
	print("###### Inverted index successfully built ######")

	query = input("Enter the query: ")
	get_query_results(query)
