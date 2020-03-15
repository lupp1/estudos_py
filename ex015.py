dias = int(input('Por quantos dias o carro será alugado? '))
km = float(input('Quantos quilômetros irá rodar? '))
d = (60 * dias) + (0.15 * km)
print(f'O total a ser pago pelo aluguel será de R${d:.2f}')

