'''
Você está desenvolvendo um sistema com várias entidades.

Sua tarefa é:
1. Criar uma classe chamada Carro com os atributos modelo, cor e ano.
2. Criar uma instância da classe Carro e imprimir seus dados com o método __str__.
3. Criar uma classe Restaurante com os atributos nome, categoria, ativo e mais dois atributos à sua escolha.
4. Adicionar um construtor que define nome e categoria, e inicia ativo como False.
5. Adicionar o método __str__ para exibir os dados formatados.
6. Criar uma classe Cliente com quatro atributos e instanciar três objetos usando o construtor.
'''
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"{self.modelo} - {self.cor} - {self.ano}"

chevette = Carro("Chevette", "Branco", 1970)
print(chevette)


class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.especialidade = "Massas"
        self.prato_casa = "Lasanha"

    def __str__(self):
        return f"{self.nome} | {self.categoria} | Ativo: {self.ativo} | {self.especialidade} | {self.prato_casa}"

bom_paladar = Restaurante("Bom Paladar", "Caseira")
print(bom_paladar)


class Cliente:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} | {self.telefone} | {self.email} | {self.endereco}"

cliente1 = Cliente("José", "123456789", "jose@mail.com", "Rua A, 123")
cliente2 = Cliente("Ana", "987654321", "ana@mail.com", "Rua B, 456")
cliente3 = Cliente("Carlos", "555555555", "carlos@mail.com", "Rua C, 789")

print(cliente1)
print(cliente2)
print(cliente3)
