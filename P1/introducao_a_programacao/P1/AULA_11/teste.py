print()
games_list = ['God of War', 'Call of Duty', 'The Last of Us', 'Fifa']

# Referenciando o índice dos jogos
for i in range(len(games_list)):
    
    print(f'{i} - {games_list[i]}')

# Separando os prints
print()
print('===================================================')
print()

# Referenciando apenas os jogos
for g in games_list:
    
    print(g, end=" | ")    
    
print("\n")
