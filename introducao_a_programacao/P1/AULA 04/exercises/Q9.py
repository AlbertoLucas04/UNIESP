# QUESTÃO 09

msg = str('Olá, seja bem-vindo a sua Avaliação de Desempenho!')
print(msg)

horas_ext = int(input('Digite aqui o número de horas extras realizadas: '))
horas_fal = int(input('Digite aqui o número de horas faltosas: '))
condicao_para_bonus = horas_fal + (horas_fal * 0.5)

if horas_ext > condicao_para_bonus:
    print('Parabéns, você recebeu um bônus de R$ 500,00!')
else:
    print('Você não recebeu nenhum bônus.')