'''
Carlos trabalha em um cartório e precisa validar se um CPF
informado pelo cliente tem o formato correto antes de prosseguir com o atendimento.

O CPF deve conter exatamente 11 dígitos numéricos.

Sua tarefa é:
1. Criar um programa que peça ao usuário um número de CPF.
2. Verificar se ele contém apenas números.
3. Verificar se ele tem exatamente 11 dígitos.
4. Exibir uma mensagem de sucesso ou erro conforme o caso.
'''
def validar_cpf(cpf):
    if not cpf.isdigit():
        print("Erro: O CPF deve conter apenas números.")
    elif len(cpf) != 11:
        print("Erro: O CPF deve ter exatamente 11 dígitos.")
    else:
        print("CPF válido.")

cpf = input("Digite seu CPF: ")
validar_cpf(cpf)
