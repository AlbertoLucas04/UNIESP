#  QUESTÃO 07

planta = float(input('Insira o tamanho da palnta (m): '))

if planta < 1:
    print('A planta é pequena!')
elif planta >= 1 and planta <= 3:
    print('A planta é média!')
else:
    print('A planta é grande!')