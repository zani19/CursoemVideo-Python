""" EX059 - CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR

SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.
"""

n1=int(input('Número 1: '))
n2=int(input('Número 2: '))
opt = 0
while opt != 5: 
    opt=int(input("""
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR 

Digite a opção desejada:"""))
    if opt == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opt == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opt == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif opt == 4:
        n1=int(input('Número 1: '))
        n2=int(input('Número 2: '))
print('Obrigado, volte sempre!')