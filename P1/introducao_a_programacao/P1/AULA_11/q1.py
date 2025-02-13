# QUESTÃO 01

clubes = ['Flamengo', 'Vasco', 'Fluminense', 'Palmeiras', 'São Paulo']

v_clube = input('Digite o seu clube do coração: ')

search_confirm = False

for c in clubes:
   
   if c.upper() == v_clube.upper():
       search_confirm = True
       
if search_confirm:
    print('Achei!')
else:
    print('Não Achei!')
   
   