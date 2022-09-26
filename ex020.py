import random
alunos = []
k = 0
while k<=3:
    alunos.append(str(input('Nome do aluno: ')))
    k = k + 1
print (f'A ordem das apresentações será: {random.sample(alunos,len(alunos))}')
