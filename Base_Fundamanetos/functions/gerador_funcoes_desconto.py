'''
Miguel está desenvolvendo um sistema de cupons de desconto
e precisa aplicar diferentes taxas de desconto sobre os valores das compras.

Sua tarefa é:
1. Criar uma closure que gere uma função personalizada de desconto.
2. Essa função deve receber a porcentagem de desconto definida pelo usuário.
3. Depois, aplicar essa função ao valor da compra.
4. Exibir o preço final com o desconto aplicado.
'''
def gerar_desconto(porcentagem):
    def aplicar_desconto(valor):
        return valor * (1 - porcentagem / 100)
    return aplicar_desconto

# Entrada do usuário
porcentagem = float(input("Digite a porcentagem de desconto: "))
valor_compra = float(input("Digite o valor da compra: "))

# Gera a função personalizada e aplica o desconto
desconto = gerar_desconto(porcentagem)
preco_final = desconto(valor_compra)

print(f"Preço final com desconto: {preco_final}")
