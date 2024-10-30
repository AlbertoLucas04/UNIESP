shop_list = []

while True:
    print('\n =======================')
    print('1 - Adicionar novo item')
    print('2 - Remover item')
    print('3 - Exibir lista completa')
    print('0 - Sair')
    print('=======================')
    
    option = int(input('Digite a opção desejada: '))
    
    # Criar a opção para adicionar itens na lista
    match option:

        # Add item
        case 1:
            print('\n====> ADICIONAR ITEM <====\n')
            new_item = input('Insira o novo item: ')
            shop_list = shop_list + new_item

        # Remove item
        case 2:
            print('\n====> REMOVER ITEM <====\n')        
            for i in range(len(shop_list)):
                print(f'{i+1} - {shop_list[i]}')
            
            print("\n===")
            
            remove_item = int(input('Digite o código do item: ')) - 1
            del shop_list[remove_item]
            
            rem_item = input('Digite o código do item: ')
            
            
        # Exibir lista
        case 3:
            print('\n====> LISTA COMPLETA <====\n')
            
            for i in range(len(shop_list)):
                print(f'{i+1} - {shop_list[i]}')
