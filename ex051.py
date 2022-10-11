num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
dec = num + (10 - 1) * razao
for c in range (num, dec + razao, razao):
    print (c)