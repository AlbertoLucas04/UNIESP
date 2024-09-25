num = int(input('Insira um número para ter sua Tabuada: '))

with open(f'tabuada_do_{num}.txt', 'w') as arquivo:

    for m in range(1,11):
        operation = f'{num} x {m} = {num * m}\n'
        arquivo.write(operation)

print(f"A Tabuada foi salva como 'tabuada_do_{num}.txt'")