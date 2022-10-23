"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:           
A) Quantos números foram digitados.      
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
c=0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    c +=1
    cont = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    while cont not in 'SN':
        print('Opção inválida!')
        cont = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    if cont in 'Nn':
        break
print(f'Foram digitados {c} números!')
if 5 in lista:
    print(f'O número 5 foi adicionado a lista')
else:
    print('O número 5 não foi digitado e não está na lista!')
lista.sort(reverse=True)
print(f' Os valores em ordem descrescente são: {lista}')

