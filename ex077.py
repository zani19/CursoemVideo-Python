brasileiro = ('Palmeiras', 'Internacional','Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR ','Atletico-MG' , 'America-MG ', 'Fortaleza', 'Botafogo', 'Santos', 'Sao Paulo', 'Bragantino', 'Goias', 'Coritiba', 'Ceara', 'Cuiaba', 'Atletico-GO', 'Avai', 'Juventude')
for p in brasileiro:
    print (f'\nNa palavra {p.upper()} temos as vogais ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')