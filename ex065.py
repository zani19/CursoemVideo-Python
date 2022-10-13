maior = menor = quant = media = soma = 0
sair = 'S'
while sair in 'Ss':
    n = int(input('Digite um número: '))
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n    
    sair=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} números e a média foi {media}\nO maior valor foi {maior} e o menor valor foi {menor}')