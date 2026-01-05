'''
Beatriz está desenvolvendo um sistema de atendimento para um site de serviços.

Ela deseja criar um programa que exiba uma saudação personalizada
dependendo da hora do dia que o usuário acessa a plataforma.

O sistema deverá seguir a seguinte lógica:
- Se for antes das 12h, exibir "Bom dia"
- Se for entre 12h e 18h, exibir "Boa tarde"
- Se for após 18h, exibir "Boa noite"

Sua tarefa é criar uma função que receba a hora atual
e retorne a saudação correspondente.

Depois, o programa deve solicitar a hora ao usuário
e exibir a saudação apropriada.
'''

def saudacao(hora):
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

hora_atual = int(input("Digite a hora atual (0-23): "))
mensagem = saudacao(hora_atual)
print(mensagem)
