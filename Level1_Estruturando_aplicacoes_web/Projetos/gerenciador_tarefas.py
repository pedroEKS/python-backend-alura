'''
Ana precisa de um programa simples para gerenciar suas tarefas diárias.

Sua tarefa é:
1. Criar um menu interativo com opções:
   - Adicionar tarefa
   - Visualizar tarefas
   - Remover tarefa
   - Sair
2. Usar uma lista para armazenar as tarefas.
3. Tratar erros como:
   - Remover tarefa inexistente
   - Entrada inválida (letras em vez de números)
   - Opção fora do menu
4. Exibir mensagens apropriadas para cada ação.
'''


tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def visualizar_tarefas():
    if tarefas:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("Nenhuma tarefa adicionada.")

def remover_tarefa():
    if not tarefas:
        print("Erro: Nenhuma tarefa para remover.")
        return
    try:
        numero = int(input("Digite o número da tarefa a ser removida: "))
        tarefa_removida = tarefas.pop(numero - 1)
        print(f"Tarefa '{tarefa_removida}' removida!")
    except ValueError:
        print("Erro: Entrada inválida! Digite um número.")
    except IndexError:
        print("Erro: Número de tarefa inexistente.")

def menu():
    while True:
        print("\n1. Adicionar tarefa\n2. Visualizar tarefas\n3. Remover tarefa\n4. Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                adicionar_tarefa()
            case "2":
                visualizar_tarefas()
            case "3":
                remover_tarefa()
            case "4":
                print("Saindo do gerenciador de tarefas. Até mais!")
                break
            case _:
                print("Erro: Opção inválida! Escolha uma opção entre 1 e 4.")

menu()
