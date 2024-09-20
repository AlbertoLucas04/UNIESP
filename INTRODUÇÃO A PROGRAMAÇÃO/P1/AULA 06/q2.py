ok = input('Digite TABUADA para receber o arquivo: ')

print('É para já!')

with open(f"tabuada.txt", "w") as arquivo:
    
    for numero in range(1,11):
        arquivo.write(f'Tabuada do {numero}:\n')
        
        for multiplicador in range(1,11):
            linha = f'{numero} x {multiplicador} = {numero * multiplicador}\n'
            arquivo.write(linha)

print(f"Tabuada salva no Arquivo 'tabuada.txt'")
