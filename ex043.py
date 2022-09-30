peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso/(altura**2)

if IMC < 18.5:
    print (f'Você tem {altura:.2f} metros e pesa {peso:.2f} kg. Seu IMC é {IMC:.0f} e você está abaixo do peso!')
elif 18.5 <= IMC < 25:
    print (f'Você tem {altura:.2f} metros e pesa {peso:.2f} kg. Seu IMC é {IMC:.0f} e você está com o peso ideal')
elif 25 <= IMC < 30:
    print (f'Você tem {altura:.2f} metros e pesa {peso:.2f} kg. Seu IMC é {IMC:.0f} e você está com sobrepeso')
elif 30 <= IMC < 40:
    print (f'Você tem {altura:.2f} metros e pesa {peso:.2f} kg. Seu IMC é {IMC:.0f} e você está com obesidade')
else:
    print (f'Você tem {altura:.2f} metros e pesa {peso:.2f} kg. Seu IMC é {IMC:.0f} e você está com obesidade mórbida')

