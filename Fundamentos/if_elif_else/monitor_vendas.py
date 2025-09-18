'''
Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho
de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs
e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles
teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem
indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem
dizendo que houve empate.
'''

# Solicita o número de vendas de cada produto
vendas_macas = int(input("Digite o número de vendas de maçãs: "))
vendas_bananas = int(input("Digite o número de vendas de bananas: "))

# Compara valores e exibe resultado
if vendas_macas > vendas_bananas:
    print("Maçãs tiveram mais vendas.")
elif vendas_bananas > vendas_macas:
    print("Bananas tiveram mais vendas.")
else:
    print("Houve um empate nas vendas.")

