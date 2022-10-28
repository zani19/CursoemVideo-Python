""" 
Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import sample
print('-='*40)
print(f'{"PALPITE MEGA-SENA":^80}')
print('-='*40)
n = int(input('Digite o número de jogos: '))
k = 1
while k <= n:
    v = sample(range(1,60), 6)
    print(f'{sorted(v)}')
    k +=1

""" k = 1
while k <= n:
    print(k)
    k += 1


import random
v = random.sample(range(50,70), 100)
v
range (50, 70) """