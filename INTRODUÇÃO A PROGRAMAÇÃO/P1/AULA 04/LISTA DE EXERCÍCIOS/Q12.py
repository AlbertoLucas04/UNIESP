# QUESTÃO 12 

msg = ('Olá, seja bem-vindo ao nosso Medidor Climático!')
print(msg)

temperatura = int(input('Insira a temperatura (°C): '))

if temperatura < 15:
    print('Está Frio!')
elif temperatura >= 15 and temperatura <= 25:
    print('Está Ameno!')
else:
    print('Está Quente!')



