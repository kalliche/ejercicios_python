'''
Auxtenticacion de contraseña usando Python
para crear un sistema de autentificacion de contraseña con Python, debe seguir los pasos mencionados a continuación
    1 crear un diccionario de nombre de usuario con sus contraseñas
    2 Luego debe solicitar la entrada del usuario como nombre de usuario utilizando la funcion de entrada en Python
    3 Luego debe usar el módulo getpass en Python para solicitar la entrada del usuario como contraseña, aqui estamos usando el módulo de getpass en lugar de la función de entrada para aseguranos de que el usuario no pueda ver lo que escribe en el campo de contraseña
'''
import getpass

database = {'user1':'123456', 'user2':'654321'}
username = input('ingrese su usuario >> ')
password = getpass.getpass('Ingrese su contraseña >> ')
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass('Ingrese nuevamente su contraseñá >> ')
        break
print('verificada')