'''
El modulo SpellChecker en Python  es una de las herramientas más manuales que se pueden usar para corregir palabras de mal escrito en un fragmento  de texto diccionario ingles
'''
from spellchecker import SpellChecker
corrector = SpellChecker()

word = input('Ingrese una palabra: ')
if word in corrector:
    print('correct')
else:
    correct_word = corrector.correction(word)
    print(f'corrector ortografico es >> {correct_word}')
