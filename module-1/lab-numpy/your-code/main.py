#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Import the NUMPY package under the name np.
import numpy as np


# In[2]:


#2. Print the NUMPY version and the configuration.
print(np.version.version)


# In[3]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a=np.random.rand(2,3,5)


# In[4]:


#4. Print a.
print(a)


# In[5]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b=np.full((5,2,3),1)


# In[6]:


#6. Print b.
print(b)


# In[7]:


#7. Do a and b have the same size? How do you prove that in Python code?
print(a.size)
print(b.size)
if a.size==b.size:
    print (True)


# In[8]:


#8. Are you able to add a and b? Why or why not?
#print(np.add(a, b))
#No, because they do not have the same shape


# In[ ]:





# In[9]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
print(b.shape)
c = np.transpose(b, (1, 2, 0))
print(c)
print(c.shape)


# In[10]:


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d=np.add(a, c)
print(d)
#Because now they do have the same shape


# In[11]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(a.shape)
print(d)
print(d.shape)

#Yes,d is a plus 1


# In[12]:


#12. Multiply a and c. Assign the result to e.
e=a*c
print(e)


# In[13]:


#13. Does e equal to a? Why or why not?
if (e==a).all(): 
    print(True)
else: 
    print(False)
#because a*1=a


# In[14]:


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max=np.amax(d)
print(d_max)
d_min=np.amin(d)
print (d_min)
d_mean=np.mean(d)
print(d_mean)


# In[15]:


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f=np.empty((2,3,5))
print(f)


# In[16]:


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
for i in d[:,:,:]:
    for l in i[:]:
        for j in l:
            x=np.where(d==j)[0][0]
            y= np.where(d==j)[1][0]
            z= np.where(d==j)[2][0]
            if j>d_min and j<d_mean:
                f[x,y,z]=25
            elif j>d_mean and j<d_max:
                f[x,y,z]=75
            elif j==d_mean:
                f[x,y,z]=50
            elif j==d_min:
                f[x,y,z]=0
            elif j==d_max:
                f[x,y,z]=100
print(f)

        


# In[17]:


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(d)
print(f)
#Yes, I have my expected f


# In[1]:


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""


# In[ ]:




