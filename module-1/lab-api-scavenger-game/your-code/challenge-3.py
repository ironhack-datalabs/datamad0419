# enter your code below

# challenge-3.py



import requests
import json



r=requests.get('https://api.github.com/repos/ironhack-datalabs/scavenger/contents/').json()  


			
print (r)
	
