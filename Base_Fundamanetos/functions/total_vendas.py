'''
Carlos trabalha em um comércio e precisa saber o valor total
das vendas realizadas no dia.

As vendas são informadas em uma única linha, separadas por espaços.

Sua tarefa é:
1. Criar um programa que receba essa linha de valores.
2. Converter cada valor para número.
3. Calcular a soma total das vendas.
4. Exibir o resultado com uma mensagem formatada.
'''
def calcular_total_vendas(lista):
    total = 0
    for valor in lista:
        total += float(valor)
    return total

entrada = input("Digite os valores das vendas separados por espaço: ")
valores = entrada.split()
total = calcular_total_vendas(valores)

print(f"O total de vendas foi: {total}")
