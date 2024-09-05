#    QUESTÃO 14

msg = ('Olá, seja bem-vindo(a) à sua Calculadora do IRPF!')
print(msg)

sal = float(input('Insira o seu Salário: R$  '))
imp_1 = sal * 0.1
imp_2 = sal * 0.15

if sal <= 2000:
    print('O seu IRPF é ISENTO de imposto!')
elif sal > 2000 and sal <= 3500:
    print(f'O seu IRPF tem o valor de R$ {imp_1}')
else: 
    print(f'O seu IRPF tem o valor de R$ {imp_2}')