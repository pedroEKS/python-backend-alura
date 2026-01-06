# Desafio: Conversor de Moedas

Você está desenvolvendo um sistema de apoio para uma agência de viagens. Uma das funcionalidades mais solicitadas é um conversor de moedas. O usuário informa um valor em reais (R$) e o sistema precisa mostrar quanto isso representa em dólares (US$), usando uma taxa de câmbio definida pela empresa.

**Tarefa:**
Sua tarefa é criar um algoritmo em linguagem natural que use uma função para fazer essa conversão. A função deve receber o valor em reais e a taxa de câmbio como entrada, e retornar o valor convertido.

---

```
 R = 0
    Valor_ptax = 0
    
    funcao converterRparaUSD(reais):
        retornar (Reais / valor_ptax)
        
    //programa principal
    exibir "Conversor de Moedas"
    
    // receber dados do usuário
    exibir "Informe o valor em R$"
    R = ler do usuario
    
    // receber tx de conversão
    exibir "Informe o valor PTAX"
    valor_ptax = ler do usuario
    
    f = converterRparaUSD(R)
    
    exibir "Valor em USD:" + "USD" + R

```
