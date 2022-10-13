""" EX057 - FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA,
MAS SÓ ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA
A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO. """

sexo=str(input('Digite seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo=str(input('Dados INVÁLIDOS! Digite seu sexo [M/F]: ')).upper()[0].strip()
print('Fim!')
