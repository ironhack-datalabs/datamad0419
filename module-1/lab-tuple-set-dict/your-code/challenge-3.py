#!/usr/bin/env python
# coding: utf-8

# ## Challenge 3: Dictionaries
# 
# In this challenge you will practice how to manipulate Python dictionaries. Before starting on this challenge, you are encouraged to review W3School's [Python Dictionary Examples and Methods](https://www.w3schools.com/python/python_dictionaries.asp).
# 
# First thing you will practice is how to sort the keys in a dictionary. Unlike the list object, Python dictionary does not have a built-in *sort* method. You'll need to use FOR loops to to sort dictionaries either by key or by value.
# 
# The dictionary below is a summary of the word frequency of Ed Sheeran's song *Shape of You*. Each key is a word in the lyrics and the value is the number of times that word appears in the lyrics.

# In[1]:


word_freq = {'love': 25, 'conversation': 1, 'every': 6, "we're": 1, 'plate': 1, 'sour': 1, 'jukebox': 1, 'now': 11, 'taxi': 1, 'fast': 1, 'bag': 1, 'man': 1, 'push': 3, 'baby': 14, 'going': 1, 'you': 16, "don't": 2, 'one': 1, 'mind': 2, 'backseat': 1, 'friends': 1, 'then': 3, 'know': 2, 'take': 1, 'play': 1, 'okay': 1, 'so': 2, 'begin': 1, 'start': 2, 'over': 1, 'body': 17, 'boy': 2, 'just': 1, 'we': 7, 'are': 1, 'girl': 2, 'tell': 1, 'singing': 2, 'drinking': 1, 'put': 3, 'our': 1, 'where': 1, "i'll": 1, 'all': 1, "isn't": 1, 'make': 1, 'lover': 1, 'get': 1, 'radio': 1, 'give': 1, "i'm": 23, 'like': 10, 'can': 1, 'doing': 2, 'with': 22, 'club': 1, 'come': 37, 'it': 1, 'somebody': 2, 'handmade': 2, 'out': 1, 'new': 6, 'room': 3, 'chance': 1, 'follow': 6, 'in': 27, 'may': 2, 'brand': 6, 'that': 2, 'magnet': 3, 'up': 3, 'first': 1, 'and': 23, 'pull': 3, 'of': 6, 'table': 1, 'much': 2, 'last': 3, 'i': 6, 'thrifty': 1, 'grab': 2, 'was': 2, 'driver': 1, 'slow': 1, 'dance': 1, 'the': 18, 'say': 2, 'trust': 1, 'family': 1, 'week': 1, 'date': 1, 'me': 10, 'do': 3, 'waist': 2, 'smell': 3, 'day': 6, 'although': 3, 'your': 21, 'leave': 1, 'want': 2, "let's": 2, 'lead': 6, 'at': 1, 'hand': 1, 'how': 1, 'talk': 4, 'not': 2, 'eat': 1, 'falling': 3, 'about': 1, 'story': 1, 'sweet': 1, 'best': 1, 'crazy': 2, 'let': 1, 'too': 5, 'van': 1, 'shots': 1, 'go': 2, 'to': 2, 'a': 8, 'my': 33, 'is': 5, 'place': 1, 'find': 1, 'shape': 6, 'on': 40, 'kiss': 1, 'were': 3, 'night': 3, 'heart': 3, 'for': 3, 'discovering': 6, 'something': 6, 'be': 16, 'bedsheets': 3, 'fill': 2, 'hours': 2, 'stop': 1, 'bar': 1}


