# Desafio: Automatizando tarefas

## O Cenário

Você está trabalhando como pessoa desenvolvedora júnior em uma equipe que está criando um sistema para auxiliar no controle de presença em eventos online. O time precisa de um algoritmo que processe a lista de participantes e envie um e-mail de agradecimento apenas para quem participou de toda a transmissão ao vivo.

> "Queremos automatizar o envio de agradecimentos. Mas só para quem assistiu à transmissão do início ao fim. Você consegue organizar esse processo em um algoritmo?"

## Racional da Solução

Em vez de contar o tempo por participante, a solução foca na checagem do tempo inicial e final, criando listas para comparação posterior. Em caso de maior rigor, poderia ser criada uma checagem intermediária no meio da transmissão. Essa abordagem simplifica o uso lógico, evitando múltiplas vias condicionais complexas e focando em uma lógica consequencial afirmativa.

## Algoritmo Proposto

Dados de entrada necessários
1. Lista de participantes contendo:
    Nome (ou identificador)
    E-mail
2. Duração total da transmissão (tempo total do evento)
3. Registro de presença na transmissão para cada participante:
    Horário de entrada
    Horário de saída

Passo a Passo (Linguagem Natural)

Início
    Obter a duração total esperada da transmissão.
    Obter a lista de participantes com seus dados e registros de logs.

Processamento
    Para cada participante na lista:
        Verificar se o participante possui um e-mail válido.
        Se não tiver e-mail válido:
            Pular para o próximo participante.
        
        Calcular o tempo de permanência:
            Subtrair o Horário de Entrada do Horário de Saída.
        
        Verificar condição de presença completa:
            Se o tempo de permanência for igual ou superior à duração total da transmissão:
                Marcar participante com status "Presença Completa".
            Senão:
                Marcar participante com status "Presença Incompleta".
    Fim 

Ação Final
    Para cada participante marcado como "Presença Completa":
        Disparar envio de e-mail de agradecimento.
    
    Encerrar o processo.

Saída Esperada
    Confirmação de e-mails enviados exclusivamente para os participantes que acompanharam o evento integralmente.