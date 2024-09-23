import time

celebridades = ['Whindersson Nunes' , 'Tirulipa' , 'Tiririca' , 'Igor Guedes' , 'Douglas di Lima', 'Renan da Resenha', 'Messias Batista']

for c in celebridades:
    print(f'Olá, {c}, você está convidado para jantar na minha casa, dia 29/09, às 18:30!')
    time.sleep(1)
    print()   

print()

print('Pessoal, o Messias não poderá ir, pois estará sofrendo pelo Vasco!')

print()
print()

confirmados = ['Whindersson Nunes' , 'Tirulipa' , 'Tiririca' , 'Igor Guedes' , 'Douglas di Lima', 'Renan da Resenha']  
for rc in confirmados:
    print(f'{rc}, diferente do sofredor, você permanece convidado para jantar na minha casa, dia 29/09, às 18:30!')
    time.sleep(1)
    print()    
