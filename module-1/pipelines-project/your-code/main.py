import pandas as pd
from functions import *

'''
usar filter, map, reduce
funciones en otro fichero
'''

data = pd.read_csv('your-code/earthquake.csv')
# print(data.head())
print(data.shape)
print(data.columns)

# eliminar duplicados
before = len(data)
data = data.drop_duplicates()
after = len(data)
print('Number of duplicate records dropped: ', str(before - after))


# comprobamos si hay algún id duplicado
print(functions.column_duplicates(data, data["id"], data["date"]))
