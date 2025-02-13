# QUESTÃO 8

num = int(input('Insira um número: '))

if num == 0:
    print('0, em Binário, é 0!')

elif num == 1:
    print('1, em Binário, é 1!')

else:
    while (num/2 != 1):
      num /= 2
      num %= 2
      if num/2 == 1:
        break

print(num)

