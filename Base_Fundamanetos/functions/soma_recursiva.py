'''
Paulo está desenvolvendo um programa para calcular valores acumulados
em um sistema financeiro.

Ele precisa somar todos os números inteiros de 1 até n,
onde n é um valor escolhido pelo usuário.

Sua tarefa é:
1. Criar uma função recursiva chamada soma_recursiva.
2. Essa função deve receber um número n.
3. A função deve retornar a soma de todos os números inteiros de 1 até n.
4. Solicitar o valor de n ao usuário.
5. Exibir o resultado com uma mensagem formatada.
'''

def soma_recursiva(n):
    if n == 0:
        return 0
    return n + soma_recursiva(n - 1)

numero = int(input("Digite um número: "))
resultado = soma_recursiva(numero)

print(f"A soma de 1 a {numero} é: {resultado}")


