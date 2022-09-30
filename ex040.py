n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))

media = (n1+n2)/2

if media < 5.0:
    print (f'Sua média é {media:.1f} e você está REPROVADO!')
elif media >= 7.0:
    print (f'Sua média é {media:.1f} e você está APROVADO!')
else:
    print (f'Sua média é {media:.1f} e você está de RECUPERAÇÃO!') 