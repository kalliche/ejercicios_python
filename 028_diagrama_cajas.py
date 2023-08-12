'''Un diagrama de caja es estadístico, visualización de datos técnica para analizar la distribución y patrones de puntos de datos numéricos de un conjunto de datos. representa los puntos de datos cuartil 1, cuartil 3, mediano, maximo y minimo de una caracteristica  que ayuda a comprender la distribución de los valores numéricos de un conjunto de datos.

Diagramas de cajas
La porción de caja de un diagrama de caja contienen tres lineas:

(1)-- La primeria linea en la superior representa el cuartil 3 de los pontos de datos, lo que significa que el 75% de los datos debajo de ese punto.

(2)-- La segunda linea en el medio representa el valor medio de los puntos de datos, lo que significa el 50% de los datos se encuentra debajo de es este punto

(3)-- La tercera linea en el diagrama de cuadros representa el cuartil 1 de los puntos de datos, lo que significa que el 25% de los datos se encuentra debajo de este punto.

(4)-- las dos lineas horizontales debajo y encima del cuadro se conocen como lineas de bigote, el bigote, el bigote anterior representa el valor máximo y el bigote inferior representa el valor minimo'''

import pandas as pd
import plotly.express as px

# data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
data = pd.read_csv('./advertising.csv')
print(data.head())

fig = px.box(data, y='TV')
fig.show()


