'''
Contar el número de palabras en un acolumna usando Python
La mayoria de los profecionales de ciencia de datos usan el pandas biblioteca para manejo y preparación de datos. La bliblioteca de pandas bno tiene ningún método para contar el número de palabras en un texto, Una forma de resolver este problema es encontrar la longitud dfel texto completo.
'''

import pandas as pd 
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv", encoding = 'latin1')
print(data.head())

''' El conjunto de datos tiene dos columnas Articulo y título, creamos una nueva columna como el número de palabras en la columna del articulo'''

data['numeros de palabras'] = data['Article'].apply(lambda n: len(n.split()))
print(data.head())