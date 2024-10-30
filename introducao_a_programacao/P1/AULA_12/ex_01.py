# Matriz
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matrix)

# Imprime a primeira lista
print(matrix[1])

# Imprime a segunda lista e o elemento zero da mesma
print(matrix[2][0])

# Percorre a matriz
for i in range(len(matrix)):
    print(matrix[i])
    for j in range(len(matrix[i])):
        print(matrix[i][j])