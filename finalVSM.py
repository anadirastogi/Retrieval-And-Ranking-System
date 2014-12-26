############################################################
# Vector Space Model Implementation using scikit learn
# The user enters a query
# Top 10 documents relevant to the query are returned
############################################################
import operator
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import *
import os 

stemmer = PorterStemmer()

f = open('stop_words.txt','r')
stop_words = f.read().split()

os.system('ls classic1/ > doclist2.txt')

f1 = open('doclist2.txt','r')
doclist = f1.read().split()

training_docs = []
for doc in doclist:
	f2 = open('classic1/'+doc,'r')
	data = ""
                 
    	for line in f2:
    		data += line 
	
	f2.close()   
	training_docs.append(data)

# Create the tf-idf weighted term document matrix 	
vectorizer = TfidfVectorizer()
listtf=vectorizer.fit_transform(training_docs).toarray()

#	query = raw_input("Enter query:")

qf = open('query_doc.txt','r')
query = qf.read()
#Preprocess the query: Remove stop words and stem the query terms
query_p=''
for word in query.split():
	if word.lower() not in stop_words:
		word = stemmer.stem(word.lower())			
		query_p += word
		query_p += ' ' 


# Transform the query into a vector
query_vect = vectorizer.transform([query_p])
dict_pair = {}

# Compute cosine similarity between the query vector and all the documents 
a = cosine_similarity(query_vect,listtf[0:])

i = 0
for cs in a[0]:
	dict_pair[i] = cs
	i = i + 1

# Sort the documents in decreasing order of cosine similarity values
# Return the names and cosine similarities of the top 10 documents relevant to the query 
dict_pair = sorted(dict_pair.iteritems(), key=operator.itemgetter(1),reverse=True)
print "Top 20 relevant documents with greater than zero similarity:"
print "Doc id		cosine similarity"
j = 0
for (key,value) in dict_pair:
	if value > 0:            #0.099
		print doclist[key],'\t',value
		j+=1
		if j==20:
			break
				
"""
	cont = raw_input("Do you have another query?(y/n)")
	if cont == 'n':
		break			
"""		
