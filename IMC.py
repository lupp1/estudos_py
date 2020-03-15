print('>>>Faça o cálculo do seu IMC!')
peso = float(input('Insira o seu peso atual:' ' '))
altura = float(input('Insira a sua altura em metros:' ' '))
imc = peso / altura ** 2
print(f'O seu IMC é igual a: {imc:.2f}')

if imc < 18.5:
    print('O seu IMC está abaixo de 18.5. Você está com Magreza.')
elif 18.5 < imc < 24.9:
    print('O seu IMC está entre 18.5 e 24.9. Você está com um IMC Normal.')
elif 25.0 < imc < 29.9:
    print('O seu IMC está entre 25.0 e 29.9. Você está com Sobrepeso.')
elif 30.0 < imc < 39.9:
    print('O seu IMC está entre 30.0 e 39.9.Você está com Obesidade.')
elif imc > 40.0:
    print('O seu IMC é maior que 40.0. Você está com Obesidade Grave!')
