# QUESTÃO 04

m1 = float(input('Quantas moedas de 1 Real você tem ? '))
m50 = float(input('Quantas moedas de 50 centavos você tem ? '))
m25 = float(input('Quantas moedas de 25 centavos você tem ? '))
total = (m1 * 1) + (m25 * 0.25) + (m50 * 0.5) 

print(f'Você possui um total de R$ {total:.2f}.')