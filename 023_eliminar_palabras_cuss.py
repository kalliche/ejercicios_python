'''Cuss words son palabras que hacen que su lenguaje suene muy descort€s, grosero y culturalmente ofensivo. A veces necesitamos identificar y eliminar palabras maliciosas.
pip3 install better_profanity'''

from better_profanity import profanity

text = 'Please leave me alone or get the fuck out'
censored = profanity.censor(text)
print(censored)