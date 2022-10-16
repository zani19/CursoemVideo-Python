n = s = k = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    k +=1
    s += n
print(f'Você digitou {k} números e a soma deles é {s}')