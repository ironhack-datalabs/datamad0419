import argparse
import os
from main import ejecutar

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate a Metacritic report')
  parser.add_argument('-f', dest='filePath',
                    default= None,
                    help='.csv de Metacritic a analizar.')
  
  args = parser.parse_args()

  if isinstance(args.filePath, str):
    print(args.filePath)
    ejecutar(os.path.normpath(args.filePath))
  else:
    print('Hay que especificar un argumento -f con la ruta al fichero .csv')