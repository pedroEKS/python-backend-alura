'''
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador.

Sua tarefa é:
1. Criar um programa que permita ao usuário escolher entre pedra, papel ou tesoura.
2. Fazer o computador escolher aleatoriamente uma das três opções.
3. Comparar as escolhas e determinar o vencedor com base nas regras:
   - Pedra ganha de Tesoura
   - Tesoura ganha de Papel
   - Papel ganha de Pedra
   - Se ambos escolherem a mesma opção, é um empate
4. Exibir a escolha do computador e o resultado da partida.
'''

import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    jogador = input("Escolha: pedra, papel ou tesoura? ").lower()
    
    if jogador not in opcoes:
        print("Escolha inválida.")
        return

    computador = random.choice(opcoes)
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "tesoura" and computador == "papel") or \
         (jogador == "papel" and computador == "pedra"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

jogar()
