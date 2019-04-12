#!/usr/bin/env python
# coding: utf-8

# ## Challenge 1: Tuples
# 
# #### Do you know you can create tuples with only one element?
# 
# **In the cell below, define a variable `tup` with a single element `"I"`.**
# 
# *Hint: you need to add a comma (`,`) after the single element.*

# In[5]:


# Your code heretup
tup=("I",)


# #### Print the type of `tup`. 
# 
# Make sure its type is correct (i.e. *tuple* instead of *str*).

# In[6]:


# Your code here
print (type(tup))


# #### Now try to append the following elements to `tup`. 
# 
# Are you able to do it? Explain.
# 
# ```
# "r", "o", "n", "h", "a", "c", "k',
# ```

# In[7]:


# Your code here
tup.append("r")
tup.append("o")
tup.append("n")
tup.append("h")
tup.append("a")
tup.append("c")
tup.append("k")

# Your explanation here
# Las tuplas son objetos inmutables, no pueden modificarse una vez creadas.


# #### How about re-assign a new value to an existing tuple?
# 
# Re-assign the following elements to `tup`. Are you able to do it? Explain.
# 
# ```
# "I", "r", "o", "n", "h", "a", "c", "k"
# ```

# In[8]:


# Your code here

# este codigo esta comentado
'''
tup[0]="r"
tup[0]="o"
tup[0]="n"
tup[0]="H"
'''

# Your explanation here
# La razon es la misma de antes, aunque puede hacerse...

tup=list(tup)
tup="Ironhack"
tup=tuple(tup)
print (tup)


# #### Split `tup` into `tup1` and `tup2` with 4 elements in each. 
# 
# `tup1` should be `("I", "r", "o", "n")` and `tup2` should be `("h", "a", "c", "k")`.
# 
# *Hint: use positive index numbers for `tup1` assignment and use negative index numbers for `tup2` assignment. Positive index numbers count from the beginning whereas negative index numbers count from the end of the sequence.*
# 
# Also print `tup1` and `tup2`.

# In[9]:


# Your code here
tup1=tuple(tup[0]+tup[1]+tup[2]+tup[3])
tup2=tuple(tup[-4]+tup[-3]+tup[-2]+tup[-1])
print (tup1)
print (tup2)


# #### Add `tup1` and `tup2` into `tup3` using the `+` operator.
# 
# Then print `tup3` and check if `tup3` equals to `tup`.

# In[15]:


# Your code here
tup3=tup1+tup2
print (tup3)
# tup es igual a tup3


# #### Count the number of elements in `tup1` and `tup2`. Then add the two counts together and check if the sum is the same as the number of elements in `tup3`

# In[17]:


# Your code here
print (len(tup1))
print (len(tup2))
print (len(tup1)+len(tup2))
print (len(tup3))


# #### What is the index number of `"h"` in `tup3`?

# In[18]:


# Your code here
h=tup3[4]
print (h)


# #### Now, use a FOR loop to check whether each letter in the following list is present in `tup3`:
# 
# ```
# letters = ["a", "b", "c", "d", "e"]
# ```
# 
# For each letter you check, print `True` if it is present in `tup3` otherwise print `False`.
# 
# *Hint: you only need to loop `letters`. You don't need to loop `tup3` because there is a Python operator `in` you can use. See [reference](https://stackoverflow.com/questions/17920147/how-to-check-if-a-tuple-contains-an-element-in-python).*

# In[24]:


# Your code here
letters = ["a", "b", "c", "d", "e"]

for e in letters:
    if e in tup3:
        print (True)
    else:
        print (False)
   
    


# #### How many times does each letter in `letters` appear in `tup3`?
# 
# Print out the number of occurrence of each letter.

# In[47]:


# Your code here
for e in letters:
    if e in tup3:
        for i in tup3:
            v=0
            if e==i:
                v+=1
                print ('la letra {} aparece {} veces'.format(e, v))
    else:
        continue
   
    


# In[ ]:





# In[ ]:




