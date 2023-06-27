'''Para crear y reproducir piedra papel y tijera, usare las declaraciones de if y elif en Python, Prepararé este juego para jugar entre dos jugadores, player-1 será el usuario y player-2 sera la computadora. El juigador uno seleccionará manualmente el papel de roca o la tijera, mientras que el jugador dos eligira asl azar, asi que tambien usaré el módulo aleatorio en Python para crear este juego.'''

import random

player1 = input('seleccione piedra, papel o tijera >> ').lower()
player2 = random.choice(['piedra', 'papel', 'tijera']).lower()
print(f'El jugador 2 selecciono >> {player2}')

if player1 == 'piedra' and player2 == 'papel':
    print('player2 2 gana')
elif player1 == 'papel' and player2 == 'tijera':
    print('player 2 gana')
elif player1 == 'tijeras' and player2 == 'piedra':
    print('player 2 gana')
elif player1 == player2:
    print('empate')
else:
    print('player 1 gana')