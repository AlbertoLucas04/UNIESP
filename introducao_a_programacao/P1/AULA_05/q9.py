# QUESTÃO 09 

feit = int(input('Escolha um feitiço: '))

match feit: 
    case 1:
        print('Você escolheu o Feitiço Fogo!') 
    case 2:
        print('Você escolheu o Feitiço Água!')
    case 3:
        print('Você escolheu o Feitiço Terra!')
    case _:
        print('Não consegui identificar o Feitiço escolhido!')
        