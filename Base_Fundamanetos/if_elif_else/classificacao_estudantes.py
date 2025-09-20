'''
Uma professora precisa de um programa que ajude a calcular a média final dos 
alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. 
As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado

Escreva um programa que receba três notas como entrada e calcule a média final. 
Com base na média, exiba a situação do aluno.
'''

# Recebe as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Exibe a média
print(f"Média final: {media:.2f}")

# Classifica o aluno
if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
