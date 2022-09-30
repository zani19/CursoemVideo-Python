from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(""" Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA """)
player = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-='*15)
print (f'O computador escolheu {(itens[computador])}')
print (f'O Jogador escolheu {(itens[player])} ')
print('-='*15)

if computador == 0:
    if player == 0:
        print ('EMPATE!')
    elif player == 1:
        print ('Jogador VENCEU!')
    elif player == 2:
        print ('Computador VENCEU!')    
    else:
        print ('JOGADA INVÁLIDA!')

elif computador == 1:
    if player == 0:
        print ('Computador VENCEU!')
    elif player == 1:
        print ('EMPATE!')    
    elif player == 2:
        print ('Jogador VENCEU!')
    else:
        print ('JOGADA INVÁLIDA!')

elif computador == 2:
    if player == 0:
        print ('Jogador VENCEU!')
    elif player == 1:
        print ('Computador VENCEU!')
    elif player == 2:
        print ('EMPATE!')
    else:
        print ('JOGADA INVÁLIDA!')