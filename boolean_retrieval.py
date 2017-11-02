from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

documents = []

doc1 = "The students like the subject information retrival a lot because they want to understand how stuff like google works"
doc2 = "The students dont like to study operating systems because that shit is wack"

documents.append(doc1)
documents.append(doc2)

#Tokenizing the document
tokens = []
for doc in documents:
	tokens.extend(word_tokenize(doc))

#Getting the list of stop words
stop_words = set(stopwords.words('english'))

#eliminating stop words from the documents
terms = [word for word in tokens if not word in stop_words]

print(tokens)
print(terms)

for i in terms:
	print(i + "->", end= ' ')
	for j in documents:
		if i in j:
			print(1, end = ' ')
		else:
			print(0, end = ' ')
	print("\n")

#Enter query
q = input("Enter query: ")
qterms = q.split(" ")

relevant_docs = []
if qterms[1].lower() == 'and':
	doc_id = 1
	for doc in documents:
		if qterms[0] in doc and qterms[2] in doc:
			relevant_docs.append(doc_id)

		doc_id += 1
elif qterms[1].lower() == 'or':
	doc_id = 1
	for doc in documents:
		if qterms[0] in doc or qterms[2] in doc:
			relevant_docs.append(doc_id)

		doc_id += 1


if len(relevant_docs) == 0:
	print("No matching documents found!")
else:
	print("The relevant documents are: ", end = " ")
	for i in relevant_docs:
		print("Document:" + str(i), end = " ")

		