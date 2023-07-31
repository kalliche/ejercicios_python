'''
Age calculator es una aplicacion increible para crear como principiante en cualquier lenguaje de programación, para la calculadora de edad, se necesitan dos fechas:
    1 fecha de hoy
    2 fecha de nacimeinto
Puedes solicitar al usuario ambas fechas o simplemente solicitar l;a fecha de nacimiento y usar la fecha de hoy en la computadora.
'''

def calcular_edad(y, m, d):
    import datetime
    hoy = datetime.datetime.now().date()
    fecha_nacimiento = datetime.date(y, m, d)
    edad = int((hoy - fecha_nacimiento).days / 365.25)
    print(edad)
calcular_edad(1986, 10, 31)