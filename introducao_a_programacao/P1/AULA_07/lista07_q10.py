# QUESTÃO 08

from random import randint
from time import sleep

valor_dado = -1
n_lançamento = 0

n = int(input('Digite quantos lançamentos do dado: '))

for i in range((n)):
    
    vlr_lancamento = randint(1,6)
    
    if vlr_lancamento > valor_dado:
        valor_dado = vlr_lancamento
        n_lançamento = i + 1
        
    print(f'NL = {i} e Vlr = {vlr_lancamento}')
    sleep(0.5)
    
print('=== O maior lançamento ===')
print(f'Maior => {valor_dado} e o lançamento n° {n_lançamento}') 
