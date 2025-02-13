shop_list = []

# CASE 01
def add_item(shop_list:list) -> list:
    new_item = input('Insira o novo item: ')
    shop_list = shop_list + new_item
    return shop_list


# CASE 02

def remove_item(shop_list:list) -> list:
    remove_item = int(input('Digite o código do item: ')) -1
    del shop_list[remove_item]
    
    return shop_list
    
# CASE 03

def show_list(shop_list:list) -> list:
    
    for i in range(len(shop_list)):
        print(f'{i+1} - {shop_list[i]}')

    
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
            
            show_list(shop_list=shop_list)
            
            print("\n===")
            
            remove_item = int(input('Digite o código do item: ')) - 1
            del shop_list[remove_item]
            
            rem_item = input('Digite o código do item: ')
            
        # Exibir lista
        case 3:
            print('\n====> LISTA COMPLETA <====\n')
            
            show_list(shop_list=shop_list)
           
