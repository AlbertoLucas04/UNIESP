# QUESTÃO 13

msg = ('Olá, seja bem-vindo à Pesquisa Eleitoral!')
print(msg)

cand = int(input('Digite qual o número do seu canditado: '))

match cand:
    case 1:
        print('Você votou no candidato A!')
    case 2:
        print('Você votou no candidato B!')
    case 3:
        print('Você votou no candidato C!')
    case _: 
        print('Você votou nulo!') 

