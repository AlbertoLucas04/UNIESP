x = 0
acumuladora = 0 
soma_notas = 0

while x != -1:
    
    x = float(input('Digite a média ou -1 para sair: '))
    if x != -1:
        soma_notas = soma_notas + x
        acumuladora = acumuladora + 1
    
media = soma_notas / acumuladora

print(media)
