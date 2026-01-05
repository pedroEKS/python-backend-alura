'''
Mariana é professora de língua portuguesa e quer um programa
que conte quantas vogais há em um texto digitado pelos alunos.

Isso ajudará a analisar a estrutura das palavras utilizadas.

Sua tarefa é:
1. Criar um programa que peça um texto ao usuário.
2. Contar quantas vogais (a, e, i, o, u) aparecem no texto.
3. Exibir o total de vogais encontradas.
'''

def contar_vogais(texto):
    vogais = "aeiou"
    contador = 0
    for letra in texto.lower():
        if letra in vogais:
            contador += 1
    return contador

entrada = input("Digite um texto: ")
total_vogais = contar_vogais(entrada)

print(f"O texto contém {total_vogais} vogais.")
