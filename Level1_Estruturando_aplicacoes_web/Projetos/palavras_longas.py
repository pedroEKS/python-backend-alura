'''
Sofia é revisora de textos e precisa identificar palavras muito longas
em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas,
então ela quer um programa que encontre palavras com mais de 10 letras
e as exiba em destaque.

Sua tarefa é:
1. Criar um programa que receba um texto digitado pelo usuário.
2. Identificar todas as palavras com mais de 10 letras.
3. Exibir essas palavras em uma lista.
4. Caso nenhuma palavra longa seja encontrada, avisar o usuário.
'''

def identificar_palavras_longas(texto):
    palavras = texto.split()
    longas = [p for p in palavras if len(p) > 10]
    
    if longas:
        print("Palavras longas encontradas:", ", ".join(longas))
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")

entrada = input("Digite um texto: ")
identificar_palavras_longas(entrada)
