'''
Carlos está criando uma calculadora simples, mas quer garantir que o programa
não quebre se o usuário digitar valores inválidos.

Sua tarefa é:
1. Criar uma calculadora que permita escolher entre soma, subtração, multiplicação e divisão.
2. Modularizar o código em funções.
3. Usar try-except para tratar erros:
   - ValueError: se o usuário digitar letras em vez de números.
   - ZeroDivisionError: se tentar dividir por zero.
4. Exibir mensagens apropriadas para cada erro.
'''

def calcular(operacao, a, b):
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return operacoes[operacao](a, b)

try:
    numero_1 = float(input("Digite o primeiro número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    if operacao not in ('+', '-', '*', '/'):
        print("Opção inválida.")
    else:
        numero_2 = float(input("Digite o segundo número: "))
        resultado = calcular(operacao, numero_1, numero_2)
        print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")


