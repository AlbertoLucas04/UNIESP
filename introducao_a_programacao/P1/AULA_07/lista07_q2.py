from time import sleep

p_n = int(input('Insira um número para a Tabuada: '))
print()
print(f'Tabuada do {p_n} ')
for multiplicador in range(1,11):
    print(f'{p_n} x {multiplicador} = {p_n * multiplicador}')
