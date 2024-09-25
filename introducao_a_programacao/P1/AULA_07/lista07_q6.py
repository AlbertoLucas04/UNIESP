# QUESTÃO 06
import math

print('Olá, seja bem-vindo(a) ao Verificador de Números Primos!')

num = int(input('Insira um número: '))

for primo in range(2, int(num**0.5) + 1):
    if num % primo == 0:
        print(f'O número {num} não é primo!')
        break
    else:
        print(f'O número {num} é primo!')
        break