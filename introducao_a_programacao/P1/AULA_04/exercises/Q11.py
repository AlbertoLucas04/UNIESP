# QUESTÃO 11

msg = ('Olá, seja bem-vindo(a) ao Cinema. Vamos conhecer nossos valores?')
print(msg)

idade = int(input('Digite sua idade: '))

if idade < 12 or idade > 60:
    print('O ingresso custa R$ 15,00.')
elif idade >= 12 or idade <= 60:
    print('O ingresso custa R$ 25,00.')
