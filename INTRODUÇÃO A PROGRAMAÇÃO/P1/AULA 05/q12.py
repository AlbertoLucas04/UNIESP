# QUESTÃO 12

at_e = float(input('Insira o ataque da sua espada: '))
dur_e = float(input('Insira a durabilidade da sua espada: '))

at_a = float(input('Insira o ataque do seu arco: '))
dur_a = float(input('Insira a durabilidade do seu arco: '))

at_l = float(input('Insira o ataque da sua lança: '))
dur_l = float(input('Insira a durabilidade da sua lança: '))

if at_e > 50 and dur_e > 70:
    print('Você deve escolher a Espada!')
elif at_a > 50 and dur_a > 70:
    print('Você deve escolher o Arco!')
elif at_l > 50 and dur_l > 70:
    print('Você deve escolher a Lança!')   
else:   
    print('Você deve trocar suas armas!')

