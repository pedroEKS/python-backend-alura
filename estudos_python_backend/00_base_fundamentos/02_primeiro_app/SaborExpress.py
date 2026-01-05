import os

# Lista para armazenar os restaurantes
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def app_name():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      ''')
    
def options():
    print('1. Cadastro de Restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar Status do Restaurante')
    print('4. Sair\n')

def back_to_menu():
    ''' Função auxiliar para voltar ao menu principal após uma ação '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def register_restaurant():
    ''' Função para cadastrar novo restaurante '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--- Cadastro de Restaurante ---\n')
    
    name_restaurant = input('Digite o nome do restaurante: ')
    category = input(f'Digite a categoria do {name_restaurant}: ')
    
    # Criando o dicionário e adicionando na lista
    restaurant_data = {'nome': name_restaurant, 'categoria': category, 'ativo': False}
    restaurantes.append(restaurant_data)
    
    print(f'\nO restaurante {name_restaurant} foi cadastrado com sucesso!')
    back_to_menu()

def list_restaurants():
    ''' Função para listar os restaurantes '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--- Listando Restaurantes ---\n')
    
    # Cabeçalho da tabela
    print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
    
    for restaurant in restaurantes:
        name = restaurant['nome']
        category = restaurant['categoria']
        # Lógica ternária para exibir o texto correto
        status = 'Ativado' if restaurant['ativo'] else 'Desativado'
        
        print(f'{name.ljust(25)} | {category.ljust(25)} | {status}')

    back_to_menu()

def toggle_status():
    ''' Função para ativar ou desativar restaurante '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--- Alterar Status do Restaurante ---\n')
    
    name_search = input('Digite o nome do restaurante para alterar o estado: ')
    found = False
    
    for restaurant in restaurantes:
        if restaurant['nome'] == name_search:
            found = True
            restaurant['ativo'] = not restaurant['ativo'] # Inverte o valor booleano
            msg = f'O restaurante {name_search} foi ativado com sucesso!' if restaurant['ativo'] else f'O restaurante {name_search} foi desativado com sucesso!'
            print(msg)
            
    if not found:
        print('O restaurante não foi encontrado.')
        
    back_to_menu()

def option_choice():
    try:
        option_chose = input('Escolha uma opção: ')

        if option_chose == '1': 
            register_restaurant()
        elif option_chose == '2':
            list_restaurants()
        elif option_chose == '3':
            toggle_status()
        elif option_chose == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Saindo... Até logo!')
            exit() # Encerra o programa
        else:
            print('Opção inválida! Tente novamente.\n')
            back_to_menu()
            
    except:
        print('Erro inesperado!')
        back_to_menu()
        
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name()
    options()
    option_choice()

if __name__ == '__main__':
    main()