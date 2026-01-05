'''
Você está desenvolvendo um sistema para gerenciar restaurantes.

Sua tarefa é:
1. Criar uma instância chamada restaurante_praca da classe Restaurante.
2. Atribuir o valor 'Italiana' ao atributo categoria dessa instância.
3. Acessar o valor do atributo nome da instância restaurante_praca.
4. Verificar se o restaurante está ativo e exibir uma mensagem.
5. Acessar o atributo de classe categoria diretamente pela classe.
6. Alterar o nome da instância restaurante_praca para 'Bistrô'.
7. Criar uma nova instância chamada restaurante_pizza com nome 'Pizza Place' e categoria 'Fast Food'.
8. Verificar se a categoria da instância restaurante_pizza é 'Fast Food'.
9. Ativar a instância restaurante_pizza.
10. Imprimir o nome e a categoria da instância restaurante_praca.
'''
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante("Praça", "Italiana")
print(restaurante_praca.nome)

if restaurante_praca.ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")

restaurante_praca.nome = "Bistrô"

restaurante_pizza = Restaurante("Pizza Place", "Fast Food")
if restaurante_pizza.categoria == "Fast Food":
    print("A categoria é Fast Food.")
else:
    print("A categoria não é Fast Food.")

restaurante_pizza.ativo = True

print(f"Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}")
