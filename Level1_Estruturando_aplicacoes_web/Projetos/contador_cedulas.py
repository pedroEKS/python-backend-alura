'''
Um banco está desenvolvendo um sistema para caixas eletrônicos
e precisa de um programa que simule o saque de dinheiro.

Sua tarefa é:
1. Solicitar ao usuário o valor do saque.
2. Validar se o valor é múltiplo de 2 (não há cédulas de R$1).
3. Calcular a menor quantidade possível de cédulas para entregar o valor.
4. Usar as cédulas disponíveis: R$100, R$50, R$20, R$10, R$5 e R$2.
5. Tratar erros de entrada (como valores não numéricos).
6. Exibir a quantidade de cada cédula usada.
'''

def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {}
    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
            valor -= quantidade * cedula
    return resultado

def caixa_eletronico():
    try:
        valor = int(input("Digite o valor do saque: R$ "))
        if valor <= 0:
            print("O valor deve ser maior que zero.")
        elif valor % 2 != 0:
            print("Erro: O valor deve ser múltiplo de 2.")
        else:
            cedulas_necessarias = calcular_cedulas(valor)
            print("\nCédulas entregues:")
            for cedula, quantidade in cedulas_necessarias.items():
                print(f"{quantidade} de R$ {cedula}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

caixa_eletronico()
