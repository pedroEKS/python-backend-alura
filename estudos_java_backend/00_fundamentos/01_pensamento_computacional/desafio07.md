# Desafio: Verificação de desconto

Você está desenvolvendo o sistema de bilheteria para um cinema. Os clientes podem ter direito a meia-entrada em duas situações:

* Se tiverem menos de 18 anos
* **OU**
* Se forem estudantes

Sua tarefa é criar um algoritmo em linguagem natural ou gráfica (usando fluxogramas, por exemplo) que avalie as informações do cliente e exiba uma mensagem indicando se ele tem ou não direito ao desconto.

---

## Regras de negócio

O cliente terá acesso à meia entrada se:

1. Tiver menos de 18 anos; **OU**
2. For estudante.

## Algoritmo

1. Recebe o nome do cliente e armazena na variável string `nomeCliente`.
2. Pergunta a idade e armazena na variável inteira `idade`.
3. Pergunta se é estudante e armazena na variável booleana `eEstudante`.
4. **SE** `idade < 18` **OU** `eEstudante`:
    * **ENTÃO** exibe: "Olá ${nomeCliente}! Você tem direito à meia entrada. Uhul! \o/"
    * **SENÃO** exibe: "Olá ${nomeCliente}! Que pena, infelizmente você não tem direito à meia entrada. :("

---

## Fluxograma

```text
            ( INÍCIO )
                |
                v
     [ Pergunta nome do cliente ]
                |
                v
    / Armazena var "nomeCliente" /
                |
                v
       [ Pergunta a idade ]
                |
                v
      / Armazena var "idade" /
                |
                v
     [ Pergunta se é estudante ]
                |
                v
    / Armazena var "eEstudante" /
                |
                v
          /-------------\
          | IDADE < 18  |
          |     OU      |
          | eEstudante? |
          \-------------/
            /         \
         SIM           NÃO
         /               \
        v                 v
[Exibe msg:             [Exibe msg:
 "Tem direito!           "Não tem direito
 Uhul! \o/"]              à meia entrada :("]
        |                  |
        |                  |
        +--------> <-------+
                 |
                 v
              ( FIM )