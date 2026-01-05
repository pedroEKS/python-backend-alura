# Desafio: Calculadora de Despesas

## O Cenário

Você está desenvolvendo um sistema simples de controle financeiro pessoal. Uma das funcionalidades é permitir que o usuário informe diversas despesas do mês (como mercado, transporte, lazer etc.), e ao final, o sistema deve apresentar o total gasto.

Sua tarefa é criar um algoritmo, em linguagem natural, que represente a seguinte lógica: o sistema deve somar automaticamente todos os valores informados pelo usuário.

## Estrutura da Solução

### Dados de Apoio

Objetivo
Sistema simples de controle financeiro pessoal.

Decomposição do Problema
- Informar diversas despesas do mês
- Categorizar as despesas (mercado, transporte, lazer)
- Informar o total gasto

Padronização de Parâmetros
- Categoria (nome da despesa)
- Valor

### Algoritmo Proposto

Fluxo em formulário multipáginas:

Início
    1. Entrada de Dados
        1.1. O usuário cadastra o nome da despesa
        1.2. O usuário cadastra o valor da despesa

    2. Verificação de Continuidade
        1.3. O usuário deseja cadastrar mais despesas?
        
        Se SIM:
            Retornar ao passo 1.1 (Repetir o loop)
        
        Se NÃO:
            1.3.2.1. O sistema processa a soma de todos os valores cadastrados
            1.3.2.2. O sistema exibe o valor total das despesas do mês na tela
Fim

### Melhorias Futuras
Para versões futuras, planeja-se incluir relatórios por categoria, permitindo ao usuário visualizar não apenas o total geral, mas também o discriminado de quanto foi gasto em cada área (ex: quanto foi gasto apenas com Transporte).