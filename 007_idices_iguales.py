'''
Agrupar elementos de los mismos ín dices significa agrupar elementos de dos o más estructuras de datos de acuerdso con sus índices. 
Para agrupar elementos del mismo índice, inicialmente tendrá dos o más listas dentro de una lista como [[ab],[c,d]]. Para agrupar los elementos de estas de ambas listas, debe crear don nuevas listas donde almacenará los elementos de ambas listas en el indice 0[a,c] e índice 1[b,d]. Ese es el significado de agrupar los elementos dfe los mismos indices.
'''

lista_entrada = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
lista_salida = []
index = 0

for i in range(len(lista_entrada[0])):
    lista_salida.append([])
    for j in range(len(lista_entrada)):
        lista_salida[index].append(lista_entrada[j][index])
    index = index + 1
a, b, c = lista_salida[0], lista_salida[1], lista_salida[2]
print(a, b, c) # [10, 40, 70] [20, 50, 80] [30, 60, 90]