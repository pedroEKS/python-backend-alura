'''
Pedro está criando um sistema de cadastro de produtos para sua loja
e percebeu que todos os números de telefone dos clientes
estão armazenados como strings.

Para facilitar buscas e validações, ele precisa que esses números
sejam tratados como inteiros.

Sua tarefa é:
1. Criar uma função que converta os números de telefone de string para inteiro.
2. Criar outra função que verifique se todos os números foram convertidos corretamente.
3. Exibir uma mensagem confirmando o sucesso da conversão.
'''
def converter_para_inteiro(numero_str):
    return int(numero_str)

def verificar_conversao(lista):
    return all(isinstance(item, int) for item in lista)

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

# Converte todos os números da lista
telefones_convertidos = [converter_para_inteiro(numero) for numero in telefones]

# Verifica se todos foram convertidos corretamente
if verificar_conversao(telefones_convertidos):
    print("Todos os números foram convertidos corretamente!")
else:
    print("Houve um erro na conversão.")

