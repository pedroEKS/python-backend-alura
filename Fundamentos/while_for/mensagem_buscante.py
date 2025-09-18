'''
Você está recebendo uma lista de valores representando os produtos de sua loja virtual
e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
'''

# Lista de valores dos produtos vendidos na semana
valores = [10, 20, 30, 40, 50]

# Inicializa a variável que armazenará a soma total
soma = 0

# Percorre cada valor da lista e acumula na variável soma
for valor in valores:
    soma += valor

# Exibe o resultado final da soma
print(f"A soma total dos produtos é: R$ {soma}")
