'''
ADIVINAR NUMERO
Para crear un juego de adivinanzas, se crea un programa para seleccionar un número aleatorio entre 1 y 10, Para dar pstas al usuario, podemos usar declaraciones condicionales decirle al usuario si el numero adivinado es menor, mayor o igual que el numero que se selleciono.
'''

import random

n = random.randrange(1,10)
adivinar = int(input('ingrese un numero >> '))
while n != adivinar:
    if adivinar < n:
        print('demasiado bajo')
        adivinar = int(input('Ingrese un nuevo numero >> '))
    elif adivinar > n:
        print('Demasiado alto')
        adivinar = int(input('Ingrese un nuevo numero >> '))
    else:
        break
print('Acertaste !!!!')