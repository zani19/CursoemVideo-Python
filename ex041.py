import datetime
x = datetime.datetime.now()
ano = (x.year)

print ('-=-'*20)
print ('CONFEDERAÇÃO NACIONAL DE NATAÇÃO!')
print ('-=-'*20)

dn = int(input('Digite seu ano de nascimento: '))
categoria = (ano - dn)

if categoria <= 9:
    print(f'Você tem {categoria} anos e é da categoria MIRIM!')
elif categoria <= 14:
    print (f'Você tem {categoria} anos e é da gategoria INFANTIL!')
elif categoria <= 19:
    print (f'Você tem {categoria} anos e é da catergoria JUNIOR!')
elif categoria <= 20:
    print (f'Você tem {categoria} anos e é da catergoria SÊNIOR!')
else:
    print (f'Você tem {categoria} anos e é da categoria MASTER!')