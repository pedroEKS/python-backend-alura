"""
Aline está implementando uma funcionalidade que exibe mensagens personalizadas para os clientes
durante uma promoção especial da sua nova loja de livros.

O sistema deve exibir uma mensagem de contagem regressiva personalizada para cada número de 10 até 1,
e ao final exibir a mensagem: "Aproveite a promoção agora!".

Regras:
- Para números pares, exibir: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
- Para números ímpares, exibir: "A contagem continua: <número> segundos restantes.".
- Ao final da contagem, exibir: "Aproveite a promoção agora!".
"""

# Laço de contagem regressiva de 10 até 1
for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {segundos} segundos restantes.")

# Mensagem final após a contagem
print("Aproveite a promoção agora!")
