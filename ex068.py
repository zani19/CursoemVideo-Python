from random import randint
v = 0
print('-='*30)
print('VAMOR JOGAR PAR OU IÍMPAR?')
print('-='*30)
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    soma = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolhe PAR ou IMPAR? [P/I] ')).upper()[0].strip()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end ='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break
    print('Vamos jogar novamente...')
print ('FIM DE JOGO!')