primeiro = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
k = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while k <=total:
        print(f'{termo} ->', end='')
        k += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados!')