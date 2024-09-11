#   QUESTÃO 15

def tratar_parametros(time):
    time = time.replace(",", ".")
    return time 

en = float(input('Insira o Percentual de Energia (%): '))
coord = float(input('Insira as Coordenadas de Destino: '))
time = float(input('Insira o Tempo (Min): '))
time_tratado = time.replace(",", ".")

P_EN = 80
P_COORD = 17200596
P_TIME = 3.78

if en >= P_EN and coord == P_COORD and time == P_TIME:
    print('O Portal está pronto para ser iniciado!')
elif en < P_EN:
    print('Cheque a Energia!')
elif coord != P_COORD:
    print('Cheque as Coordenadas!')
elif time != P_TIME:
    print('Cheque o Tempo!')
else: 
    print('Cheque os Parâmetros inseridos!')
    