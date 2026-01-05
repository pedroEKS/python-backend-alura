'''
Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas:
uma contendo os nomes dos produtos e outra com seus respectivos preços.

Para facilitar a organização, ela precisa combinar essas listas
de forma que cada produto seja associado ao seu preço.

Sua tarefa é:
1. Solicitar ao usuário os nomes dos produtos, separados por vírgula.
2. Solicitar os preços correspondentes, também separados por vírgula.
3. Criar uma função que junte essas listas e exiba o resultado
   no formato: produto: preço
'''
def exibir_produtos_com_precos(produtos, precos):
    for produto, preco in zip(produtos, precos):
        print(f"{produto.strip()}: {preco.strip()}")

produtos = input("Digite os produtos separados por vírgula: ").split(',')
precos = input("Digite os preços separados por vírgula: ").split(',')

exibir_produtos_com_precos(produtos, precos)
