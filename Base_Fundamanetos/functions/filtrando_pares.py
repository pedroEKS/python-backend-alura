'''
Lucas está desenvolvendo um sistema para gerar relatórios financeiros
e precisa filtrar apenas os valores pares de uma lista de números
informada pelo usuário.

Sua tarefa é:
1. Criar um programa que receba uma lista de números digitados pelo usuário.
2. Utilizar a função filter() para selecionar apenas os números pares.
3. Exibir os números pares em uma mensagem formatada.
'''
def filtrar_pares(numeros):
    return list(filter(lambda x: int(x) % 2 == 0, numeros))

entrada = input("Digite os números separados por espaço: ")
lista_numeros = entrada.split()
pares = filtrar_pares(lista_numeros)

print("Números pares:", " ".join(pares))
