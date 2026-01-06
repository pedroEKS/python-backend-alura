# Desafio: Calculando Pedidos

## O Cenário

Você está desenvolvendo uma funcionalidade para um aplicativo de lanchonete. O sistema precisa calcular o valor total de um pedido com base na quantidade de itens solicitados (Hambúrguer, Batata frita e Refrigerante).

## Algoritmo Corrigido

Abaixo está a estrutura lógica organizada para garantir o cálculo correto, definindo constantes de preço e variáveis de quantidade.

```
    1. Definição de Variáveis (Tabela de Preços)
         PRECO_HAMBURGUER ← 12.00
         PRECO_BATATA ← 7.00
         PRECO_REFRI ← 5.00
    
    2. Entrada de Dados
         Escrever "Digite seu nome:"
         Ler nomeCliente
         Escrever "Quantos hambúrgueres você deseja?"
         Ler qtdHamburguer
         Escrever "Quantas batatas fritas você deseja?"
         Ler qtdBatata
         Escrever "Quantos refrigerantes você deseja?"
         Ler qtdRefri
    
    3. Processamento (Cálculo dos subtotais e total)
         subtotalHamburguer ← qtdHamburguer × PRECO_HAMBURGUER
         subtotalBatata ← qtdBatata × PRECO_BATATA
         subtotalRefri ← qtdRefri × PRECO_REFRI
         valorTotal ← subtotalHamburguer + subtotalBatata + subtotalRefri
    
    4. Saída de Dados
         Exibir "Olá, " + nomeCliente
         Exibir "O valor total do seu pedido é: R$ " + valorTotal
```
