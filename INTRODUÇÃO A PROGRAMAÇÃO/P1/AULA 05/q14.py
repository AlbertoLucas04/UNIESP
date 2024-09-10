# QUESTÃO 14

at_g1 = int(input('Guerreiro 01, insira o seu valor de ataque: '))
def_g1 = int(input('Guerreiro 01, insira o seu valor de defesa: '))

at_g2 = int(input('Guerreiro 02, insira o seu valor de ataque: '))
def_g2 = int(input('Guerreiro 02, insira o seu valor de defesa: '))

s1 = at_g1 + def_g1
s2 = at_g2 + def_g2

if s1 > s2:
    print('O vencedor é o Guerreiro 01!')     
elif s2 > s1: 
    print('O vencedor é o Guerreiro 02!')
elif def_g1 > def_g2:
      print('O vencedor é o Guerreiro 01!')
elif def_g2 > def_g1:
    print('O vencedor é o Guerreiro 02!')
else:
     print('Houve um empate!')


