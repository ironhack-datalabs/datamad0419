#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# In[1]:


import numpy as np
import pandas as pd


# # Challenge 1 - Iterators, Generators and `yield`. 
# 
# In iterator in Python is an object that represents a stream of data. However, iterators contain a countable number of values. We traverse through the iterator and return one value at a time. All iterators support a `next` function that allows us to traverse through the iterator. We can create an iterator using the `iter` function that comes with the base package of Python. Below is an example of an iterator.

# In[2]:


# We first define our iterator:

iterator = iter([1,2,3])

# We can now iterate through the object using the next function

print(next(iterator))


# In[3]:


# We continue to iterate through the iterator.

print(next(iterator))


# In[4]:


print(next(iterator))


# In[5]:


# After we have iterated through all elements, we will get a StopIteration Error

#print(next(iterator))


# In[6]:


# We can also iterate through an iterator using a for loop like this:
# Note: we cannot go back directly in an iterator once we have traversed through the elements. 
# This is why we are redefining the iterator below

iterator = iter([1,2,3])

for i in iterator:
    print(i)


# In the cell below, write a function that takes an iterator and returns the first element in the iterator and returns the first element in the iterator that is divisible by 2. Assume that all iterators contain only numeric data. If we have not found a single element that is divisible by 2, return zero.

# In[93]:


def divisible2(iterator):
    # This function takes an iterable and returns the first element that is divisible by 2 and zero otherwise
    # Input: Iterable
    # Output: Integer
    
    # Sample Input: iter([1,2,3])
    # Sample Output: 2
    
    # Your code here:
    for i in iterator:
        if i%2==0  : return i
    return 0  
        
            
    

        
divisible2(iter([1,1,3]))     


# ### Generators
# 
# It is quite difficult to create your own iterator since you would have to implement a `next` function. Generators are functions that enable us to create iterators. The difference between a function and a generator is that instead of using `return`, we use `yield`. For example, below we have a function that returns an iterator containing the numbers 0 through n:

# In[7]:


def firstn(n):
     number = 0
     while number < n:
         yield number
         number = number + 1


# If we pass 5 to the function, we will see that we have a iterator containing the numbers 0 through 4.

# In[8]:


iterator = firstn(5)

for i in iterator:
    print(i)


# In the cell below, create a generator that takes a number and returns an iterator containing all even numbers between 0 and the number you passed to the generator.

# In[104]:


def even_iterator(n):
    # This function produces an iterator containing all even numbers between 0 and n
    # Input: integer
    # Output: iterator
    
    # Sample Input: 5
    # Sample Output: iter([0, 2, 4])
   
    # Your code here:
    yield iter([i for i in range(n) if i%2==0])


gen=even_iterator(5)
print (gen)
print (gen.__next__())   # comentar esta linea y descomentar la siguiente para ver resultado [0,2,4]
#print (list(gen.__next__())) 


# # Challenge 2 - Applying Functions to DataFrames
# 
# In this challenge, we will look at how to transform cells or entire columns at once.
# 
# First, let's load a dataset. We will download the famous Iris classification dataset in the cell below.

# In[60]:


columns = ['sepal_length', 'sepal_width', 'petal_length','petal_width','iris_type']
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=columns)


# Let's look at the dataset using the `head` function.

# In[62]:


# Your code here:
print (iris.head())


# Let's start off by using built-in functions. Try to apply the numpy mean function and describe what happens in the comments of the code.

# In[63]:


# Your code here:
mean=np.mean(iris)
print (mean)
# numpy esta haciendo la media del dataset por columnas, segun las dimensiones del sepalo y el petalo, 
# lo cual es correcto. Ademas solo efectua la operacion sobre los datos numericos.


# Next, we'll apply the standard deviation function in numpy (`np.std`). Describe what happened in the comments.

# In[64]:


# Your code here:
std=np.std(iris)
print (std)
# igual que antes numpy trabaja correctamente sobre los datos del dataframe,
# puede comprobarse con la funcion describe de pandas.
print (iris.describe())


# The measurements are in centimeters. Let's convert them all to inches. First, we will create a dataframe that contains only the numeric columns. Assign this new dataframe to `iris_numeric`.

# In[65]:


# Your code here:
names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
iris_numeric=pd.DataFrame(iris, columns=names)
    
print (iris_numeric.head())


# Next, we will write a function that converts centimeters to inches in the cell below. Recall that 1cm = 0.393701in.

# In[66]:


def cm_to_in(x):
    # This function takes in a numeric value in centimeters and converts it to inches
    # Input: numeric value
    # Output: float
    
    # Sample Input: 1.0
    # Sample Output: 0.393701
    
    # Your code here:
    return x*0.393701

print (cm_to_in(1.0))


# Now convert all columns in `iris_numeric` to inches in the cell below. We like to think of functional transformations as immutable. Therefore, save the transformed data in a dataframe called `iris_inch`.

# In[67]:


# Your code here:
iris_inch=pd.DataFrame(cm_to_in(iris_numeric), columns=names)
    
print(iris_inch.head())


# We have just found that the original measurements were off by a constant. Define the global constant `error` and set it to 2. Write a function that uses the global constant and adds it to each cell in the dataframe. Apply this function to `iris_numeric` and save the result in `iris_constant`.

# In[68]:


# Define constant below:
error=2

def add_constant(x):
    # This function adds a global constant to our input.
    # Input: numeric value
    # Output: numeric value
    
    # Your code here:
    return x+error

iris_constant=pd.DataFrame(add_constant(iris_numeric), columns=names)
print (iris_constant.head())


# # Bonus Challenge - Applying Functions to Columns
# 
# Read more about applying functions to either rows or columns [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html) and write a function that computes the maximum value for each row of `iris_numeric`

# In[69]:


# Your code here:
def maximum(x):
    M=0
    for e in x:
        if e>M: M=e
    return M

Max_row=iris_numeric.apply(maximum, axis=1)   # axis=1 es por filas 
print (Max_row.head())


# Compute the combined lengths for each row and the combined widths for each row using a function. Assign these values to new columns `total_length` and `total_width`.

# In[112]:


# Your code here:
def total(a, b):
    return a+b

iris_numeric['total_length']=total(iris_numeric['sepal_length'].values, iris_numeric['petal_length'].values)
iris_numeric['total_width']=total(iris_numeric['sepal_width'].values, iris_numeric['petal_width'].values)

print (iris_numeric.head())


# In[ ]:




