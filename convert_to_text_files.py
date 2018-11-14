'''

      id                  name
0      1        Hisashi Suzuki
1     10           David Brady
2    100  Santosh S. Venkatesh
3   1000     Charles Fefferman
4  10000         Artur Speiser




     id  year                                              title event_type  \
0     1  1987  Self-Organization of Associative Database and ...        NaN   
1    10  1987  A Mean Field Theory of Layer IV of Visual Cort...        NaN   
2   100  1988  Storing Covariance by the Associative Long-Ter...        NaN   
3  1000  1994  Bayesian Query Construction for Neural Network...        NaN   
4  1001  1994  Neural Network Ensembles, Cross Validation, an...        NaN   

                                            pdf_name          abstract  \
0  1-self-organization-of-associative-database-an...  Abstract Missing   
1  10-a-mean-field-theory-of-layer-iv-of-visual-c...  Abstract Missing   
2  100-storing-covariance-by-the-associative-long...  Abstract Missing   
3  1000-bayesian-query-construction-for-neural-ne...  Abstract Missing   
4  1001-neural-network-ensembles-cross-validation...  Abstract Missing   

                                          paper_text  
0  767\n\nSELF-ORGANIZATION OF ASSOCIATIVE DATABA...  
1  683\n\nA MEAN FIELD THEORY OF LAYER IV OF VISU...  
2  394\n\nSTORING COVARIANCE BY THE ASSOCIATIVE\n...  
3  Bayesian Query Construction for Neural\nNetwor...  
4  Neural Network Ensembles, Cross\nValidation, a...  





   id  paper_id  author_id
0   1        63         94
1   2        80        124
2   3        80        125
3   4        80        126
4   5        80        127




   id  paper_id  author_id                                              title  \
0   1        63         94                        Connectivity Versus Entropy   
1   2        80        124  Stochastic Learning Networks and their Electro...   
2   3        80        125  Stochastic Learning Networks and their Electro...   
3   4        80        126  Stochastic Learning Networks and their Electro...   
4   5        80        127  Stochastic Learning Networks and their Electro...   

                                          paper_text  
0  1\n\nCONNECTIVITY VERSUS ENTROPY\nYaser S. Abu...  
1  9\n\nStochastic Learning Networks and their El...  
2  9\n\nStochastic Learning Networks and their El...  
3  9\n\nStochastic Learning Networks and their El...  
4  9\n\nStochastic Learning Networks and their El...  


'''

import pandas as pd

authors_df = pd.read_csv("authors.csv")
author_paper_df = pd.read_csv("paper_authors.csv")
papers_df = pd.read_csv("papers.csv")
papers_df = papers_df[['id','title', 'paper_text']]


authors_df.rename(columns={'id': 'author_id'}, inplace=True)
papers_df.rename(columns={'id': 'paper_id'}, inplace=True)

df = pd.merge(author_paper_df, papers_df, on = 'paper_id')
#print(df.head())
print(list(authors_df))
print("############")
print()

#Build a dict of type (paper_id) -> [author_names]
paper_authors_dict = {}
for index, row in df.iterrows():
	l = authors_df[authors_df['author_id'] == row['author_id']]
	if row['paper_id'] in paper_authors_dict:
		paper_authors_dict[row['paper_id']].extend(list(l['name']))

	else:
		paper_authors_dict[row['paper_id']] = list(l['name'])


#print(paper_authors_dict)

df = df[['paper_id', 'title', 'paper_text']]
df.drop_duplicates(subset=['paper_id'], keep=False, inplace = True)


#### Putting the data into text files
for index, row in df.iterrows():
	try:
		with open(str("docs/" + row['title'] + ".txt"), "w+") as f:
			f.write(row['title'])
			
			key = str(paper_authors_dict[row['paper_id']])
			authors = key[1:-1] #removing the list brackets []
			f.write(authors)
			
			f.write(row['paper_text'])
	except:
		print("The file name might be having / which is causing directory problems, skipping...")

print("#### FILES CREATED ####")