# #### Sort the keys of `word_freq` ascendingly.
# 
# Please create a new dictionary called `word_freq2` based on `word_freq` with the keys sorted ascedingly.
# 
# There are several ways to achieve that goal but many of the ways are beyond what we have covered so far in the course. There is one way that we'll describe employing what you have learned. Please feel free to use this way or any other way you want.
# 
# 1. First extract the keys of `word_freq` and convert it to a list called `keys`.
# 
# 1. Sort the `keys` list.
# 
# 1. Create an empty dictionary `word_freq2`.
# 
# 1. Use a FOR loop to iterate each value in `keys`. For each key iterated, find the corresponding value in `word_freq` and insert the key-value pair to `word_freq2`.
# 
# Print out `word_freq2` to examine its keys and values. Your output should be:
# 
# ```python
# {'a': 8, 'about': 1, 'all': 1, 'although': 3, 'and': 23, 'are': 1, 'at': 1, 'baby': 14, 'backseat': 1, 'bag': 1, 'bar': 1, 'be': 16, 'bedsheets': 3, 'begin': 1, 'best': 1, 'body': 17, 'boy': 2, 'brand': 6, 'can': 1, 'chance': 1, 'club': 1, 'come': 37, 'conversation': 1, 'crazy': 2, 'dance': 1, 'date': 1, 'day': 6, 'discovering': 6, 'do': 3, 'doing': 2, "don't": 2, 'drinking': 1, 'driver': 1, 'eat': 1, 'every': 6, 'falling': 3, 'family': 1, 'fast': 1, 'fill': 2, 'find': 1, 'first': 1, 'follow': 6, 'for': 3, 'friends': 1, 'get': 1, 'girl': 2, 'give': 1, 'go': 2, 'going': 1, 'grab': 2, 'hand': 1, 'handmade': 2, 'heart': 3, 'hours': 2, 'how': 1, 'i': 6, "i'll": 1, "i'm": 23, 'in': 27, 'is': 5, "isn't": 1, 'it': 1, 'jukebox': 1, 'just': 1, 'kiss': 1, 'know': 2, 'last': 3, 'lead': 6, 'leave': 1, 'let': 1, "let's": 2, 'like': 10, 'love': 25, 'lover': 1, 'magnet': 3, 'make': 1, 'man': 1, 'may': 2, 'me': 10, 'mind': 2, 'much': 2, 'my': 33, 'new': 6, 'night': 3, 'not': 2, 'now': 11, 'of': 6, 'okay': 1, 'on': 40, 'one': 1, 'our': 1, 'out': 1, 'over': 1, 'place': 1, 'plate': 1, 'play': 1, 'pull': 3, 'push': 3, 'put': 3, 'radio': 1, 'room': 3, 'say': 2, 'shape': 6, 'shots': 1, 'singing': 2, 'slow': 1, 'smell': 3, 'so': 2, 'somebody': 2, 'something': 6, 'sour': 1, 'start': 2, 'stop': 1, 'story': 1, 'sweet': 1, 'table': 1, 'take': 1, 'talk': 4, 'taxi': 1, 'tell': 1, 'that': 2, 'the': 18, 'then': 3, 'thrifty': 1, 'to': 2, 'too': 5, 'trust': 1, 'up': 3, 'van': 1, 'waist': 2, 'want': 2, 'was': 2, 'we': 7, "we're": 1, 'week': 1, 'were': 3, 'where': 1, 'with': 22, 'you': 16, 'your': 21}
# ```

# In[15]:


# Your code here
keys=word_freq.keys()
keys=sorted(keys)
word_freq2={}

for e in keys:
    word_freq2[e]=word_freq[e]
    
print (word_freq2)    
    


