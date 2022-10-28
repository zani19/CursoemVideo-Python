""" 
Exercício Python 086:
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
""" linha0 = [[], [], []]
linha1 = [[], [], []]
linha2 = [[], [], []]

for c in range(0,3):
    n=int(input(f'Digite um valor para [0, {c}]: '))
    linha0[(c)].append(n)
for c in range(0,3):
    n=int(input(f'Digite um valor para [1, {c}]: '))
    linha1[(c)].append(n)
for c in range(0,3):
    n=int(input(f'Digite um valor para [2, {c}]: '))
    linha2[(c)].append(n)
print(linha0[0], linha0[1], linha0[2])
print(linha1[0], linha1[1], linha1[2])
print(linha2[0], linha2[1], linha2[2]) """

matriz = [[[], [], []], [[], [], []], [[], [], []]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()