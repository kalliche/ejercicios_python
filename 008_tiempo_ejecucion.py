'''
Es importante calcular el tiempo de ejecución cuando se trabaja en un proyecto grande, Cuando trabajamos en un gran proyecto, tenemos varios enfoques en mente, El mejor debería ser el que tome el menor tiempo de ejecuacion en total de escenarios. 
Entonces, para calcular el tiempo de ejecuacion de un programa python debemos seguir los pasos mensionados a continuación.
    1 Primero, almacene el tiempode inicnio del programa en una variable.
    2 Escribe el progrtama Python
    3 Almacene la hora de finalizacion del programa en una variable
    4 reste el tioempo de inicio del programa desde el momento final del programa.
Al final obtendra el tiempo de ejecución de su programa en segundos
'''

from time import time
start = time()

# Python el programa de ejecución
word = 'Artificial Intelligence'
text = word.split()
a = ' '
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print(f'Tiempo de ejecución fue de: >> {execution_time}')