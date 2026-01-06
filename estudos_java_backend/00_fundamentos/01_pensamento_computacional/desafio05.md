# Desafio: Classificando Desempenho Acadêmico

## O Cenário

Você está trabalhando no desenvolvimento de um sistema educacional que precisa exibir mensagens personalizadas para estudantes com base em sua média final. A regra de negócio definida pela equipe pedagógica é a seguinte:

- Média menor que 5,0: mensagem "Você está reprovado."
- Média entre 5,0 e 6,9: mensagem "Você está de recuperação."
- Média 7,0 ou mais: mensagem "Parabéns! Você foi aprovado."

## Algoritmo Proposto

Abaixo está a estrutura lógica para o processo de verificação e decisão:

```
Receber os dados das notas do aluno
Calcular a média final

Definir as mensagens personalizadas do sistema:
    Mensagem_Reprovado: "Você está reprovado"
    Mensagem_Recuperacao: "Você está em recuperação"
    Mensagem_Aprovado: "Parabéns! Você está aprovado"

Verificar a condição da média:
    Se a média for menor que 5.0:
        Exibir Mensagem_Reprovado
    
    Senão, Se a média estiver entre 5.0 e 6.9:
        Exibir Mensagem_Recuperacao
    
    Senão (para médias de 7.0 ou superiores):
        Exibir Mensagem_Aprovado
    Fim
```
