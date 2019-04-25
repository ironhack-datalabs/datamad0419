#!/usr/bin/env python
# coding: utf-8

# Now we want to enhance the `get_bow_from_docs` function so that it will work with HTML webpages. In HTML, there are a lot of messy codes such as HTML tags, Javascripts, [unicodes](https://www.w3schools.com/charsets/ref_utf_misc_symbols.asp) that will mess up your bag of words. We need to clean up those junk before generating BoW.
# 
# Next, what you will do is to define several new functions each of which is specialized to clean up the HTML codes in one aspect. For instance, you can have a `strip_html_tags` function to remove all HTML tags, a `remove_punctuation` function to remove all punctuation, a `to_lower_case` function to convert string to lowercase, and a `remove_unicode` function to remove all unicodes.
# 
# Then in your `get_bow_from_doc` function, you will call each of those functions you created to clean up the HTML before you generate the corpus.
# 
# Note: Please use Python string operations and regular expression only in this lab. Do not use extra libraries such as `beautifulsoup` because otherwise you loose the purpose of practicing.

# In[58]:


# Define your string handling functions below
# Minimal 3 functions
import re

def strip_html_tags(doc):                # elimina tags
    return re.sub("\<(.*?)\>",'', doc)



def remove_punctuation(doc):  # quita puntuaciones
    return re.sub('\W', ' ', doc)



def remove_unicode(doc):          # quita unicode
    return doc.encode('ascii', errors='ignore').strip().decode('ascii')


# Next, paste your previously written `get_bow_from_docs` function below. Call your functions above at the appropriate place.

# In[59]:


def get_bow_from_docs(docs, stop_words=[]):
    # In the function, first define the variables you will use such as `corpus`, `bag_of_words`, and `term_freq`.
    corpus = []
    bag_of_words = []
    term_freq = []
    
    # write your codes here
    
    for doc in docs:
        with open(doc, 'r') as f:
            F=f.read()
            F=strip_html_tags(F)
            F=remove_punctuation(F)
            F=remove_unicode(F)
            corpus.append(F)
    
    corpus=[corpus[i].lower() for i in range(len(corpus))]
    corpus=[corpus[i].replace('.', '') for i in range(len(corpus))]
    
    for e in corpus:
        f=e.split(' ')
        for g in f:
            if g not in bag_of_words : bag_of_words.append(g)
            
    for e in corpus:
        lista=[]
    e=e.split()
    for f in bag_of_words:
        if f in e:
            lista.append(1)
        else:
            lista.append(0)
        term_freq.append(lista) 
    
    bag_of_words=[e for e in bag_of_words if e]   # elimina strings vacios
     
    
    return {
        "bag_of_words": bag_of_words,
        "term_freq": term_freq
    }
    


# Next, read the content from the three HTML webpages in the `your-codes` directory to test your function.

# In[64]:


from sklearn.feature_extraction import stop_words
bow = get_bow_from_docs([
        'en.wikipedia.org_Data_analysis.html',
        'www.coursereport.com_ironhack.html',
        'www.lipsum.com.html'
    ],
    stop_words.ENGLISH_STOP_WORDS
)

print(bow)
# he probado solamente con la pagina de lipsum, con las otras dos paginas me da un error IOPub data rate exceeded


# Do you see any problem in the output? How do you improve the output?
# 
# A good way to improve your codes is to look into the HTML data sources and try to understand where the messy output came from. A good data analyst always learns about the data in depth in order to perform the job well.
# 
# Spend 20-30 minutes to improve your functions or until you feel you are good at string operations. This lab is just a practice so you don't need to stress yourself out. If you feel you've practiced enough you can stop and move on the next challenge question.

# In[ ]:




