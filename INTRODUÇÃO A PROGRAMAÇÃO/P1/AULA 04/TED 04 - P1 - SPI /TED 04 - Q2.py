#  QUESTÃO 02

msg =('Olá, seja bem-vindo(a) ao Mercado das Maçãs!')
print(msg)

apple = int(input('Insira a quantidade de maçãs compradas (Un): '))
vlr_11apple = apple * 1.30
promo_12apple = apple * 1

if apple > 12:
  print(f'Sua compra deu R$ {vlr_11apple}')
elif apple >= 12:
  print(f'Sua compra deu R$ {promo_12apple}')

                  
