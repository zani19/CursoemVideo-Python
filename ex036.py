casa = float(input('Digite o valor da casa R$ '))
salario = float(input('Digite o seu salário R$ '))
anos = int(input('Digite em quantos anos vai pagar: '))

meses = anos * 12
prestacao = casa / meses
print (f'Valor minimo necessário para realizar o empréstimo: {(salario*0.30):.2f}')
print (f'Valor das prestações: R$ {prestacao:.2f}')
if prestacao >= (salario* 0.30):
    print('Não é possível fazer o empréstimo!')
else:
    print('Parabéns, você pode realizar o empréstimo!')