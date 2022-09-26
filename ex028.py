from random import randint
from time import sleep

computador = randint (0,5)
print('-=-' * 20)
print ('Vou pensar em um número entre 0 e 5. TENTE ADIVINHAR!!!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print ('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print ('PARABÉNS, VOCÊ GANHOU!')
else:
    print (f'VOCÊ PERDEU! O número escohido foi {computador} e não o {jogador}')