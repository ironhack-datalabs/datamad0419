#!/usr/bin/env python
# coding: utf-8

# **Lambda** is a special Python function type that is **anonymous**. By *anonymous* it means a lambda function does not have name. Lambda functions are embedded inside codes so that you don't call them like calling regular Python functions.
# 
# **`Map`** applies a function to all the items in an input list. The function that is applied can be a standard or a lambda function.
# 
# For instance, below is an example of multiplying number tuples in a list:

# In[1]:


items = [(1,2), (3,4), (5,6)]

def multiply(num_tuple):
    return num_tuple[0]*num_tuple[1]
list(map(multiply, items))


# ...is the same as:

# In[2]:


items = [(1,2), (3,4), (5,6)]
list(map(lambda item: item[0]*item[1], items))


# Why do we sometimes use `lambda` and `map`? Because, as you see in the example above, they make your code really concise by combining 3 lines of code to 1 line.
# 
# Besides `map`, there is also **`filter`** that selectively returns elements in an array according to whether you return `True`. There is also **`reduce`** that performs computation on a list of items then returns result.
# 
# Here is a [good tutorial](http://book.pythontips.com/en/latest/map_filter.html) about `map`, `filter`, and `reduce`. Read it if you are not familiar with how they are used. Then proceed to the next cell.

# In the next cell, use `filter` and `lambda` to return a list that contains positive numbers only. The output should be:
# 
# ```[1, 4, 5]```

# In[3]:


numbers = [1, 4, -1, -100, 0, 5, -99]

# Enter your code below
res=list(filter(lambda x: x>0, numbers))
print (res)


# Next, use `reduce` and `lambda` to return a string that only contains English terms. The English terms are separated with a whitespace ` `.
# 
# Hints: 
# 
# * If your Jupyter Notebook cannot import `langdetect`, you need to install it with `pip install langdetect`. If Jupyter Notebook still cannot find the library, try install with `python3 -m pip install langdetect`. This is because you need to install `langdetect` in the same Python run environment where Jupyter Notebook is running.
# 
# * If a word is English, `langdetect.detect(word)=='en'` will return `True`.
# 
# Your output should read:
# 
# ```'good morning everyone'```

# In[7]:


import langdetect
from functools import reduce
words = ['good morning', '早上好', 'доброго', 'おはようございます', 'everyone', '大家', 'каждый', 'みんな']

# Enter your code below
res=reduce(lambda x,y: x+" "+y if langdetect.detect(y)=='en' else x, words)
print (res)


# # Bonus Question

# Finally, if you still have time, convert your response in Q2 by using `lambda`, `map`, `filter`, or `reduce` where applicable. Enter your function in the cell below.
# 
# As you write Python functions, generally you don't want to make your function too long. Long functions are difficult to read and difficult to debug. If a function is getting too long, consider breaking it into sever shorter functions where the main function calls other functions. If anything goes wrong, you can output debug messages in each of the functions to check where exactly the error is.

# In[59]:


# Enter your code below
def get_bow_from_docs(docs, stop_words=[]):
    # In the function, first define the variables you will use such as `corpus`, `bag_of_words`, and `term_freq`.
    corpus = []
    bag_of_words = []
    term_freq = []
    
    # write your codes here
    
    for doc in docs:
        with open(doc, 'r') as f:
            F=f.read()
            #F=strip_html_tags(F)
            #F=remove_punctuation(F)
            #F=remove_unicode(F)
            corpus.append(F)
    
    corpus=[corpus[i].lower() for i in range(len(corpus))]
    corpus=[corpus[i].replace('.', '') for i in range(len(corpus))]
    
    for e in corpus:
        f=e.split(' ')
        for g in f:
            if g not in bag_of_words : bag_of_words.append(g)
            

    
    bag_of_words=[e for e in bag_of_words if e]   # elimina strings vacios
    
    bag_of_words=list(filter(lambda x: len(x)>3, bag_of_words))
    
    for e in corpus:
        lista=[]
        for f in bag_of_words:
            if f in e: lista.append(1)
            else: lista.append(0)
        term_freq.append(lista) 
    
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }
    


# Test your function below with the Bag of Words lab docs (it's easier for you to debug your code). Your output should be:
# 
# ```{'bag_of_words': ['ironhack', 'cool', 'love', 'student'], 'term_freq': [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]}```

# In[60]:


from sklearn.feature_extraction import stop_words
bow = get_bow_from_docs([
    '../../lab-bag-of-words/your-code/doc1.txt', 
    '../../lab-bag-of-words/your-code/doc2.txt', 
    '../../lab-bag-of-words/your-code/doc3.txt'],
    stop_words.ENGLISH_STOP_WORDS
)

print(bow)


# In[ ]:




