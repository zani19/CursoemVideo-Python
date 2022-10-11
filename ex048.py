soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma += c
        """ soma = soma + c """
print (f'Foram encontrados {cont} números!')
print (f'A soma de todos os números multiplos de 3 é {soma}')
