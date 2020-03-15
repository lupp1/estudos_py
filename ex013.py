salario = float(input('Qual o salário do funcionário? R$'))
r = float(input('Digite o valor do reajuste: '))
aj = salario * r/100
print(f'O novo salário do funcionário, com reajuste de {r:.2f}% é de R${salario + aj:.2f}')