celebridades = ['Whindersson Nunes' , 'Tirulipa' , 'Tiririca' , 'Igor Guedes' , 'Douglas di Lima', 'Renan da Resenha', 'Messias Batista']

for c in celebridades:
    print(f'Olá, {c}, você está convidado para jantar na minha casa, dia 22/09, às 16:00!')

    for rc in celebridades:
        celebridades.pop()
        print('Pessoal, o Messias não poderá ir, pois está sofrendo pelo Vasco!')
        print(f'Olá, {rc}, permanece convidado para jantar na minha casa, dia 22/09, às 16:00!')

    