# enter your code below

# challenge-3.py



import requests
import json


url='https://api.github.com/repos/ironhack-datalabs/scavenger/contents/'

r=requests.get(url).json()  

#print (r)


names=[value for d in r for key,value in d.items() if key=='name']
			
#print (names)

scaven=[requests.get(url+names[i]).json()[0]['name'] for i in range(1, len(names))\
        if requests.get(url+names[i]).json()[0]['name'].endswith('.scavengerhunt')]

#print (scaven)	

print (requests.get(url+names[1]+scaven[1]))




