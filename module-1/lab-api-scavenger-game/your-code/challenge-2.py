# enter your code below

# challenge-2.py



import requests
import json


# 2.1

r=requests.get('https://api.github.com/repos/ironhack-datalabs/datamad0419/commits?since=2019-04-17T00:00:00Z').json()  # commits



# 2.2

print (len(r))
			

	
