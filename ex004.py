a = input('Digite algo:' ' ')
print(f'O tipo desta variável é: {type(a)}')
print(
    f'É numérico? {a.isnumeric()}',
    f'É apenas espaço? {a.isspace()}',
    f'É alfabético? {a.isalpha()}',
    f'É alfanumérico? {a.isalnum()}',
    f'Está em maiúsculas? {a.isupper()}',
    f'Está em minúsculas? {a.islower()}',
    f'Está capitalizado? {a.istitle()}',
    sep= '\n'
)


