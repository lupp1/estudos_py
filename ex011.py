print('Quantos litros de tinta você precisa para pintar sua parede?')
l = float(input('Largura da parede em metros: '))
a = float(input('Altura da pareade em metros: '))
t = (a * l/2)
print(f'Sua parede tem dimensões de {a:.3f}x{l:.3f} e sua área é de {(a * l):.3f}m²',
      f'Para pintar essa parede, você precisará de {t:.2f}L de tinta.',
      sep='\n')
p = float(input('Quanto custa o seu litro de tinta? R$'))
print(f'O custo para pintar a sua parede será de R${(t * p):.2f}')
