print('-='*30)
print('CADASTRO DE PESSOAS')
print('-='*30)
mais18 = homens = menos20 = 0

while True:
    idade = int (input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input('Digite o sexo: [M/F] ')).upper()[0].strip()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    if continuar == 'N':
        break
print(f'Pessoas com mais de 18 anos: {mais18}\nTotal homens cadastrados: {homens}\nTotal mulheres com menos de 20 anos: {menos20}')
