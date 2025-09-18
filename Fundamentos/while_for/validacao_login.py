"""
João está desenvolvendo um sistema de cadastro para um site de leitura.
Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos.

Regras:
    O nome de usuário deve ter pelo menos 5 caracteres.
    A senha deve ter pelo menos 8 caracteres.

O sistema deve continuar solicitando as informações até que ambas as condições sejam atendidas.
Quando o usuário insere dados válidos, o programa deve exibir a mensagem:
"Cadastro realizado com sucesso!".
"""

# Loop de validação
while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verifica as condições separadamente
    if len(usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
    elif len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
    else:
        print("Cadastro realizado com sucesso!")
        break
