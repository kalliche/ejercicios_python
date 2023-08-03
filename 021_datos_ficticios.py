'''Si estas aprendiendo ciencia de datos y le resulta dificil crear un conjunto de datos para practicar desde cero, puede descargar un conjunto de datos de "Kaggle" o crear datos falsos
pip3 install faker
pip3 install matplotlib
pip3 install pandas2'''

from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 

'''Cada vez que se ejecute el código, obtendrá resultados diferentes. Ahora crear un conjunto de datos'''
fake = Faker()
data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)
print(data.head())

# exportar el DataFrame a un archivo CSV
data.to_csv('data_faker.csv', index=False)
print('CSV exportado correctamente')

# print(fake.name())
# print(fake.address())
# print(fake.text())

# ggenerar graficas de la información obtenida
# cargar datos de csv 
data = pd.read_csv('./data_faker.csv')

# contar la cantida de perfiles generados por Fker por genero
gender_counts = data['sex'].value_counts()

# crear la grafica de barras
plt.bar(gender_counts.index, gender_counts.values)

# agregar titulos y etiqyuetas a los ejes
plt.title('Cantidad de perfiles Generados por Genero')
plt.xlabel('genero')
plt.ylabel('cantidad')

# mostrar grafica
plt.show()






