# QUESTÃO 15

msg = ('Olá, seja bem-vindo(a) ao seu Controlador de Velocidade!')

vel = float(input('Insira aqui a sua Velocidade (Km/h): '))
multa = (vel - 80) * 5

if vel <= 80:
    print('Você está dentro do limite de velociade. Continue assim!')
else:
    print(f'Você será multado no valor de R$ {multa}.')