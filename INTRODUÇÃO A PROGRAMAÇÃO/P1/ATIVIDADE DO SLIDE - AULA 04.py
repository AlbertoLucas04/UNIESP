print('Olá, seja bem-vindo a Casa de Festas. Realize seu cadastro abaixo!')

name = input('Digite seu nome: ')
adress = input('Digite seu endereço: Av. ')
password = input('Digite sua senha: ')
idade = int(input('Digite sua idade: '))

if idade <= 17:
    print('Volte para casa!')
else:
    print('Confira as informações!')

print(f'{name}')
print(f'{adress}')
print(f'{password}')
print(f'{idade}')
