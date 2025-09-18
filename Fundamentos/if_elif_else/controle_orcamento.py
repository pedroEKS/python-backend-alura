'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um 
programa que ajude a controlar suas despesas. O programa deve receber o 
total de despesas realizadas e informar se ele ultrapassou o limite ou 
ainda está dentro do orçamento.
'''

# Recebe o valor total das despesas
despesas = float(input("Digite o total de despesas do mês: R$ "))

# Define o limite de orçamento
limite = 3000.00

# Verifica se ultrapassou o limite
if despesas > limite:
    print("Atenção! Você ultrapassou o limite de orçamento mensal.")
else:
    print("Parabéns! Você está dentro do orçamento.")
