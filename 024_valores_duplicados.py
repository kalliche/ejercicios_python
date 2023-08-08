'''Encontrar valores duplicatos de una matriz o cualquier otra escultura de datos ues una de las preguntas populares de la entrevista de codificacion que puede obtener en cualquier entrevista de codificacion, el lenguaje de progeramacion python proporciona muchas funciones integradas para encontrar los valores duplicados.

deffinir€ una funcion de python que tomara un alista de valores en cualquier tipo de datos, a continuacion se muestra la funcion para encontrar valores duplicados en una lista.'''

def find_duplicates(x):
    length = len(x)
    duplicates = []
    for i in range(length):
        n = i + 1
        for a in range(n, length):
            if x[i] == x[a] and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates

names = ['Pedro', 'Simon', 'Jose', 'Maria', 'Pedro', 'Pedro', 'Maria']
print(find_duplicates(names))
