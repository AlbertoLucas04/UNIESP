import os

with open('vingadores.txt', 'r') as arquivo:
    vingadores = arquivo.read()    
    
    with open('vingadores.txt', 'r') as arquivo:
        vingadores = arquivo.readlines()      
 
        for convite in vingadores:
            print(f'Olá, {vingadores}, você está convidado(a) para a minha festa!')


    