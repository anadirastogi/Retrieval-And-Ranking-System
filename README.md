# Retrieval-And-Ranking-System


1. What is this ? 

   This is a document retrieval system that returns the top 10 documents in proper ranking from the corpus based on the search query provided by the user.
--------------

2. How has it been implemented ?

    1) In Python
    2) Used a machine-learning library scikit-learn
    3) Used tf-idf calculator provided by the above mentioned library to implement Latent Semantic Indexing 
--------------

3. How does it work ? 

    1) User provides a search query 
    2) The query goes through preprocessing
        1) Stemming or lemmatization using Porter's algorithm
        2) Stop word removal 
    3) prepare a tf-idf vector for the query 
    4) Process the query vector against the document vectors through dot product 
    5) Extract and sort the top 10 documents based on the magnitude of the dot product
    

      
