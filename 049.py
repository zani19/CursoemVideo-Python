n = int(input('Digite a tabuada do: '))
print ('-='*10)
print (f'Taboada do {n}')

for c in range (1, 11):
    tab = n * c
    print (f'{n} x {c} = {tab}')
print ('-='*10)