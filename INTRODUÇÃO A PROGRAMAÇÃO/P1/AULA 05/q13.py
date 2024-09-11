#  QUESTÃO 13

def tratar_texto(pos_ar):
    pos_ar = pos_ar.capitalize()
    pos_ar = pos_ar.strip()
    return pos_ar

pos_ar = input('Insira onde está o exército: ')
pos_ar = tratar_texto(pos_ar)

match pos_ar:
    case "Dentro":
        print('O Sistema de Defesa do Castelo não será ativado.')
    case "Fora":
        print('O Sistema de Defesa do Castelo será ativado.')
    case _:
        print('Posição do Exército não identificada.')

