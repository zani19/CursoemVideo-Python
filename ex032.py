""" from calendar import isleap

ano = int(input('Digite um ano: '))

if isleap(ano):
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} não é um ano bissexto') """

from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print (f"O ano {ano} é bissexto")
else:
    print (f"O ano {ano} não é bissexto")