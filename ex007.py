n1 = float(input('Insira a primeira nota do aluno:' ' '))
n2 = float(input('Insira a segunda nota do aluno:' ' '))
m = (n1 + n2) / 2

if m < 5:
    print(f'O aluno foi reprovado. A nota mínima é 5, e no momento ela vale {m:.2f}')
elif m > 5:
    print(f'O aluno foi aprovado! A nota mínima é 5, e no momento ela vale {m:.2f}')
else:
    print(f'O aluno foi aprovado com nota mínima de 5.')

