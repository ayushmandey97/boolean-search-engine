#For map reduce
import os
from mrjob.job import MRJob

#For linguistic preprocessing
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Getting the list of stop words
stop_words = set(stopwords.words('english'))
existing_terms = set()
class MRWordCount(MRJob):
	
	#Need to get (term, docID) yield
	def mapper(self, _, line):
		doc_name = os.environ['map_input_file']

		#Getting the content from stored documents
		tokens = word_tokenize(line)

		print(tokens) #contains stop words
		
		#eliminating stop words from the documents
		terms = [word for word in tokens if not word in stop_words]
		terms = list(set(terms))
		
		print(terms) #doesnt contain stop words

		for term in terms:
			if(term, doc_name) not in existing_terms:
				yield(term, doc_name)
				existing_terms.add((term, doc_name))

	#need to reduce the (term -> [doc list]) yield
	def reducer(self, term, docs):
		lister = []
		lister.extend(docs)
		yield(term, lister) 
			


if __name__ == '__main__':
	MRWordCount.run()
