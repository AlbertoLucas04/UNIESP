# QUESTÃO 05

agua = float(input('Insira a Quantidade de Água (L): '))
dist = float(input('Insira a Distância para o Oásis (Km): '))

agua_nec = dist * 2

if agua >= agua_nec:
    print('A quantidade de água é suficiente!')
else:
    print('A quantidade de água é insuficiente!')