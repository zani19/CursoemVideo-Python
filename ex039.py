import datetime
ano = datetime.datetime.now()
x = (ano.year)

dn = int(input('Digite o ano em que você nasceu: '))
idade = x - dn
print (f'Você tem {idade} anos')

if idade == 18:
    print ('Você precisa se alistar!')
elif idade > 18:
    print (f'Você deveria ter se alistado a {idade - 18} anos atrás')
else:
    print (f'Você precisará se alistar daqui a {18 - idade} anos')

