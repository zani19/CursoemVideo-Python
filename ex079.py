""" 
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lista = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in lista:
        lista.append(n)
    else:
        print(f'O valor {n} já está na lista!')
    cont = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    while cont not in 'SN':
        print('Opção inválida!')
        cont = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    if cont in 'Nn':
        break
print(f'Você digitou os números {sorted(lista)}')