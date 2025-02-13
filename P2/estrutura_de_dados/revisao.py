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

put_num1 = int(input('Insira um número: '))

for i in put_num1:
    


