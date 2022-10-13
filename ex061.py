""" EX061 - REFAÇA O DESAFIO 051, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA,
MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE """

""" 
num = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
dec = num + (10 - 1) * razao
for c in range (num, dec + razao, razao):
    print (c) """

primeiro = int(input('Primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
k = 1
while k <= 10:
    print(f'{termo} ->', end=' ')
    termo += razao
    k += 1
print ('FIM!')