dist = int(input('Digite a distância da viagem: '))
if dist < 200:
    print (f'O valor da viagem é de R$ {(dist*0.50):.2f}')
else:
    print (f'O valor da viagem é de R$ {(dist*0.45):.2f}')