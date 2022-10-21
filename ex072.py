from msvcrt import kbhit


num = ('zero', 'um', 'dois', ' três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    entrada = int(input('Digite um número entre 0 e 20: ')) 
    if 0 <= entrada <= 20:
        print(f'Você digitou o número: {num[entrada].upper()}')
        continuar = ' '
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
        if continuar == 'N':
            break
    else: 
        print('Opção inválida! ',end='')
print(f'Agradecemos sua participação!')
