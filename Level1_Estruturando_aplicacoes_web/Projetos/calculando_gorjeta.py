'''
João trabalha como garçom em um restaurante e precisa calcular
a gorjeta que os clientes deixam ao pagar a conta.

O restaurante sugere uma gorjeta de 10%, mas alguns clientes
podem escolher dar mais ou menos.

Sua tarefa é:
1. Criar um programa que receba o valor total da conta.
2. Receber também a porcentagem de gorjeta desejada.
3. Calcular o valor da gorjeta.
4. Exibir o valor da gorjeta e o total a pagar.
'''
def calcular_gorjeta(conta, porcentagem):
    valor_gorjeta = conta * (porcentagem / 100)
    total = conta + valor_gorjeta
    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")

conta = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem de gorjeta: "))
calcular_gorjeta(conta, porcentagem)
