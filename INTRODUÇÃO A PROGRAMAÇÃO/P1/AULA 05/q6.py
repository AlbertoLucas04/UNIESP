#  QUESTÃO 06 

tempo_dragao01 = float(input('Insira o tempo do 01º Dragão (S): '))
dist_dragao01 = float(input('Insira a distãncia do 01º Dragão (M): '))

tempo_dragao02 = float(input('Insira o tempo do 02º Dragão (S): '))
dist_dragao02 = float(input('Insira a distãncia do 02º Dragão (M): '))

vel_d1 = dist_dragao01 / tempo_dragao01
vel_d2 = dist_dragao02 / tempo_dragao02

if vel_d1 > vel_d2:
    print('O 02º Dragão é o vencedor!')
elif vel_d1 < vel_d2:
    print('O 01º Dragão é o vencedor!')
else:
    print('Ambos finalizaram ao mesmo tempo!')