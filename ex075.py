num = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os números {num}')

if num.count(9) == 0:
    print('Você não digitou o numéro 9!')
else:
    print(f'O valor 9 apareceu {num.count(9)} vezes')

if num.count(3) == 0:
    print('Você não digitou o numéro 3!')
else:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')

print('Os números pares digitados foram: ',end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')