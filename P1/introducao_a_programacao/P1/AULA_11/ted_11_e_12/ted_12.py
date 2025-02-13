import random

# Construindo a matriz A com valores randômicos de 0 a 100
A = [[random.randint(0, 100) for _ in range(10)] for _ in range(10)]

# Calculando a soma de todos os valores na matriz A
soma_total = sum(sum(linha) for linha in A)
print("Soma de todos os valores da matriz A:", soma_total)

# Construindo a matriz B onde cada elemento é o valor da matriz A * 3
B = [[valor * 3 for valor in linha] for linha in A]

# Exibindo a matriz B
print("Matriz B (Matriz A * 3):")
for linha in B:
    print(linha)