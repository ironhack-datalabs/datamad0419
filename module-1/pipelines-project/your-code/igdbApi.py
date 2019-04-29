import json
import requests
import os
import pandas as pd

def igdbApi():
  #ENTER YOUR KEY HERE
  key = "358b26818240ae6fecc8ba34dd037843"
  url = 'https://api-v3.igdb.com/games'
  body= 'fields name,popularity; sort popularity desc;'
  #RETRIEVE ONE GAME
  response = requests.post(
    url,
    data= body,
    headers={'user-key': key,
              'Content-Type': 'application/json; charset=UTF-8'
            }
    )

  result = response.json()
  top10hyped_df = pd.DataFrame(result)
  return top10hyped_df