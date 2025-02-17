# 1.Faça um programa que calcule a média de três números inseridos pelo usuário.

def media_calculator(a,b,c):
    media = (a + b + c) / 3
    return media

n1 = float(input('Insira sua 1ª nota: '))
n2 = float(input('Insira sua 2ª nota: '))
n3 = float(input('Insira sua 3ª nota: '))

result = media_calculator(n1,n2,n3)

print(f'\nMédia = {result}')

# 2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

put_num = float(input('Insira um número: '))

if put_num % 2 == 0:
    print('/nEsse número é par!')
else:
    print('/nEsse número é ímpar!')

''' 3. Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
esse número.'''

put_num = int(input('Insira um número: '))

for p in range(0, put_num + 1):
  if p % 2 == 0:
    print(p)

''' 4. Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista. '''

num_list = [27, 5, 83, 14, 62, 39, 71, 8, 56, 90]

print(f'A lista é {num_list}')

max_num = max(num_list)
min_num = min(num_list)

print(f'\nO maior número é {max_num}')
print(f'O menor número é {min_num}')

''' 5. Faça um programa que leia uma lista de números e retorne a média dos números pares. '''

num_list = [3, 7, 15, 22, 8, 11, 29, 4, 18, 9]

par_list = []

for num in num_list:
    if num % 2 == 0:
        par_list.append(num)

media_par_list = sum(par_list) / len(par_list)

print(f'A média dos números pares dessa lista é {media_par_list}')
    
''' 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
número. '''
from math import factorial

put_num = int(input('Insira um número: '))
fat = factorial(put_num2)

print(f'\n{put_num2}! = {fat}')

''' 7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário. '''


    


