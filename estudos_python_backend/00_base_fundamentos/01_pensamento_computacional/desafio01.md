# Desafio: organizando o suporte ao cliente

## O Cenário

> **Demanda do time de Customer Success:**
> Precisamos melhorar a forma como lidamos com os pedidos de suporte dos usuários. As mensagens chegam com vários problemas misturados, como dificuldades para acessar o sistema, dúvidas sobre pagamento ou erros no uso de funcionalidades. Está tudo confuso e difícil de responder de forma ágil.

## Proposta de Solução

### 1. Decomposição

**Como decompor o problema macro em partes menores e gerenciáveis?**

- Criar uma **rede de categorias** para classificar os tipos de pedidos recebidos (ex: Financeiro, Técnico, Acesso)
- Estruturar uma **área dedicada de atendimento** ao cliente (Front-end/Interface)
- Desenvolver uma **base de conhecimento (FAQ)** para perguntas frequentes e métricas de avaliação da solução

### 2. Reconhecimento de Padrões

**É possível reconhecer padrões nos pedidos para prever soluções?**

**Sim.** Conforme os pedidos forem recebidos, resolvidos e avaliados, podemos implementar um sistema de **tags** para agrupar problemas similares e vincular soluções que já funcionaram anteriormente.

### 3. Abstração

**Que tipo de abstrações podem ser criadas para simplificar o fluxo, ignorando detalhes irrelevantes?**

Podemos filtrar o conteúdo das mensagens focando apenas em **palavras-chave** essenciais que definem a urgência e o tipo do problema:

- `erro`
- `falha`
- `lentidão`
- `crash`
- `pagamento`

### 4. Algoritmos

**É viável criar um algoritmo (passo a passo) para lidar com cada tipo de solicitação?**

- **Automação:** Implementar um chatbot de resposta automática que utilize IA para interpretar a dúvida e sugerir soluções baseadas na base de conhecimento
- **Escalonamento:** Criar um algoritmo de triagem onde, se a automação não resolver, o ticket é encaminhado automaticamente para um **SAC humano** especializado naquele tipo de problema