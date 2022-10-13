""" EX060 - FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E
MOSTRE O SEU FATORIAL. """

""" 
k = 1
fat = 1
while k <=10:
    fat = fat * k
    k = k + 1
print (f'fat(10) = {fat}') """

n=int(input('Digite um número: '))
k=n
fat = 1
while k > 0:
    print(f'{k}', end='')
    print(' x ' if k > 1 else ' = ', end='')
    fat = fat * k
    k -= 1
print(f'{fat}')

