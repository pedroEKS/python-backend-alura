# 1. Verificar se um numero é par ou ímpar
'''
#Usando If e Else

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

'''


#Usando match

numero = int(input("Digite um número: "))

match numero % 2:
    case 0:
        print("O número é par.")
    case 1:
        print("O número é ímpar.")


# 2. Classificação por idade
'''
# Usando if elif else

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 18:
    print("Adolescente")
elif idade > 18:
    print("Adulto")
else:
    print("Idade inválida")
'''

# Usando match 

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 18:
    print("Adolescente")
elif idade > 18:
    print("Adulto")
else:
    print("Idade inválida")

# 3. Verificação de Login
'''
# Usando if else

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 18:
    print("Adolescente")
elif idade > 18:
    print("Adulto")
else:
    print("Idade inválida")
'''

# Usando match

idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 18:
    print("Adolescente")
elif idade > 18:
    print("Adulto")
else:
    print("Idade inválida")

# 4. Determinar quadrante no plano cartesiano
'''
# Usando if elif else

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("Primeiro Quadrante")
elif x < 0 and y > 0:
    print("Segundo Quadrante")
elif x < 0 and y < 0:
    print("Terceiro Quadrante")
elif x > 0 and y < 0:
    print("Quarto Quadrante")
else:
    print("O ponto está no eixo ou na origem")
'''

# Usando match

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

match (x, y):
    case (a, b) if a > 0 and b > 0:
        print("Primeiro Quadrante")
    case (a, b) if a < 0 and b > 0:
        print("Segundo Quadrante")
    case (a, b) if a < 0 and b < 0:
        print("Terceiro Quadrante")
    case (a, b) if a > 0 and b < 0:
        print("Quarto Quadrante")
    case _:
        print("O ponto está no eixo ou na origem")
