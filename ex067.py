n=0
while True:
    n = int(input('Você gostaria de ver a tabuada de qual número? '))
    tab = 1 
    while tab <= 10:
        print(f'{n:2} x {tab:2} = {n*tab:2}')
        tab += 1
    if n < 0:
        break
print('FIM DA TABUADA!')