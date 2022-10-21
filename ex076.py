listagem = ('Lápis', 1.75, 'Borracha', 0.50, 'Caneta', 3.0, 'Fita adesiva', 4.0, 'Estojo', 30.00, 'Mochila', 79.90)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)