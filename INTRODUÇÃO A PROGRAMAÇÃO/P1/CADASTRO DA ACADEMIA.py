print('Olá, seja bem-vindo! Preencha os dados abaixo:')

#CADASTRO
nome = input('Nome Completo: ')
nasc = input('Data de nascimento: ')
peso = input('Peso (Kg): ')
altura = input('Altura (Cm): ')
lesao = input('Possui alguma lesão ? ')

if f'{lesao}' == "Sim":
    input('Detalhe sobre: ')

fumante = input ('Você fuma ? ')
bebe = input('Você consume bebidas alcólicas ? ')

plano_inicio = print('Qual plano será seu plano ? ')

p1 = str(print('Plano 01 (P1) - 01 Mês - R$ 90,00'))
p2 = str(print('Plano 02 (P2) - 03 Meses - R$ 200,00'))
p3 = str(print('Plano 03 (P3) - 06 Meses - R$ 420,00'))
p4 = str(print('Plano 04 (P4) - 12 Meses - R$ 720,00 '))

plano_fim = input('Plano escolhido: ')

pgto = print('Qual será a forma de pagamento ?')
print('Débito')
print('Crédito')
print('Dinheiro')
print('Pix')

#CONCLUSÃO
print('Agradecemos pelas informações!')
