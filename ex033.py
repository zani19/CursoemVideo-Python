a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c > b:
    menor = c

maior = a
if b > a  and b > c:
    menor = b
if c > a and c > b:
    maior = c

print (f'O menor número é o {menor} e o maior número é o {maior}')