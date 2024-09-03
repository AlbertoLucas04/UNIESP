#QUESTÃO 01

prova_01 = float(input("Digite a 01ª Nota: "))
prova_02 = float(input('Digite a 02ª Nota: '))

media_simples = (prova_01 + prova_02) / 2

if 0 <= media_simples <= 10:
    if media_simples >= 6:
        print('Parabéns, você foi aprovado!')
        print(f'{media_simples}')
    
    else: 
        print('Infelizmente, você não foi aprovado. Dirija-se à coordenação.')
        print(f'{media_simples}')
else: 
    print('Valor Incorreto!')

