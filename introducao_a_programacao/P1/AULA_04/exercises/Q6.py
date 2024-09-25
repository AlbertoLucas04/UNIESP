# QUESTÃO 06

CONTA = 998834659
saldo_anterior = int('10000')
debito = int('1000')
credito = int('2500')
saldo_atual = saldo_anterior - debito + credito 

put_name = input('Digite seu nome: ')
put_conta = input('Digite sua conta: ')

if put_conta == f'{CONTA}':
    print('Olá, seja bem vindo(a)!')
    print('Aqui vai um extrato da sua conta:')
    print(f'Saldo anterior: {saldo_anterior}')
    print(f'Crédito: {credito}')
    print(f'Débito: {debito}')
    print(f'Saldo atual: {saldo_atual}')
    if saldo_atual < int('0'):
        print('Saldo negativo.')
    else:
        print('Saldo Positivo.')
else:
    print('Acesso negado.')
