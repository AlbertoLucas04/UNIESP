# Importando biblioteca para entrada de dados
vetor = []

# Lendo 10 números e armazenando no vetor
for i in range(10):
    num = int(input(f"Digite o número {i + 1}: "))
    vetor.append(num)

# Verificando e exibindo números repetidos e suas posições
repetidos = {}
for i, valor in enumerate(vetor):
    if vetor.count(valor) > 1:
        if valor not in repetidos:
            repetidos[valor] = []
        repetidos[valor].append(i)

# Exibindo o resultado
if repetidos:
    print("Números repetidos e suas posições:")
    for num, posicoes in repetidos.items():
        print(f"Número {num} nas posições {posicoes}")
else:
    print("Não há números repetidos.")