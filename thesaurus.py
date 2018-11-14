#### EXPERIMENTAL

	#Obtaining the term synopsis
	term1_syn = Word(term1)
	term1_syn = term1_syn.synonyms()[:3]
	term1_syn.insert(0, term1)
	term1_syn = [word for word in term1_syn if word in term_dict] #eliminating synonymns not present in the collection
	

	term2_syn = Word(term2)
	term2_syn = term2_syn.synonyms()[:3]
	term2_syn.insert(0, term2)
	term2_syn = [word for word in term2_syn if word in term_dict]
	
	#List of documents relevant to term1 and term2 respectively
	doc_term1 = []
	doc_term2 = []


	for term in term1_syn:
		if flag1 == True:
			doc_term1.extend(term_dict[term])
		else:
			for doc in document_list:
				if doc not in doc_seen and doc not in term_dict[term]:
					doc_term1.extend(doc)
					doc_seen.add(doc)

		doc_term1 = list(set(doc_term1)) #removing duplicates

	
	doc_seen = set()
	for term in term2_syn:
		if flag1 == True:
			doc_term2.extend(term_dict[term])
		else:
			for doc in document_list:
				if doc not in doc_seen and doc not in term_dict[term]:
					doc_term2.extend(doc)
					doc_seen.add(doc)

		doc_term1 = list(set(doc_term2)) #removing duplicates