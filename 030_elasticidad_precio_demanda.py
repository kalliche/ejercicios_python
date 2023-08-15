'''El precio es uno de los factores más importantes que influye en una demanda de un producto, la estalidad se refiere al grado de respuesta, y la estalistida precio de la demanda se refiere al grado de capacidad de respuesta de la demanda de un producto debido al cambio en su precio. 

La estalicidad precio de la demanda se refiere al grado de capacidad de respuesta de la demanda de un producto o un cambio en el precio. En pocas palabras, significa el grado en que la demanda de un producto cambia con un aumento o disminución en su precio. Por ejemplo, la demanda de un producto aumenta un 20% debido a una disminuciuón del 10% en su precio. Esto es lo que significa cambiar la demanda con el cambio en el precio de un producto, y cuando calcula el grado en que cambia la demanda, se llama elasticidad precio de la demanda.

formula (porcentaje de cambio en la cantidad demandada / porcentaje de cambio en el precio)
'''

# comenzare la tarea de calcular la elasticidad precio de la demanda utilizando python creando conjunto de datos que debe contener datos sobre el cambio en el precio y la demanda de un producto

import pandas as pd

data = pd.DataFrame({'Demand': [20, 30, 31, 33, 30, 33, 35],'Price': [2000, 1800, 1850, 1700, 1800, 1700, 1600]})
print(data)

# las primeras filas de este conjunto de datos contiene la demanda inicial y precio, para un producto, y las filas posteriores contienen el cambio en la demanda y el cambio en el precio del producto, Ahora nuestro próximo paso es agregar dos columnas más como el cambio porcentual en la demanda y porcentaje  de cambio en el precio

data['% Change in demand'] = data['Demand'].pct_change()
data['% Change in Price'] = data['Price'].pct_change()
print(data)

# Ahora el ultimo paso es calcular la eslasticidad precio de la demanda (% cambio en la demanda / % cambio de precio) agregando una nueva columna a estos datos. A continuación se muestra cómo puede calcularlo usando python

data['Price Elasticity'] = data['% Change in demand'] / data['% Change in Price']
print(data)