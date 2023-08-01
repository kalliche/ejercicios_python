from difflib import SequenceMatcher

text1 = 'Mi nombre es Gabriel Marquez'
text2 = 'Hola, Mi nombre es Gabriel Marquez'

sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f'los textos son {sequenceScore * 100}% similar')

text3 = 'Mi nombre es Gabriel Marquez'
text4 = 'Gabriel Marquez escritor Colombiano ya fallecido'

sequenceScore = SequenceMatcher(None, text3, text4).ratio()
print(f'Los textos son {sequenceScore * 100}% similar')

