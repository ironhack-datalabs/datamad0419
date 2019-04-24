# enter your code below

# challenge-1.py



import requests
import json


# 1.1

r=requests.get('https://api.github.com/repos/ironhack-datalabs/datamad0419/forks').json()  # forks
#print (type(r))
#print (r)



# 1.2

languages=[value for d in r for key,value in d.items() if key=='language']



# 1.3			

print (list(set(languages)))	

