'''
Você está criando um sistema para organizar músicas.

Sua tarefa é:
1. Criar uma classe chamada Musica.
2. A classe deve ter três atributos: nome, artista e duracao.
3. Criar três objetos da classe Musica com valores diferentes.
4. Exibir os dados de cada música formatados.
'''
class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica("Merry Go Round of Life", "Joe Hisaishi", "6:07")
musica2 = Musica("Cello Suite No. 1", "Bach", "3:01")
musica3 = Musica("Concerto for Two Cellos", "Vivaldi", "4:05")

for musica in [musica1, musica2, musica3]:
    print(f"Nome: {musica.nome} | Artista: {musica.artista} | Duração: {musica.duracao}")
