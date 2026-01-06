 # Desafio: Simulador de pedidos em uma cafeteria

 Você foi contratado por uma cafeteria que deseja automatizar o atendimento no balcão. O sistema deve permitir que o atendente registre os pedidos de cada cliente, calcule o valor total e aplique um desconto de 10% para clientes cadastrados.

**Regras:**
O processo deve funcionar da seguinte forma:

    O atendente informa quantos itens o cliente vai pedir.
    Para cada item, o sistema solicita o nome e o preço.
    Ao final, o sistema pergunta se o cliente é cadastrado.
    Se for, aplica o desconto e exibe o valor com desconto.
    Caso contrário, exibe o valor cheio.
---
O desafio consiste em criar um algoritmo que represente essa lógica de forma completa. 
---
```
item = NULL
qtde_item = 0
n=1
preco = 0
subtotal = 0
total = 0
cliente = TRUE
    
funcao aplicardescontocliente (C):
    retornar (subtotal * 0,10)
    
//programa principal
exibir "Sistema de Pedidos Cafeteria"

//receber dados
exibir "Informe a quantidade de ítens:"
qtde_item = ler do usuario

//Validação de entrada
SE qtde_item <= 0
    exibir "Dado Inválido. Informe a quantidade de ítens:"

//Loop para verificação dos ítens solicitados
ENQUANTO n <= qtde_item
    exibir "Informe o nome do produto:"
    item = ler do usuario
    
    exibir "Informe o valor:"
    preco = ler do usuario
    subtotal = subtotal + preco
    n = n+1
    
//Verificar se é cliente para aplicar o desconto
exibir "É cliente cadastrado?"
SE cliente 
    f = aplicardescontocliente (C)
    total = subtotal - f
    exibir "Valor do desconto:" + "R$" + f
    exibir "Valor total:" + "R$" + total
SE NÃO
    total = subtotal
    exibir "Valor total:" + "R$" + total"

    ```