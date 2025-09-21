'''
Pedro está desenvolvendo um sistema de cadastro
e precisa garantir que os usuários tenham senhas seguras.

Sua tarefa é:
1. Criar um programa que gere uma senha aleatória de 12 caracteres.
2. A senha deve conter pelo menos:
   - uma letra maiúscula
   - uma letra minúscula
   - um número
   - um caractere especial
3. Exibir a senha gerada ao usuário.
'''

import random
import string

def gerar_senha(tamanho=12, simbolos='!@#$%&*?'):
    senha = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(simbolos)
    ]
    todos_caracteres = string.ascii_letters + string.digits + simbolos
    senha += random.choices(todos_caracteres, k=tamanho - 4)
    random.shuffle(senha)
    return ''.join(senha)

print(f"Senha gerada: {gerar_senha()}")

