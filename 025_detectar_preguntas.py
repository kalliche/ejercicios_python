'''Dectetar preguntas significa identificar si una oración es interrogativa o no. También podemos usar el aprendizaje automatico para detectar preguntas, pero como todos sabemos en tipo de oraciones que vemos en una oracion interrogativa'''
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

question_words = ['what', 'why', 'when', 'where', 'name', 'is', 'how', 'do', 'does', 'which', 'are', 'could', 'would', 'should', 'has', 'have', 'whom', 'whose', 'do not']

question = input('Input a sentence: ')  #Do you have any feelings for me?
question = question.lower()
question = word_tokenize(question)

if any(x in question[0] for x in question_words):
    print('This es a question!!')
else:
    print('This is not a question!')

