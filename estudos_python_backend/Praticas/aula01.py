# print("Hello world!")
import os

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
    print('1. Cadastro de Restaurante.')
    print('2. Listar de Restaurante.')
    print('3. Ativar de Restaurante.')
    print('4. Sair.\n')

'''
def finalizar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Saindo... Até logo!')
    exit()
'''

def option_choice():
    option_chose = input('Escolha uma opção: ')
    print(f'Você escolheu a opção {option_chose}!')
    if option_chose == '1': 
       print('Cadastro de Restaurante escolhido!')
    elif option_chose == '2':
        print('Listar de Restaurante escolhido!')
    elif option_chose == '3':
        print('Ativar de Restaurante escolhido!')
    elif option_chose == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Saindo... Até logo!')
        exit()
    else:
        print('Opção inválida! Tente novamente.\n')
        options()
        option_choice()  
        
def main():
    app_name()
    options()
    option_choice()

if __name__ == '__main__':
    main()