#!/usr/bin/env python
# coding: utf-8

# ## Challenge 2: Sets
# 
# There are a lot to learn about Python Sets and the information presented in the lesson is limited due to its length. To learn Python Sets in depth you are strongly encouraged to review the W3Schools tutorial on [Python Sets Examples and Methods](https://www.w3schools.com/python/python_sets.asp) before you work on this lab. Some difficult questions in this lab have their solutions in the W3Schools tutorial.
# 
# #### First, import the Python `random` libary

# In[1]:


import random


# #### In the cell below, create a list named `sample_list_1` with 80 random values. 
# 
# Requirements:
# 
# * Each value is an integer falling between 0 and 100.
# * Each value in the list is unique.
# 
# Print `sample_list_1` to review its values
# 
# *Hint: use `random.sample` ([reference](https://docs.python.org/3/library/random.html#random.sample)).*

# In[2]:


# Your code here
sample_list_1=random.sample(range(100),80)
print (sample_list_1)


# #### Convert `sample_list_1` to a set called `set1`. Print the length of the set. Is its length still 80?

# In[3]:


# Your code here
set1=set(sample_list_1)
print (len(set1))

# Si, sigue siendo 80 porque los elementos son unicos.


# #### Create another list named `sample_list_2` with 80 random values.
# 
# Requirements:
# 
# * Each value is an integer falling between 0 and 100.
# * The values in the list don't have to be unique.
# 
# *Hint: Use a FOR loop.*

# In[4]:


# Your code here
sample_list_2=[]
for i in range(80):
    a=random.randint(0,100)
    sample_list_2.append(a)
    
print (sample_list_2)    


# #### Convert `sample_list_2` to a set called `set2`. Print the length of the set. Is its length still 80?

# In[5]:


# Your code here
set2=set(sample_list_2)
print (len(set2))

# Ya no son 80 porque los elementos ya no son unicos y un set devuelve los elementos sin repeticion.


# #### Identify the elements present in `set1` but not in `set2`. Assign the elements to a new set named `set3`.

# In[6]:


# Your code here
set3=set1.difference(set2)


# #### Identify the elements present in `set2` but not in `set1`. Assign the elements to a new set named `set4`.

# In[7]:


# Your code here
set4=set2.difference(set1)


# #### Now Identify the elements shared between `set1` and `set2`. Assign the elements to a new set named `set5`.

# In[8]:


# Your code here
set5=set1.intersection(set2)


# #### What is the relationship among the following values:
# 
# * len(set1)
# * len(set2)
# * len(set3)
# * len(set4)
# * len(set5)
# 
# Use a math formular to represent that relationship. Test your formular with Python code.

# In[9]:


# Your code here

# La union es igual a la suma de ambos conjuntos menos la interseccion.

total1=len(set1)+len(set2)-len(set5)
total2=len(set3)+len(set4)+len(set5)

if total1==total2: print (True)


# #### Create an empty set called `set6`.

# In[10]:


# Your code here
set6=set()
print (type(set6))


# #### Add `set3` and `set5` to `set6` using the Python Set `update` method.

# In[11]:


# Your code here
set6.update(set3)
set6.update(set5)
print (set6)


# #### Check if `set1` and `set6` are equal.

# In[12]:


# Your code here
if set1==set6: 
    print (True)
else:
    print (False)


# #### Check if `set1` contains `set2` using the Python Set `issubset` method. Then check if `set1` contains `set3`.*

# In[13]:


# Your code here
print (set2.issubset(set1))
print (set3.issubset(set1))


# #### Using the Python Set `union` method, aggregate `set3`, `set4`, and `set5`. Then aggregate `set1` and `set2`. 
# 
# #### Check if the aggregated values are equal.

# In[14]:


# Your code here
print (len(set3.union(set4).union(set5)))
print (len(set1.union(set2)))


# #### Using the `pop` method, remove the first element from `set1`.

# In[15]:


# Your code here
print (set1)
set1.pop()


# #### Remove every element in the following list from `set1` if they are present in the set. Print the remaining elements.
# 
# ```
# list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
# ```

# In[16]:


# Your code here
list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]

print (set1)
print ('')
for e in list_to_remove:
    if e in set1:
        set1.remove(e)
        
print (set1)
        


# In[ ]:





# In[ ]:




