#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# In[1]:


import re


# # Challenge 1 - Combining Strings
# 
# Combining strings is an important skill to acquire. There are multiple ways of combining strings in Python, as well as combining strings with variables. We will explore this in the first challenge. In the cell below, combine the strings in the list and add spaces between the strings (do not add a space after the last string). Insert a period after the last string.

# In[2]:


str_list = ['Durante', 'un', 'tiempo', 'no', 'estuvo', 'segura', 'de', 'si', 'su', 'marido', 'era', 'su', 'marido']
# Your code here:
strings=' '.join(str_list)
strings+='.'
print (strings)


# In the cell below, use the list of strings to create a grocery list. Start the list with the string `Grocery list: ` and include a comma and a space between each item except for the last one. Include a period at the end. Only include foods in the list that start with the letter 'b' and ensure all foods are lower case.

# In[3]:


food_list = ['Bananas', 'Chocolate', 'bread', 'diapers', 'Ice Cream', 'Brownie Mix', 'broccoli']
# Your code here:
head='Grocery list: '
foods=' '.join(food_list)
foods=foods.lower()
foods=re.findall('b[a-z]+ ?[a-z]+', foods)
foods=', '.join(foods)+'.'
foods=head+foods
print (foods)


# In the cell below, write a function that computes the area of a circle using its radius. Compute the area of the circle and insert the radius and the area between the two strings. Make sure to include spaces between the variable and the strings. 
# 
# Note: You can use the techniques we have learned so far or use f-strings. F-strings allow us to embed code inside strings. You can read more about f-strings [here](https://www.python.org/dev/peps/pep-0498/).

# In[4]:


import math

string1 = "The area of the circle with radius:"
string2  = "is:"
radius = 4.5

def area(x, pi = math.pi):
    # This function takes a radius and returns the area of a circle. We also pass a default value for pi.
    # Input: Float (and default value for pi)
    # Output: Float
    
    # Sample input: 5.0
    # Sample Output: 78.53981633
    
    # Your code here:
    return pi*(x**2)
    
    
# Your output string here:
A=string1+' {} '.format(radius)+string2+' {:.3f} '.format(area(radius))
print (A)


# # Challenge 2 - Splitting Strings
# 
# We have first looked at combining strings into one long string. There are times where we need to do the opposite and split the string into smaller components for further analysis. 
# 
# In the cell below, split the string into a list of strings using the space delimiter. Count the frequency of each word in the string in a dictionary. Strip the periods, line breaks and commas from the text. Make sure to remove empty strings from your dictionary.

# In[5]:


poem = """Some say the world will end in fire,
Some say in ice.
From what I’ve tasted of desire
I hold with those who favor fire.
But if it had to perish twice,
I think I know enough of hate
To say that for destruction ice
Is also great
And would suffice."""

# Your code here:
S=re.findall('\w+', poem)
print (S)

print('')

F={}
for e in S:
    if e in F: F[e]+=1
    else : F[e]=1        
print (F)


# In the cell below, find all the words that appear in the text and do not appear in the blacklist. You must parse the string but can choose any data structure you wish for the words that do not appear in the blacklist. Remove all non letter characters and convert all words to lower case.

# In[12]:


blacklist = ['and', 'as', 'an', 'a', 'the', 'in', 'it']

poem = """I was angry with my friend; 
I told my wrath, my wrath did end.
I was angry with my foe: 
I told it not, my wrath did grow. 

And I waterd it in fears,
Night & morning with my tears: 
And I sunned it with smiles,
And with soft deceitful wiles. 

And it grew both day and night. 
Till it bore an apple bright. 
And my foe beheld it shine,
And he knew that it was mine. 

And into my garden stole, 
When the night had veild the pole; 
In the morning glad I see; 
My foe outstretched beneath the tree."""

# Your code here:
S=poem.lower()
S=re.findall('\w+', S)
Res=[e for e in S if e not in blacklist]
print (Res)


# # Challenge 3 - Regular Expressions
# 
# Sometimes, we would like to perform more complex manipulations of our string. This is where regular expressions come in handy. In the cell below, return all characters that are upper case from the string specified below.

# In[13]:


poem = """The apparition of these faces in the crowd;
Petals on a wet, black bough."""

# Your code here:
res=re.findall('[A-Z]', poem)
print (res)


# In the cell below, filter the list provided and return all elements of the list containing a number. To filter the list, use the `re.search` function. Check if the function does not return `None`. You can read more about the `re.search` function [here](https://docs.python.org/3/library/re.html).

# In[45]:


data = ['123abc', 'abc123', 'JohnSmith1', 'ABBY4', 'JANE']

# Your code here:
res=[re.search('^\d+[a-z]+|[a-z]+\d+$|[A-Z]+[a-z]+[A-Z]+[a-z]+\d$|[A-Z]+\d$', e).group(0)     for e in data if re.search('^\d+[a-z]+|[a-z]+\d+$|[A-Z]+[a-z]+[A-Z]+[a-z]+\d$|[A-Z]+\d$', e)!=None]
print (res) 


# # Bonus Challenge - Regular Expressions II
# 
# In the cell below, filter the list provided to keep only strings containing at least one digit and at least one lower case letter. As in the previous question, use the `re.search` function and check that the result is not `None`.
# 
# To read more about regular expressions, check out [this link](https://developers.google.com/edu/python/regular-expressions).

# In[ ]:


data = ['123abc', 'abc123', 'JohnSmith1', 'ABBY4', 'JANE']
# Your code here:


# In[48]:


res=[re.search('^\d+[a-z]+|[a-z]+\d+$|[A-Z]+[a-z]+[A-Z]+[a-z]+\d$', e).group(0)     for e in data if re.search('^\d+[a-z]+|[a-z]+\d+$|[A-Z]+[a-z]+[A-Z]+[a-z]+\d$', e)!=None]
print (res) 


# In[ ]:





# In[ ]:





# In[ ]:




