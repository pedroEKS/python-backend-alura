'''
Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido.

Ela quer um programa onde:
1. O computador escolhe um número aleatório entre 1 e 100.
2. O jogador tenta adivinhar qual é esse número.
3. O programa informa se o palpite é maior ou menor que o número correto.
4. O jogo continua até o jogador acertar.
5. Se o jogador digitar um valor inválido (letras ou número fora do intervalo),
   uma exceção ValueError deve ser lançada com uma mensagem apropriada.
'''

import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            chute = int(input("Tente adivinhar o número (1-100): "))
            if chute < 1 or chute > 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")
            
            tentativas += 1

            if chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError as erro:
            print(f"Entrada inválida: {erro}")

adivinhar_numero()
