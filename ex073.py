brasileiro = ('Palmeiras', 'Internacional','Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR ','Atlético-MG' , 'América-MG ', 'Fortaleza', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')

print('-='*30)
print('{:^60}'.format("BRASILEIRÃO - 2022"))
print('-='*30)

print('-='*30)
print('{:^60}'.format("PRIMEIROS COLOCADOS"))
print('-='*30)

print(brasileiro[0:5])

print('-='*30)
print('{:^60}'.format("ÚLTIMOS COLOCADOS"))
print('-='*30)

print(brasileiro[-4:])

print('-='*30)
print('{:^60}'.format("TIMES EM ORDEM ALFABÉTICA"))
print('-='*30)
print(sorted(brasileiro))

print('-='*30)
print('{:^60}'.format("Posição -  São Paulo"))
print('-='*30)
print(f'(O São Paulo se encontra na {brasileiro.index("São Paulo")+1}ª posição!')