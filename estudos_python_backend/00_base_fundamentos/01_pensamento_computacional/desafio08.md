# Desafio: Calculando valor da entrega

Você está desenvolvendo um sistema para uma empresa de delivery. O valor da taxa de entrega depende da distância até o cliente e se o pedido foi feito em um dia de chuva.

**Regras:**
* Para entregas até 5 km, a taxa é R$ 5,00.
* Entre 5 e 10 km, a taxa é R$ 8,00.
* Acima de 10 km, a taxa é R$ 10,00.
* Se estiver chovendo, acrescenta R$ 2,00 à taxa padrão.

---

### Algoritmo em Pseudocódigo

```
    Declaração de variáveis
        REAL tx_de_entrega = 0
        INTEIRO distancia = 0
        BOOLEANO dia_chuva = FALSO
        
    Entrada de dados
        ESCREVA "Qual a distância em km?"
        LEIA distancia
        
        ESCREVA "Está chovendo? (VERDADEIRO/FALSO)"
        LEIA dia_chuva
        
    Lógica da Chuva (Adicional)
        SE dia_chuva ENTÃO
            tx_de_entrega = 2
        SENÃO
            tx_de_entrega = 0
        FIM_SE
            
    Lógica da Distância (Base)
        SE distancia <= 5 ENTÃO
            tx_de_entrega = tx_de_entrega + 5
            
        SENÃO SE distancia > 5 E distancia <= 10 ENTÃO
            tx_de_entrega = tx_de_entrega + 8

        SENÃO
            tx_de_entrega = tx_de_entrega + 10
        FIM_SE
            
    EXIBIR "Valor total da Entrega: R$ " + tx_de_entrega
```