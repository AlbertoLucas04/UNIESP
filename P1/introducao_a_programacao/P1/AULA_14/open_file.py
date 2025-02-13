filename = 'jesus_vive.txt'

message = input('Digite: ')

with open(filename, 'a', encoding="UTF-8") as arquivo:
    arquivo.write(message + "\n")
    
with open(filename, "r", encoding="UTF-8") as other_file:
    conteudo = other_file.read()
    print(conteudo)
    


    