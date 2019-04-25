#!/usr/bin/env python
# coding: utf-8

# Now you want to improve your previous solution by removing the stop words from the corpus. The idea is you only want to add terms that are not in the `stop_words` list to the `bag_of_words` array.
# 
# Requirements:
# 
# 1. Move all your previous codes from `main.ipynb` to the cell below.
# 1. Improve your solution by ignoring stop words in `bag_of_words`.
# 
# After you're done, your `bag_of_words` should be:
# 
# ```['ironhack', 'is', 'cool', 'love', 'am', 'student', 'at']```
# 
# And your `term_freq` should be:
# 
# ```[[1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1]]```

# In[8]:


stop_words = ['all', 'six', 'less', 'being', 'indeed', 'over', 'move', 'anyway', 'fifty', 'four', 'not', 'own', 'through', 'yourselves', 'go', 'where', 'mill', 'only', 'find', 'before', 'one', 'whose', 'system', 'how', 'somewhere', 'with', 'thick', 'show', 'had', 'enough', 'should', 'to', 'must', 'whom', 'seeming', 'under', 'ours', 'has', 'might', 'thereafter', 'latterly', 'do', 'them', 'his', 'around', 'than', 'get', 'very', 'de', 'none', 'cannot', 'every', 'whether', 'they', 'front', 'during', 'thus', 'now', 'him', 'nor', 'name', 'several', 'hereafter', 'always', 'who', 'cry', 'whither', 'this', 'someone', 'either', 'each', 'become', 'thereupon', 'sometime', 'side', 'two', 'therein', 'twelve', 'because', 'often', 'ten', 'our', 'eg', 'some', 'back', 'up', 'namely', 'towards', 'are', 'further', 'beyond', 'ourselves', 'yet', 'out', 'even', 'will', 'what', 'still', 'for', 'bottom', 'mine', 'since', 'please', 'forty', 'per', 'its', 'everything', 'behind', 'un', 'above', 'between', 'it', 'neither', 'seemed', 'ever', 'across', 'she', 'somehow', 'be', 'we', 'full', 'never', 'sixty', 'however', 'here', 'otherwise', 'were', 'whereupon', 'nowhere', 'although', 'found', 'alone', 're', 'along', 'fifteen', 'by', 'both', 'about', 'last', 'would', 'anything', 'via', 'many', 'could', 'thence', 'put', 'against', 'keep', 'etc', 'amount', 'became', 'ltd', 'hence', 'onto', 'or', 'con', 'among', 'already', 'co', 'afterwards', 'formerly', 'within', 'seems', 'into', 'others', 'while', 'whatever', 'except', 'down', 'hers', 'everyone', 'done', 'least', 'another', 'whoever', 'moreover', 'couldnt', 'throughout', 'anyhow', 'yourself', 'three', 'from', 'her', 'few', 'together', 'top', 'there', 'due', 'been', 'next', 'anyone', 'eleven', 'much', 'call', 'therefore', 'interest', 'then', 'thru', 'themselves', 'hundred', 'was', 'sincere', 'empty', 'more', 'himself', 'elsewhere', 'mostly', 'on', 'fire', 'am', 'becoming', 'hereby', 'amongst', 'else', 'part', 'everywhere', 'too', 'herself', 'former', 'those', 'he', 'me', 'myself', 'made', 'twenty', 'these', 'bill', 'cant', 'us', 'until', 'besides', 'nevertheless', 'below', 'anywhere', 'nine', 'can', 'of', 'your', 'toward', 'my', 'something', 'and', 'whereafter', 'whenever', 'give', 'almost', 'wherever', 'is', 'describe', 'beforehand', 'herein', 'an', 'as', 'itself', 'at', 'have', 'in', 'seem', 'whence', 'ie', 'any', 'fill', 'again', 'hasnt', 'inc', 'thereby', 'thin', 'no', 'perhaps', 'latter', 'meanwhile', 'when', 'detail', 'same', 'wherein', 'beside', 'also', 'that', 'other', 'take', 'which', 'becomes', 'you', 'if', 'nobody', 'see', 'though', 'may', 'after', 'upon', 'most', 'hereupon', 'eight', 'but', 'serious', 'nothing', 'such', 'why', 'a', 'off', 'whereby', 'third', 'i', 'whole', 'noone', 'sometimes', 'well', 'amoungst', 'yours', 'their', 'rather', 'without', 'so', 'five', 'the', 'first', 'whereas', 'once']

# Write your code below
corpus = []
docs = ['doc1.txt', 'doc2.txt', 'doc3.txt']

for doc in docs:
    with open(doc, 'r') as f:
        corpus.append(f.read())

corpus=[corpus[i].lower() for i in range(len(corpus))]
corpus=[corpus[i].replace('.', '') for i in range(len(corpus))]


bag_of_words = []
for e in corpus:
    f=e.split(' ')
    for g in f:
        if g not in bag_of_words and g not in stop_words : bag_of_words.append(g)  # aqui se quita stop_words

            
term_freq = []
for e in corpus:
    lista=[]
    e=e.split()
    for f in bag_of_words:
        if f in e:
            lista.append(1)
        else:
            lista.append(0)
    term_freq.append(lista)   
    
print ('is' in stop_words)    # el resultado sale diferente del esperado, estas palabras estan en stop_words
print ('am' in stop_words) 
print ('at' in stop_words) 

print (bag_of_words)
print (term_freq)


# In[ ]:




