preco = float(input('Digite o valor do produto: R$ '))
print ('-==-'*12)
print (' Digite 1 - Pagamento a Vista dinheiro ou cheque\n Digite 2 - Pagamento à Vista no cartão\n Digite 3 - Pagamento em até 2x no cartão\n Digite 4 - Pagamento em 3x ou mais no cartão')
print ('-==-'*12)

pgto = (input('Digite a forma de pagamento: '))

if pgto == '1':
    print (f'Pagamento à Vista com desconto de 10%: R${preco*0.9:.2f}')
elif pgto == '2':
    print (f'Pagamento à Vista no cartão com desconto de 5%: R${preco*0.95:.2f}')
elif pgto == '3':
    print (f'Pagamento em até 2x no cartão: R${preco:.2f}')
else:
    print (f'Pagamento em 3x ou mais no cartão: R${preco*1.20:.2f}')