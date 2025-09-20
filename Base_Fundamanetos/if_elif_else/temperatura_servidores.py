'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma 
sala de servidores não ultrapasse 25°C. Ele quer um programa que 
receba a temperatura atual como entrada e, se necessário, exiba 
uma mensagem de alerta.
'''

# Recebe a temperatura atual como entrada
temperatura = float(input("Digite a temperatura atual: "))

# Verifica se está acima do limite
if temperatura > 25:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print("Temperatura dentro do limite seguro.")

