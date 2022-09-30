l1 = int(input('Digite o lado A do triângulo: '))
l2 = int(input('Digite o lado B do triângulo: '))
l3 = int(input('Digite o lado C do triângulo: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível formar um triângulo com essas medidas.')
    if l1 == l2 == l3:
        print('Triângulo EQUILATERO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Triângulo Isósceles')
    else:
        print('Triângulo ESCALENO!')
else:
    print('Não é possível formar um triângulo com essas medidas.')