#######################################################
# Code to remove stopwords from the documents
# and perform stemming
#######################################################
import os
from nltk.stem.porter import *

os.system('mkdir classic1')
os.system('ls classic/ > doclist.txt')

f = open('stop_words.txt','r')
stop_words = f.read().split()

f1 = open('doclist.txt','r')
doclist = f1.read().split()

stemmer = PorterStemmer()
i=0

for doc in doclist:
	i+=1
	f2 = open('classic/'+doc,'r')
	words = f2.read().split()
	f3 = open('classic1/'+doc,'w')
	for word in words: 
		if word.lower() not in stop_words:
			word = stemmer.stem(word.lower())			
			f3.write(word + ' ')
	if i == 4000:
		break
		
	
	
