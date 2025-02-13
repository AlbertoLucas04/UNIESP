# QUESTÃO 3

frase = input('Insira sua frase: ')
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'

frase = frase.lower()

total_v = 0
total_c = 0
for contador_de_vogais in vogais:
    total_v += frase.count(contador_de_vogais)

for contador_de_consoantes in consoantes:
    total_c += frase.count(contador_de_consoantes)

print(f'Total de Consoantes: {total_c} ')
print(f'Total de Vogais: {total_v} ')





