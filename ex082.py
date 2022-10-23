""" 
Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    cont = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    while cont not in 'SN':
        cont = str(input('Opção inválida! Digite (S) para continuar ou (N) para sair:')).upper()[0].strip()
    if cont in 'Nn':
        break
print(f'A lista é: {lista}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números impares é: {impares}')