# #### Sort the values of `word_freq` ascendingly.
# 
# Sorting the values of a dictionary is more tricky than sorting the keys because a dictionary's values are not unique. Therefore you cannot use the same way you sorted dict keys to sort dict values.
# 
# The way to sort a dict by value is to utilize the `sorted` and `operator.itemgetter` functions. The following code snippet is provided to you to try. It will give you a list of tuples in which each tuple contains the key and value of a dict item. And the list is sorted based on the dict value ([reference](http://thomas-cokelaer.info/blog/2017/12/how-to-sort-a-dictionary-by-values-in-python/)
# ).
# 
# ```python
# import operator
# sorted_tups = sorted(word_freq.items(), key=operator.itemgetter(1))
# print(sorted_tups)
# ```
# 
# Therefore, the steps to sort `word_freq` by value are:
# 
# * Using `sorted` and `operator.itemgetter`, obtain a list of tuples of the dict key-value pairs which is sorted on the value.
# 
# * Create an empty dictionary named `word_freq2`.
# 
# * Iterate the list of tuples. Insert each key-value pair into `word_freq2` as an object.
# 
# Print `word_freq2` to confirm your dictionary has its values sorted. Your output should be:
# 
# ```python
# {'conversation': 1, "we're": 1, 'plate': 1, 'sour': 1, 'jukebox': 1, 'taxi': 1, 'fast': 1, 'bag': 1, 'man': 1, 'going': 1, 'one': 1, 'backseat': 1, 'friends': 1, 'take': 1, 'play': 1, 'okay': 1, 'begin': 1, 'over': 1, 'just': 1, 'are': 1, 'tell': 1, 'drinking': 1, 'our': 1, 'where': 1, "i'll": 1, 'all': 1, "isn't": 1, 'make': 1, 'lover': 1, 'get': 1, 'radio': 1, 'give': 1, 'can': 1, 'club': 1, 'it': 1, 'out': 1, 'chance': 1, 'first': 1, 'table': 1, 'thrifty': 1, 'driver': 1, 'slow': 1, 'dance': 1, 'trust': 1, 'family': 1, 'week': 1, 'date': 1, 'leave': 1, 'at': 1, 'hand': 1, 'how': 1, 'eat': 1, 'about': 1, 'story': 1, 'sweet': 1, 'best': 1, 'let': 1, 'van': 1, 'shots': 1, 'place': 1, 'find': 1, 'kiss': 1, 'stop': 1, 'bar': 1, "don't": 2, 'mind': 2, 'know': 2, 'so': 2, 'start': 2, 'boy': 2, 'girl': 2, 'singing': 2, 'doing': 2, 'somebody': 2, 'handmade': 2, 'may': 2, 'that': 2, 'much': 2, 'grab': 2, 'was': 2, 'say': 2, 'waist': 2, 'want': 2, "let's": 2, 'not': 2, 'crazy': 2, 'go': 2, 'to': 2, 'fill': 2, 'hours': 2, 'push': 3, 'then': 3, 'put': 3, 'room': 3, 'magnet': 3, 'up': 3, 'pull': 3, 'last': 3, 'do': 3, 'smell': 3, 'although': 3, 'falling': 3, 'were': 3, 'night': 3, 'heart': 3, 'for': 3, 'bedsheets': 3, 'talk': 4, 'too': 5, 'is': 5, 'every': 6, 'new': 6, 'follow': 6, 'brand': 6, 'of': 6, 'i': 6, 'day': 6, 'lead': 6, 'shape': 6, 'discovering': 6, 'something': 6, 'we': 7, 'a': 8, 'like': 10, 'me': 10, 'now': 11, 'baby': 14, 'you': 16, 'be': 16, 'body': 17, 'the': 18, 'your': 21, 'with': 22, "i'm": 23, 'and': 23, 'love': 25, 'in': 27, 'my': 33, 'come': 37, 'on': 40}
# ```

# In[38]:


# Your code here
import operator
sort=sorted(word_freq.items(), key=operator.itemgetter(1))
word_freq2={}


for i in range(len(sort)):
    word_freq2.update({sort[i][0]:sort[i][1]})

print (word_freq2)    


# #### Convert `word_freq` into Pandas dataframes
# 
# In your future work, you may need to convert Python dictionaries to Pandas dataframes. So let's practice this by converting `word_freq`.
# 
# **First, import the `pandas` library.**

# In[25]:


import pandas as pd


# **Then, use the `pd.DataFrame()` constructor to convert `word_freq` into a dataframe.**
# 
# Here's a [reference](https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe) to show you how to accomplish this. Also name the two columns of the dataframe as `word` and `freq`.
# 
# Assign the converted value to a variable called `df`. The first few rows of `df` should look like this:
# 
# ![df](df.png)

# In[31]:


# Your code here
df=pd.DataFrame(word_freq.items(), columns=['word','freq'])
print (df)


# With the Pandas DataFrame, you can sort the values easily with the built-in method `sort_values` ([reference](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html)).
# 
# #### Sort `df` ascendingly based on column `word`.

# In[35]:


# Your code here
df=df.sort_values(by=['word'], axis=0, ascending=True)
print (df)


# #### Sort `df` ascendingly based on column `freq`.

# In[36]:


# Your code here
df=df.sort_values(by=['freq'], axis=0, ascending=True)
print (df)


# In[ ]:




