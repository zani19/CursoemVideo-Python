"""
soma = 0 #zero é o elemento neutro para a soma
x=1
while x<=3:
    n = int(input('Digite o número:'))
    soma = soma + n
    x = x+1
print (soma) """


n = soma = cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Quantidade de números digitados: {cont}\nSoma dos números digitados: {soma}')