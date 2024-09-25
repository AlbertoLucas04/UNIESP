# QUESTÃO 07

import string
import math
import time

def verificar_nome(nome):
    if nome != str.isalpha:
        print('NOME: Insira apenas Letras!')   
    if nome != str.istitle:
        print('NOME: Insira, em cada nome, letras maiúsculas!') 

    return
    
    
def verificar_idade(idade):
    if idade != str.isdigit: 
        print('IDADE: Insira apenas números!')
    else:
       return
    
name = input('Insira seu nome: ')   
age = input('Insira sua idade: ')
email = input('insira seu email: ')

print('Confira se suas informações estão corretas!')


time.sleep(3)
v_n = verificar_nome(name)
v_i = verificar_idade(age)
