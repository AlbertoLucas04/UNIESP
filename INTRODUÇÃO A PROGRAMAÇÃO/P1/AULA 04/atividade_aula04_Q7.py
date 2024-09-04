# QUESTÃO 07

qtd_max = int('150')
qtd_min = int('30')
qtd_media = (qtd_max + qtd_min) / 2

qtd_atual = int(input('Insira a quantidade atual do produto: '))

if qtd_atual < qtd_media:
    print('Efetuar compra.')
else:
    print('Não efetuar compra.')