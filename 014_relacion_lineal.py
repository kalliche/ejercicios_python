'''
La relación lineal es un termino estadístico que no es más que la relación entre dos variables. Una relación lineal muestra qué tanbien dos variables x y y estan relacionadas entre si, como profecional de la ciencia de datos.
Puede usar cualquier biblioteca de visualizacion de datos en Python para visualizar una relación lineal, prefiero usar trazador ya que proporciona resultados interactivos. Pero como muchos programadores de Python usan matplotlib para visualización de datos, te mostrare cómo visualizar una relación lineal con Python usando plotly y matplotlib
pip3 install statsmodels
'''
import pandas as pd
import numpy as np
import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib




data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding='latin1')
data = data.dropna()
print(data.head())

'''Visualizar relaciones lineales utilizando la biblioteca plotly'''
figure = px.scatter(data_frame = data, 
                    x="Impressions",
                    y="Likes", 
                    size="Likes", 
                    trendline="ols", 
                    title = "Relationship Between Likes and Impressions")
figure.show()

'''Para visualizar relaciones lineales usando matplotlib se usa el método seaborn.regplot, asi que esta como trazar relaciones lineales mediante el uso de la biblioteca'''
matplotlib.use('TkAgg')
plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("relationship Bewtween Likes y Impressions")
sns.regplot(x = "Impressions",
            y = "Likes",
            data = data)
plt.show()
