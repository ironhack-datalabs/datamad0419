import json
import requests

a = open(".env", "r")
b = a.read()
print(b)
c = requests.get("https://api.github.com/repos/ironhack-datalabs/datamad0419/forks?client_id=alonsopdani&client_secret={}".format(b))
res = c.json()
print(res)