# QUESTÃO 05
import math

p_number = int(input('Quantos números da sequência de Fibonacci você deseja? '))
first = 0
second = 1

if p_number <= first:
    print('Não há nada para apresentar. Insira um número maior que 0!')
elif p_number == second:
    print('O número é: 1')
else:
    print(first, end=' | ')
    print(second, end=' | ')
    
    for _ in range(2,p_number):
        
        next_number = first + second
        print(next_number, end=' | ')
        
        first = second
        second = next_number   
    