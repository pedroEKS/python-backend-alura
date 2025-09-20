'''
Joana está participando de um processo seletivo para uma vaga de desenvolvedora
e recebeu um desafio técnico: criar uma calculadora que realize operações básicas
(soma, subtração, multiplicação e divisão) entre dois números.

Sua tarefa é:
1. Criar funções lambda para cada operação matemática.
2. Solicitar ao usuário dois números e o operador desejado (+, -, * ou /).
3. Executar a operação correspondente e exibir o resultado formatado.
'''
def calcula(operacao, a, b):
    somar = lambda a, b: a + b
    subtrair = lambda a, b: a - b
    multiplicar = lambda a, b: a * b
    dividir = lambda a, b: a / b if b != 0 else "Erro: divisão por zero"

    match operacao:
        case "+":
            return somar(a, b)
        case "-":
            return subtrair(a, b)
        case "*":
            return multiplicar(a, b)
        case "/":
            return dividir(a, b)
        case _:
            return "Operação inválida"

# Entrada do usuário
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (| + | - | * | / |): ")

# Resultado
resultado = calcula(operacao, a, b)
print(f"O resultado é: {resultado}")
