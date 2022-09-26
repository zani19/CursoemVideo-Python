import math

catadj = float(input('Digite o valor do cateto adjacente: '))
catopost = float(input('Digite o valor do cateto oposto: '))
print (f' Cateto Adjacente: {catadj}\n Cateto Oposto: {catopost}\n Hipotenusa: {math.hypot(catadj, catopost)}')
