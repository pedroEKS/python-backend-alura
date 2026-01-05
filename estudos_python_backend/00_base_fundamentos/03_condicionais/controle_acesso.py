'''
Mariana é responsável por liberar o acesso ao escritório e precisa de um 
programa que verifique se os funcionários podem entrar. Para isso, ela 
usará o horário atual. O escritório só permite acesso entre 8h e 18h. 
Crie um programa que receba a hora atual como entrada (em formato de 24 horas) 
e exiba uma mensagem informando se o acesso é permitido ou negado.
'''

# Recebe a hora atual
hora = int(input("Digite a hora atual (formato 24h): "))

# Verifica se está dentro do horário permitido
if hora >= 8 and hora <= 18:
    print("Acesso permitido ao escritório.")
else:
    print("Acesso negado. Fora do horário permitido.")
