'''
Julia é professora e precisa de um programa simples
para ajudar seus alunos a calcularem suas idades.

Sua tarefa é criar uma função chamada calcular_idade
que receba dois valores:
- o ano de nascimento
- o ano atual

A função deve retornar a idade calculada.

Depois, o programa deve solicitar esses dados ao usuário
e exibir a idade com uma mensagem formatada.
'''
def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

nascimento = int(input("Digite o ano de nascimento: "))
atual = int(input("Digite o ano atual: "))
idade = calcular_idade(nascimento, atual)

print(f"A idade é {idade} anos.")
