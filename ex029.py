velocidade = float(input('Digite sua velocidade: '))
if velocidade > 80:
     print ('MULTADO! Você excedeu o limite permitido que é 80km/h!')
     multa = (velocidade - 80)*7
     print (f'Você foi multado em R${multa:.2f}')
else:
    print ('Siga em frente, olhe para o lado!')