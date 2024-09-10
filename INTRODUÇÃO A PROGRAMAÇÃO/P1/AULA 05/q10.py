# QUESTÃP 10 

door = int(input('Escolha uma Porta: '))

match door:
    case 1:
        print('Você enfrentará o Desafio 01!')
    case 2:
        print('Você enfrentará o Desafio 02!')
    case 3:
        print('Você enfrentará o Desafio 03!')
    case 4:
        print('Você enfrentará o Desafio 04!')
    case 5:
        print('Você enfrentará o Desafio 05!')
    case _:
        print('Não consegui identificar a Porta escolhida!')