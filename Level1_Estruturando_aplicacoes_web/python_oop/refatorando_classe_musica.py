'''
Você está desenvolvendo um sistema para organizar músicas.

Sua tarefa é:
1. Refatorar a classe Musica que atualmente define atributos diretamente na classe.
2. Utilizar o método __init__ para tornar a classe mais concisa e expressiva.
3. Criar objetos da classe Musica com nome, artista e duração.
4. Exibir os dados de cada música.
'''

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica("Imagine", "John Lennon", 183)
musica2 = Musica("Bohemian Rhapsody", "Queen", 354)
musica3 = Musica("Clair de Lune", "Debussy", 300)

for musica in [musica1, musica2, musica3]:
    print(f"{musica.nome} - {musica.artista} ({musica.duracao} segundos)")
