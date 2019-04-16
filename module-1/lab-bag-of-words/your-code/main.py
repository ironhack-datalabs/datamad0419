#!/usr/bin/env python
# coding: utf-8

# Define `docs` array that contains the paths of `doc1.txt`, `doc2.txt`, and `doc3.txt`.

# In[1]:


docs = ['doc1.txt', 'doc2.txt', 'doc3.txt']


# Define an empty array `corpus` that will contain the content strings of the docs. Loop `docs` and read the content of each doc into the `corpus` array.

# In[2]:


corpus = []

# Write your code here
for doc in docs:
    with open(doc, 'r') as f:
        corpus.append(f.read())

print (corpus)        


# Print `corpus`.

# In[11]:


corpus=[corpus[i].lower() for i in range(len(corpus))]
corpus=[corpus[i].replace('.', '') for i in range(len(corpus))]
print(corpus)


# You should have seen:
# 
# ```['ironhack is cool', 'i love ironhack', 'i am a student at ironhack']```
# 
# However, if your output is:
# 
# ```['Ironhack is cool.', 'I love Ironhack.', 'I am a student at Ironhack.']```
# 
# This means you didn't:
# 
# 1. Remove punctuation from the strings;
# 
# 1. Convert strings to lowercase.
# 
# Revise your code above until you receive the correct output for `corpus`.

# Now define `bag_of_words` as an empty array. It will contain the unique terms in `corpus`.
# 
# Loop through `corpus`. In each loop, do the following:
# 
# 1. Break the string into an array of terms. 
# 1. Create a sub-loop to iterate the terms array. 
#   * In each sub-loop, you'll check if the current term is already contained in `bag_of_words`. If not in `bag_of_words`, append it to the array.

# In[49]:


bag_of_words = []

# Write your code here
for e in corpus:
    f=e.split(' ')
    for g in f:
        if g not in bag_of_words : bag_of_words.append(g)


# Print `bag_of_words`. You should see: 
# 
# ```['ironhack', 'is', 'cool', 'i', 'love', 'am', 'a', 'student', 'at']```

# In[50]:


print(bag_of_words)


# Now we define an empty array called `term_freq`. Loop `corpus` for a second time. In each loop, create a sub-loop to iterate the terms in `bag_of_words`. Count how many times each term appears in each doc of `corpus`. Append the term-frequency array to `term_freq`.

# In[76]:


term_freq = []

# Write your code here
for e in corpus:
    lista=[]
    e=e.split()
    for f in bag_of_words:
        if f in e:
            lista.append(1)
        else:
            lista.append(0)
    term_freq.append(lista) 


# Print `term_freq`. You should see:
# 
# ```[[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1]]```

# In[77]:


print(term_freq)


# **If your answer is correct, congratulations! You've solved the challenge!**
# 
# If not, go back and check for errors in your code.
