""" MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM NÚMERO ENTRE 0 E 10.
SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER """

from random import randint
print('ESTOU PENSANDO EM UM NÚMERO ENTRE 0 E 10, CONSEGUE ADIVINHAR???')
comp = randint(0,10)
cont = 0
n=0
while n != comp:
    n=int(input('Em qual número eu pensei? '))
    cont += 1 
    if n == comp:
        print(f'Parabéns!')
    else:
        if n > comp:
            print('O número que pensei é menor!')
        else:
            print('O número que pensei é maior!')       
print(f'Você acertou depois de {cont} tentativas!')

""" 
from random import randint
print ('Bem vindo!')
sorteado = randint (1, 100)
chute = 0
while chute != sorteado:
    chute = int(input ('Chute um número: '))
    if chute == sorteado:
        print ('Você venceu!')
    else:
        if chute > sorteado:
            print ('Alto')
        else:
            print ('Baixo')
print ('Fim do jogo!') """