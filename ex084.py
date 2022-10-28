""" 
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
lista = []
principal = []
maior = menor = 0
while True:
    lista.append(str(input('Nome: ').capitalize()))
    lista.append(float(input('Digite um peso: ')))
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()
    cont = str(input('Deseja continuar? [S/N] '))
    while cont not in 'SsNn':
        cont = str(input('Opção Inválida! Deseja continuar? [S/N] '))
    if cont in 'Nn':
        break
print(f'Foram cadastradas {len(principal)} pessoas!')
print(f'O menor peso foi de {menor} kg, peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]')
print(f'O maior peso foi de {maior} kg, peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]')
