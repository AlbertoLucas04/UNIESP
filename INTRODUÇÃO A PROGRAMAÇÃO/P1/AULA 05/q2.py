# QUESTÃO 02

ouro = float(input('Insira a quantidade de Ouro (Kg): '))
prata = float(input('Insira a quantidade de Prata (Kg): '))
total_liga_met = ouro + prata 
prata_armad = (prata / total_liga_met) * 100

if prata_armad >= 70:
    print('Parabéns, vamos fazer a armadura!')
else: 
    print('Não vamos conseguir fazer a armadura.')

 