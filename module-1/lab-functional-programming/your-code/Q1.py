#!/usr/bin/env python
# coding: utf-8

# In the cell below, create a Python function that wraps your previous solution for the Bag of Words lab.
# 
# Requirements:
# 
# 1. Your function should accept the following parameters:
#     * `docs` [REQUIRED] - array of document paths.
#     * `stop_words` [OPTIONAL] - array of stop words. The default value is an empty array.
# 
# 1. Your function should return a Python object that contains the following:
#     * `bag_of_words` - array of strings of normalized unique words in the corpus.
#     * `term_freq` - array of the term-frequency vectors.

# In[8]:


# Import required libraries
from sklearn.feature_extraction import stop_words
# Define function
def get_bow_from_docs(docs, stop_words=[]):
    
    # In the function, first define the variables you will use such as `corpus`, `bag_of_words`, and `term_freq`.
    corpus = []
    bag_of_words = []
    term_freq = []
    """
    Loop `docs` and read the content of each doc into a string in `corpus`.
    Remember to convert the doc content to lowercases and remove punctuation.
    """
    for doc in docs:
        with open(doc, 'r') as f:
            corpus.append(f.read())
        
    corpus=[corpus[i].lower() for i in range(len(corpus))]
    corpus=[corpus[i].replace('.', '') for i in range(len(corpus))]
    
    """
    Loop `corpus`. Append the terms in each doc into the `bag_of_words` array. The terms in `bag_of_words` 
    should be unique which means before adding each term you need to check if it's already added to the array.
    In addition, check if each term is in the `stop_words` array. Only append the term to `bag_of_words`
    if it is not a stop word.
    """
    for e in corpus:
        f=e.split(' ')
        for g in f:
            if g not in bag_of_words and g not in stop_words : bag_of_words.append(g)

    
    
    
    """
    Loop `corpus` again. For each doc string, count the number of occurrences of each term in `bag_of_words`. 
    Create an array for each doc's term frequency and append it to `term_freq`.
    """
    for e in corpus:
        lista=[]
        e=e.split()
        for f in bag_of_words:
            if f in e:
                lista.append(1)
            else:
                lista.append(0)
        term_freq.append(lista) 

    
    
    # Now return your output as an object
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }
    


# Test your function without stop words. You should see the output like below:
# 
# ```{'bag_of_words': ['ironhack', 'is', 'cool', 'i', 'love', 'am', 'a', 'student', 'at'], 'term_freq': [[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1]]}```

# In[9]:


# Define doc paths array
docs = ['doc1.txt', 'doc2.txt', 'doc3.txt'] 


# Obtain BoW from your function
bow = get_bow_from_docs(docs)

# Print BoW
print(bow)


# ### If your attempt above is successful, nice work done!
# 
# Now test your function again with the stop words. In the previous lab we defined the stop words in a large array. In this lab, we'll import the stop words from Scikit-Learn.

# In[10]:


#from sklearn.feature_extraction import stop_words
print(stop_words.ENGLISH_STOP_WORDS)


# You should have seen a large list of words that looks like:
# 
# ```frozenset({'across', 'mine', 'cannot', ...})```
# 
# `frozenset` is a type of Python object that is immutable. In this lab you can use it just like an array without conversion.

# Next, test your function with supplying `stop_words.ENGLISH_STOP_WORDS` as the second parameter.

# In[11]:


bow = get_bow_from_docs(docs, stop_words.ENGLISH_STOP_WORDS)

print(bow)


# You should have seen:
# 
# ```{'bag_of_words': ['ironhack', 'cool', 'love', 'student'], 'term_freq': [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]}```

# In[ ]:




