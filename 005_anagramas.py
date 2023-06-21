'''
Anagramas son palabras formadas reorganizando las letras de otra palabra, por ejemplo, ccche y arco, gato y acto, etc. grupar anagramas es una de las preguntas populares en la codificación de entrevistas.
dada las palabras el script agrupa las que tenfan las mismas letras pero sean diferentes palabras
'''
from collections import defaultdict

def group_anagramas(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = ' '.join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

words = ['tea', 'eat', 'bat', 'ate', 'arc', 'car']
print(group_anagramas(words))
# dict_values([['tea', 'eat', 'ate'], ['bat'], ['arc', 'car']])