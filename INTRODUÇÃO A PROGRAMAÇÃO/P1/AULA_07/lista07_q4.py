# QUESTÃO 04

from random import randint

print('Seja bem-vindo(a) ao jogo da advinhação!')

number = int(input('Digite um número e teste sua sorte: '))
r_n = randint(1,2)

while number:
    if number == r_n:
        print('Parabéns, você acertou o número!')
    else:
        input('Digite um número e teste sua sorte! ')
    
     
    