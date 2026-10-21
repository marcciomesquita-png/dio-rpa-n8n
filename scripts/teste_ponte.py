"""
Teste de ponte n8n <-> Python.

Nao faz nada util de proposito. A unica coisa que este arquivo prova e o
CONTRATO: o no Execute Command do n8n consegue chamar o Python desta maquina,
mandar dados pela entrada padrao e receber JSON de volta pela saida padrao.

Se este teste passa, o item 9 do bootcamp (RPA com n8n e Python) e viavel
sem Docker e sem o task runner nativo.

Como o n8n vai chamar:
    python "C:\\Users\\tezzo\\Documents\\dio-rpa-n8n\\scripts\\teste_ponte.py"

Como testar na mao:
    echo {"nome": "Marccio"} | python scripts/teste_ponte.py
"""

import json
import platform
import sys
from datetime import datetime


def ler_entrada():
    """Le o que vier do n8n pela entrada padrao.

    O n8n manda o item como JSON. Quando nao vem nada (teste solto no
    terminal, ou no primeiro no do fluxo), devolve dicionario vazio em vez
    de quebrar.
    """
    bruto = sys.stdin.read() if not sys.stdin.isatty() else ""

    # O PowerShell carimba um BOM (﻿) na frente do que manda pelo pipe.
    # Invisivel na tela e o json.loads quebra nele. Tirar antes de qualquer coisa.
    bruto = bruto.lstrip("﻿").strip()

    if not bruto:
        return {}
    try:
        return json.loads(bruto)
    except json.JSONDecodeError:
        # Entrada que nao e JSON ainda e informacao: devolve como texto.
        return {"texto_bruto": bruto}


def main():
    entrada = ler_entrada()

    resposta = {
        "ponte": "ok",
        "quando": datetime.now().isoformat(timespec="seconds"),
        "python": platform.python_version(),
        "sistema": f"{platform.system()} {platform.release()}",
        "recebi": entrada,
    }

    # Uma linha de JSON na saida padrao. O n8n le isso e transforma em item.
    print(json.dumps(resposta, ensure_ascii=False))


if __name__ == "__main__":
    main()
