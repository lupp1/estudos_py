from math import sqrt, pow
c1 = float(input('Digite o valor de um cateto: '))
c2 = float(input('Digite o valor do outro cateto: '))
print(f'O valor da hipotenusa é {sqrt((pow(c1, 2) + pow(c2, 2)))}')
