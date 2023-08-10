'''csv los archivos de valores separados por comas, (formato de archivo más utilizado para importar y exportar grandes cvonjuntos de datos, La razon por la cual se prefiere un archivo csv a un archivo axcel ex que un archivo csv consume menos memoria en comparación con un archivo excel.)'''

# escribir un archivo csv
import csv
import pandas as pd

data = {'Name': ['Vegueta', 'Bulma', 'Gohan', 'Goku', 'Picoro'],
        'Age': [23, 21, 25, 23, 22]
        }
data = pd.DataFrame(data)
data.to_csv('age_data.csv', index=False)
print(data.head())

# leer un archivo csv
data = pd.read_csv('age_data.csv')
print(data.head())