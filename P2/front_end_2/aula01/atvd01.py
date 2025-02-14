

alturas_masc = [1.61, 1.72, 1.83, 1.74, 1.95, 1.86, 1.92, 1.68]

alturas_fem = [1.79, 1.63, 1.57, 1.75, 1.72, 1.71, 1.58]

max_masc = max(alturas_masc)
min_masc = min(alturas_masc)

max_fem = max(alturas_fem)
min_fem = min(alturas_fem)

media_alturas_masc = sum(alturas_masc) / len(alturas_masc)
media_alturas_masc_modelado = round(media_alturas_masc, 2)
qtd_fem = len(alturas_fem)

print('\n=== Olá, seja bem-vindo(a) ao Expositor de Dados ===\n')
print('De qual grupo você deseja obter os dados?\n')
print('1. Masculino\n2. Feminino\n3. Ambos os grupos')
put_option = int(input('\n=> '))

match put_option:

    case 1:
        print('\nSegue os dados solicitados.\n')
        print('Dados (Grupo Masculino)')
        print(f'Maior altura: {max_masc} m')
        print(f'Menor altura: {min_masc} m')
        print(f'Média das alturas: {media_alturas_masc_modelado} m\n')

    case 2:
        print('Segue os dados solicitados.\n')
        print('Dados (Grupo Feminino)')
        print(f'Maior altura: {max_fem} m')
        print(f'Menor altura: {min_fem} m')
        print(f'Quantidade de pessoas: {qtd_fem}\n')

    case 3:
        print('\nSegue os dados solicitados.\n')
        print('Dados (Grupo Masculino)')
        print(f'Maior altura: {max_masc} m')
        print(f'Menor altura: {min_masc} m')
        print(f'Média das alturas: {media_alturas_masc_modelado} m\n\n')
        print('Dados (Grupo Feminino)')
        print(f'Maior altura: {max_fem} m')
        print(f'Menor altura: {min_fem} m')
        print(f'Quantidade de pessoas: {qtd_fem}')

    case _:
        print("Insira um código válido.")


    


