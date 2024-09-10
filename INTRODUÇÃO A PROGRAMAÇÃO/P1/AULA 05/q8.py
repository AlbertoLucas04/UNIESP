# QUESTÃO 08

tasks = int(input('Insira o número de missões: '))

if tasks > 10:
    print('Você receberá 100 moedas de ouro!')
elif tasks >= 5 and tasks <= 10:
    print('Você receberá 50 moedas de ouro!')
elif tasks < 5:
    print('Você receberá 05 moedas de ouro!')
    