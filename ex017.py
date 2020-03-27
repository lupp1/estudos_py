from math import sqrt, pow
catetoOp = float(input('Digite o valor de um cateto: '))
catetoAdj = float(input('Digite o valor do outro cateto: '))
print(f'O valor da hipotenusa é {sqrt((pow(catetoOp, 2) + pow(catetoAdj, 2)))}')
