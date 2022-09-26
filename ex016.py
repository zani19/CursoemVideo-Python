'''
import math
n = float(input('Digite um número real: '))
num = math.trunc(n)
print (f'O número inteiro de {n} é {num}')
'''
""" import math
n = float(input('Digite um número real: '))
print (f'O número inteiro de {n} é {math.trunc(n)}') """

from math import trunc
n = float(input('Digite um número real: '))
print (f'O número inteiro de {n} é {trunc(n)}')