# QUESTÃO 02

mentorandos = [5,6,7,10,9]

# Cálculo da média

soma = 0

for i in range(len(mentorandos)):
    
    soma += mentorandos[i]
    
media = soma / len(mentorandos)

print(f'Média da Turma: {media}')
