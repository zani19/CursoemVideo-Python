soma = caro = menor = cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do Produto: ')).upper().strip()
    preço = float(input('Digite o preço do Produto: R$ '))
    soma += preço
    cont +=1
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    continuar = ' '
    
print(f'Total gasto: R$ {soma:.2f}\n{caro} produtos custaram mais de R$1000\nO produto mais barato foi {barato.upper()} e custou R$ {menor:.2f}')
