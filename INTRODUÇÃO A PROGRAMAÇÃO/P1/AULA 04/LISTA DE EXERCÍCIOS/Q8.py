# QUESTÃO 08

msg = str('Olá, seja bem-vindo ao nosso programa de descontos!')
print(msg)

vlr_da_compra = float(input('Digite o valor da compra: R$ '))
desc_100 = vlr_da_compra - (vlr_da_compra * 0.1)
desc_50_100 = vlr_da_compra - (vlr_da_compra * 0.05)

if vlr_da_compra > 100:
    print(f'Você recebeu um desconto! O valor da compra será de: R$ {desc_100} ')
elif vlr_da_compra >= 50 and vlr_da_compra <= 100:
    print(f'Você recebeu um desconto! O valor da compra será de: R$ {desc_50_100}')
else:
    print(f'Você recebeu não um desconto! O valor da compra será de: R$ {vlr_da_compra}')
    
