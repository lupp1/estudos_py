medida = float(input('Digite uma medida em metros:'' '))

print(f"O valor em milímetros é: {medida * pow(10, 3)}mm",
      f'Em centímetros: {medida * pow(10, 2)}cm',
      f'Em decímetros: {medida * pow(10, 1)}dm',
      f'Em decâmetros: {medida * pow(10, -1)}dam',
      f'Em hectômetros: {medida * pow(10, -2)}hm',
      f'Em quilômetros: {medida * pow(10, -3)}km',
      sep='\n')

