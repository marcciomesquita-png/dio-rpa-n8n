# Automação com n8n — desafios da DIO

Entregas do bootcamp **Santander 2026 — Automação com N8N**, da [DIO](https://www.dio.me).

## Conteúdo

| Arquivo | O que é |
| --- | --- |
| [`desafio-criativo-prompt.md`](desafio-criativo-prompt.md) | **Desafio Criativo** — construção, passo a passo, de um prompt para planejar uma automação no n8n |
| [`scripts/teste_ponte.py`](scripts/teste_ponte.py) | Teste da ponte entre o n8n e um script Python, usando o nó **Execute Command** |

## Sobre a ponte com Python

O n8n tem um runner nativo de Python, mas ele só existe na distribuição Docker: a instalação via
npm não traz o pacote `@n8n/task-runner-python`. Em uma instalação local no Windows, o caminho que
funciona é o nó **Execute Command**, chamando o interpretador do sistema e trocando dados por
`stdin` e `stdout` em JSON.

O `teste_ponte.py` existe para provar esse contrato antes de depender dele. Ele lê o `stdin`,
tolera entrada vazia, aceita texto que não seja JSON e devolve sempre um JSON válido.

⚠️ Um detalhe que custa tempo quando aparece: no Windows, o PowerShell escreve um **BOM** (`﻿`)
na frente do que manda pelo pipe, e o `json.loads` falha com uma mensagem que não ajuda. O script
remove o BOM antes de interpretar.
