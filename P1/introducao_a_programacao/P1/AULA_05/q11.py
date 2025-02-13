# QUESTÃO 11

p1_c1 = int(input('Digite a Pontuação do 1° Candidato na 01ª Prova: : '))
p2_c1 = int(input('Digite a Pontuação do 1° Candidato na 02ª Prova: : '))

p1_c2 = int(input('Digite a Pontuação do 2° Candidato na 01ª Prova: : '))
p2_c2 = int(input('Digite a Pontuação do 2° Candidato na 02ª Prova: : '))

p1_c3 = int(input('Digite a Pontuação do 3° Candidato na 01ª Prova: : '))
p2_c3 = int(input('Digite a Pontuação do 3° Candidato na 02ª Prova: : '))

med_1 = (p1_c1 + p2_c1) / 2
med_2 = (p1_c2 + p2_c2) / 2 
med_3 = (p1_c3 + p2_c3) / 2


if med_1 > med_2 and med_1 > med_3:
    print(f'O 1º Candidato é o Vencedor, com pontuação {med_1}!')
elif med_2 > med_1 and med_2 > med_3:
    print(f'O 2º Candidato é o Vencedor, com pontuação de {med_2}')
elif med_3 > med_2 and med_3 > med_1:
    print(f'O 3º Candidato é o Vencedor, com pontuação de {med_3}')
elif med_1 == med_2 and med_1 == med_3:
    print('Há um empate!')