'''
Sara está participando de um concurso de escrita,
e uma das regras exige que cada palavra do texto
tenha um limite máximo de caracteres.

Sua tarefa é criar uma função que receba uma palavra
e exiba a quantidade de caracteres dessa palavra.

Depois, o programa deve solicitar essa palavra ao usuário
e mostrar a quantidade de caracteres com uma mensagem formatada.
'''
def contar_caracteres(palavra):
    return len(palavra)

texto = input("Digite uma palavra: ")
quantidade = contar_caracteres(texto)

print(f"Essa palavra tem {quantidade} caracteres.")

