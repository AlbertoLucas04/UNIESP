# QUESTÃO 10 

msg = ('Olá, sabia que eu sei descobrir qual é o tipo de triângulo apenas pela medida dos lados?')
print(msg)

l1 = int(input('Digite o valor do 01º lado: '))
l2 = int(input('Digite o valor do 02º lado: '))
l3 = int(input('Digite o valor do 03º lado: '))

if l1 == l2 and l3:
    print('Esse triângulo é Equilátero, pois possui todos os lados iguais.')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Esse triângulo é Isóceles, pois possui dois lados lados iguais.')
else:
    print('Esse triângulo é Escaleno, pois não possui nenhum lado igual.')