""" 
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[[], [], []], [[], [], []], [[], [], []]]
somaterceira = somapar = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if c == 2:
            somaterceira += matriz[l][2]    
        if c == 0:
            maior = matriz [1][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]    
    print()
print(f'A soma de todos os valores pares digitados é {somapar}')
print(f'A soma dos valores da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é {maior}')