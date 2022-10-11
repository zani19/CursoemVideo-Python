n = int(input('Digite um número: '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print ('\033[33m', end='')
        tot += 1
    else:
        print ('\033[31m', end='')
    print (f'{c}', end='')
print (f'\n\033[m O número {n} foi divisível {tot} vezes')
if tot == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')