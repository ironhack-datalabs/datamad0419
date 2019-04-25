#!/usr/bin/env python
# coding: utf-8

# # Advanced Regular Expressions Lab
# 
# Complete the following set of exercises to solidify your knowledge of regular expressions.

# In[1]:


import re


# ### 1. Use a regular expression to find and extract all vowels in the following text.

# In[2]:


text = "This is going to be a sentence with a good number of vowels in it."


# In[3]:


res=re.findall('[aeiou]', text)
print (res)


# ### 2. Use a regular expression to find and extract all occurrences and tenses (singular and plural) of the word "puppy" in the text below.

# In[5]:


text = "The puppy saw all the rest of the puppies playing and wanted to join them. I saw this and wanted a puppy of my own!"


# In[6]:


res=re.findall('puppy|puppies', text)
print (res)


# ### 3. Use a regular expression to find and extract all tenses (present and past) of the word "run" in the text below.

# In[7]:


text = "I ran the relay race the only way I knew how to run it."


# In[8]:


res=re.findall('run|ran', text)
print (res)


# ### 4. Use a regular expression to find and extract all words that begin with the letter "r" from the previous text.

# In[12]:


res=re.findall('r[a-z]+', text)
print (res)


# ### 5. Use a regular expression to find and substitute the letter "i" for the exclamation marks in the text below.

# In[14]:


text = "Th!s !s a sentence w!th spec!al characters !n !t."


# In[15]:


res=re.sub('!', 'i', text)
print (res)


# ### 6. Use a regular expression to find and extract words longer than 4 characters in the text below.

# In[16]:


text = "This sentence has words of varying lengths."


# In[17]:


res=re.findall('[a-z][a-z][a-z][a-z]+', text)
print (res)


# ### 7. Use a regular expression to find and extract all occurrences of the letter "b", some letter(s), and then the letter "t" in the sentence below.

# In[18]:


text = "I bet the robot couldn't beat the other bot with a bat, but instead it bit me."


# In[20]:


res=re.findall('b\w+t', text)
print (res)


# ### 8. Use a regular expression to find and extract all words that contain either "ea" or "eo" in them.

# In[21]:


text = "During many of the peaks and troughs of history, the people living it didn't fully realize what was unfolding. But we all know we're navigating breathtaking history: Nearly every day could be — maybe will be — a book."


# In[24]:


res=re.findall('\w+[eo]\w+', text)
print (res)


# ### 9. Use a regular expression to find and extract all the capitalized words in the text below individually.

# In[25]:


text = "Teddy Roosevelt and Abraham Lincoln walk into a bar."


# In[27]:


res=re.findall('[A-Z]+\w+', text)
print (res)


# ### 10. Use a regular expression to find and extract all the sets of consecutive capitalized words in the text above.

# In[28]:


res=re.findall('[A-Z]+\w+ ?[A-Z]+\w+', text)
print (res)


# ### 11. Use a regular expression to find and extract all the quotes from the text below.
# 
# *Hint: This one is a little more complex than the single quote example in the lesson because there are multiple quotes in the text.*

# In[29]:


text = 'Roosevelt says to Lincoln, "I will bet you $50 I can get the bartender to give me a free drink." Lincoln says, "I am in!"'


# In[32]:


res=re.findall('\"(.*?)\"', text)
print (res)


# ### 12. Use a regular expression to find and extract all the numbers from the text below.

# In[34]:


text = "There were 30 students in the class. Of the 30 students, 14 were male and 16 were female. Only 10 students got A's on the exam."


# In[35]:


res=re.findall('[0-9]+', text)
print (res)


# ### 13. Use a regular expression to find and extract all the social security numbers from the text below.

# In[40]:


text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""


# In[37]:


res=re.findall('[0-9]+-[0-9]+-[0-9]+', text)
print (res)


# ### 14. Use a regular expression to find and extract all the phone numbers from the text below.

# In[45]:


res=re.findall('\([0-9]+\)[0-9]+-[0-9]+', text)
print (res)


# ### 15. Use a regular expression to find and extract all the formatted numbers (both social security and phone) from the text below.

# In[46]:


res=re.findall('[0-9]+-[0-9]+-[0-9]+|\([0-9]+\)[0-9]+-[0-9]+', text)
print (res)


# In[ ]:





# In[ ]:




