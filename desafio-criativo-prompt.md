# Planejando uma automação no n8n com um bom prompt

Desafio Criativo do Bootcamp **Santander 2026 — Automação com N8N**, da DIO.

O exercício pede para construir, por etapas, um prompt capaz de orientar uma IA a planejar uma
automação no n8n. Este arquivo traz as três etapas e o prompt final.

**Caso escolhido:** triagem de solicitações que chegam por e-mail em uma caixa compartilhada.
Um processo comum, que quase toda equipe pequena faz à mão antes de automatizar.

---

## Passo 1 — A automação desejada

```text
Quero criar uma automação no N8N para triar solicitações que chegam por e-mail
em uma caixa compartilhada.

Público ou responsável:
Um time pequeno de atendimento que recebe pedidos de várias áreas e hoje faz a
triagem manualmente, lendo mensagem por mensagem.

Resultado esperado:
Cada solicitação classificada por urgência, registrada em uma planilha com a data
e a hora de entrada, encaminhada ao responsável certo, e com um aviso automático
de recebimento para quem abriu o pedido.
```

---

## Passo 2 — Contexto e regras

```text
Ferramentas envolvidas:
Gmail (caixa compartilhada), Google Sheets e Slack.

Fluxo desejado:
1. Detectar a chegada de um novo e-mail na caixa compartilhada.
2. Ler assunto e corpo e classificar a solicitação em uma de três urgências:
   alta, normal ou baixa.
3. Registrar uma linha na planilha com data e hora de entrada, remetente,
   assunto, urgência e responsável definido.
4. Notificar o responsável pela urgência no canal do Slack.
5. Responder ao solicitante confirmando o recebimento e informando o prazo
   previsto para aquela urgência.

Regras importantes:
- Ignorar mensagens automáticas e respostas de confirmação, para não abrir
  solicitação duplicada.
- Se o assunto ou o remetente estiverem vazios, registrar como urgência normal
  e marcar a linha para revisão humana, em vez de descartar.
- Gravar sempre a data e a hora de entrada, mesmo quando a classificação falhar:
  sem marca de entrada não há como medir o tempo de resposta depois.
- Uma solicitação nunca pode ser encerrada pela automação; ela só registra,
  encaminha e avisa.
```

---

## Passo 3 — Prompt final

```text
Atue como um especialista em N8N.

Crie uma automação para triar solicitações que chegam por e-mail em uma caixa
compartilhada.

Público:
Um time pequeno de atendimento que recebe pedidos de várias áreas e hoje faz a
triagem manualmente, lendo mensagem por mensagem.

Ferramentas envolvidas:
Gmail (caixa compartilhada), Google Sheets e Slack.

Fluxo:
1. Detectar a chegada de um novo e-mail na caixa compartilhada.
2. Ler assunto e corpo e classificar a solicitação em uma de três urgências:
   alta, normal ou baixa.
3. Registrar uma linha na planilha com data e hora de entrada, remetente,
   assunto, urgência e responsável definido.
4. Notificar o responsável pela urgência no canal do Slack.
5. Responder ao solicitante confirmando o recebimento e informando o prazo
   previsto para aquela urgência.

Regras:
- Ignorar mensagens automáticas e respostas de confirmação, para não abrir
  solicitação duplicada.
- Se o assunto ou o remetente estiverem vazios, registrar como urgência normal
  e marcar a linha para revisão humana, em vez de descartar.
- Gravar sempre a data e a hora de entrada, mesmo quando a classificação falhar:
  sem marca de entrada não há como medir o tempo de resposta depois.
- Uma solicitação nunca pode ser encerrada pela automação; ela só registra,
  encaminha e avisa.
- Se qualquer passo falhar, registrar o erro e seguir com os demais, em vez de
  interromper o fluxo inteiro.

Explique quais nós do N8N devem ser utilizados e a lógica de funcionamento do
workflow.
```

---

## Três escolhas de escrita, e por que elas estão aí

O modelo da DIO pede processo, público, ferramentas, fluxo e regras. Preencher os campos já
resolve o exercício. O que vem abaixo é a diferença entre um prompt que funciona e um prompt que
não deixa a IA escolher o caminho fácil.

**1. A exceção não descarta — ela marca.**
O caminho óbvio seria *"ignorar e-mails sem assunto"*. Mas um pedido sem assunto continua sendo um
pedido, e descartar em silêncio é como se perde trabalho sem ninguém notar. A regra escrita manda
**registrar como normal e marcar para revisão humana**. Custa uma linha no prompt e evita um buraco
invisível no fluxo.

**2. A marca de entrada é obrigatória mesmo quando o resto falha.**
Data e hora de entrada não são enfeite de registro: são o começo da contagem. Sem elas, não existe
tempo de resposta, não existe fila medida, não existe conversa sobre melhorar. Por isso a regra diz
*"mesmo quando a classificação falhar"* — a pior hora para perder o relógio é justamente quando
algo deu errado.

**3. A automação não encerra nada.**
Ela registra, encaminha e avisa. Encerrar continua sendo decisão de gente. Automação que fecha caso
sozinha some com o trabalho da vista — e o que some da vista não volta para a fila.

---

## O que o prompt tem além dos campos preenchidos

| Elemento | Onde aparece | Por que importa |
| --- | --- | --- |
| Papel | *"Atue como um especialista em N8N"* | define o vocabulário da resposta |
| Saída pedida | *"Explique quais nós e a lógica"* | pede o raciocínio, não só a lista de nós |
| Tratamento de erro | regra final | evita que uma falha derrube o fluxo inteiro |
| Limite explícito | *"nunca pode ser encerrada"* | diz à IA o que **não** fazer, que é o que normalmente falta |

Um prompt bom não é o mais detalhado — é o que remove a saída fácil.
