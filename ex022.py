
""" nome = str(input('Digite seu nome: ')).strip()
count_nome = nome.replace(' ','')
dividido = nome.split()

print (f'Seu nome com letras maiúsculas: {nome.upper()}')
print (f'Seu nome com letras minúsculas: {nome.lower()}')
print (f'Seu nome possui {len(count_nome)} letras')
print (f'Seu primeiro nome possui {dividido[0]}') """

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print (f'Seu nome com letras maiúsculas: {nome.upper()}')
print (f'Seu nome com letras minúsculas: {nome.lower()}')
print (f'Seu nome possui {len(nome) - nome.count(" ")} letras')
print (f'Seu primeiro nome possui {dividido[0]}')