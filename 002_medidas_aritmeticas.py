'''
media
la media es el valor promedio dfe todos los valores en un conjunto de datos, para calcular el valor medio de un conjunto de datos, primero  necesitamos encontrar la suma de todos los valores y luego dividir la suma de todos los valores por el numero total de valores.
'''
lista = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
media = sum(lista)/len(lista)
print(f'la media es {media}')

'''
Mediana
La mediana es el valor medi entre todos los valores en orden ordenado, aquí necesitamos calcular el valor medio de todos los valores en un conjunto de datos, pero antes de calcular la media necesitamos organizar todos los valores en orden ordenado, hay dos formas diferentes de calcular el valor medio:
1 cuando el número total de valores es par: Mediana = [ ( n / 2 )th término + { ( n / 2 ) + 1 }th] / 2
2 cuando el número total de valores es impar: Mediana = { ( n + 1 ) / 2 }thtérmino
'''
lista = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
lista.sort()
if len(lista) % 2 == 0:
    m1 = lista[len(lista)//2]
    m2 = lista[len(lista)//2 - 1]
    mediana = (m1 + m2)/2
else:
    mediana = lista[len(lista)//2]
print(f'La mediana es {mediana}')

'''
moda
La moda es el valor más frecuente entre todos los valores,
'''
lista = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frecuencia = {}
for i in lista:
    frecuencia.setdefault(i,0)
    frecuencia[i] += 1
frecuente = max(frecuencia.values())
for i, j in frecuencia.items():
    if j == frecuente:
        moda = i
print(f'La moda es {moda}')