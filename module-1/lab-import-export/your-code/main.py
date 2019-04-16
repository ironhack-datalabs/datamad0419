

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# # Challenge 1 - Working with JSON files
# 
# Import the pandas library

# In[1]:


# Your import here:
import pandas as pd


# ####  After importing pandas, let's find a dataset. In this lesson we will be working with a NASA dataset.
# 
# Run the code in the cell below to load the dataset containing information about asteroids that have landed on earth. This piece of code helps us open the URL for the dataset and deocde the data using UTF-8.

# In[2]:


# Run this code

from urllib.request import urlopen
import json

response = urlopen("https://data.nasa.gov/resource/y77d-th95.json")
json_data = response.read().decode('utf-8', 'replace')


# In the next cell, load the data in `json_data` and load it into a pandas dataframe. Name the dataframe `nasa`.

# In[3]:


# Your code here:
nasa=pd.read_json(json_data, orient='records')


# Now that we have loaded the data, let's examine it using the `head()` function.

# In[4]:


# Your code here:
print (nasa.head())


# #### The `value_counts()` function is commonly used in pandas to find the frequency of every value in a column.
# 
# In the cell below, use the `value_counts()` function to determine the frequency of all types of asteroid landings by applying the function to the `fall` column.

# In[5]:


# Your code here:
print (nasa['fall'].value_counts())


# Finally, let's save the dataframe as a json file again. Since we downloaded the file from an online source, the goal of saving the dataframe is to have a local copy. Save the dataframe using the `orient=records` argument and name the file `nasa.json`.

# In[6]:


# Your code here:
nasa.to_json('nasa.json',orient='records')


# # Challenge 2 - Working with CSV and Other Separated Files
# 
# csv files are more commonly used as dataframes. In the cell below, load the file from the URL provided using the `read_csv()` function in pandas. Starting version 0.19 of pandas, you can load a csv file into a dataframe directly from a URL without having to load the file first like we did with the JSON URL. The dataset we will be using contains informtaions about NASA shuttles. 
# 
# In the cell below, we define the column names and the URL of the data. Following this cell, read the tst file to a variable called `shuttle`. Since the file does not contain the column names, you must add them yourself using the column names declared in `cols` using the `names` argument. Additionally, a tst file is space separated, make sure you pass ` sep=' '` to the function.

# In[7]:


# Run this code:

cols = ['time', 'rad_flow', 'fpv_close', 'fpv_open', 'high', 'bypass', 'bpv_close', 'bpv_open', 'class','']
tst_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/shuttle/shuttle.tst'


# In[8]:


# Your code here:
shuttle=pd.read_csv(tst_url, sep=' ', index_col=False)
shuttle.columns=cols


# Let's verify that this worked by looking at the `head()` function.

# In[9]:


# Your code here:
print (shuttle.head())


# To make life easier for us, let's turn this dataframe into a comma separated file by saving it using the `to_csv()` function. Save `shuttle` into the file `shuttle.csv` and ensure the file is comma separated and that we are not saving the index column.

# In[10]:


# Your code here:
shuttle.to_csv('shuttle.csv', index=False)


# # Challenge 3 - Working with Excel Files
# 
# We can also use pandas to convert excel spreadsheets to dataframes. Let's use the `read_excel()` function. In this case, `astronauts.xls` is in the same folder that contains this notebook. Read this file into a variable called `astronaut`. 
# 
# Note: Make sure to install the `xlrd` library if it is not yet installed.

# In[11]:


# Your code here:
astronaut=pd.read_excel('astronauts.xls', index=False)


# Use the `head()` function to inspect the dataframe.

# In[12]:


# Your code here:
print (astronaut.head())


# Use the `value_counts()` function to find the most popular undergraduate major among all astronauts.

# In[13]:


# Your code here:
astronaut['Undergraduate Major'].value_counts()


# Due to all the commas present in the cells of this file, let's save it as a tab separated csv file. In the cell below, save `astronaut` as a tab separated file using the `to_csv` function. Call the file `astronaut.csv` and remember to remove the index column.

# In[14]:


# Your code here:
astronaut.to_csv('astronaut.csv')


# # Bonus Challenge - Fertility Dataset
# 
# Visit the following [URL](https://archive.ics.uci.edu/ml/datasets/Fertility) and retrieve the dataset as well as the column headers. Determine the correct separator and read the file into a variable called `fertility`. Examine the dataframe using the `head()` function.

# In[17]:


# Your code here:
fertility=pd.read_csv('fertility_Diagnosis.txt', sep=',', index_col=False)
cols_fert=['Season', 'Age', 'Childish', 'Accident', 'Surgical', 'High fevers', 'Frequency of alcohol consumption', 'Smoking habit', 'Number of hours spent sitting per day', 'Output']
fertility.columns=cols_fert
print (fertility.head())


# In[ ]:




