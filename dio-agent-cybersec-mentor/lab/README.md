# Laboratório

Código de estudo, **seu e local**, usado para testar a skill `vulnerability-analysis`.

| Arquivo | O que é |
| --- | --- |
| `app.py` | Login vulnerável a SQL Injection (propositalmente) |
| `app_corrigido.py` | Mesma lógica com consulta parametrizada |

## Rodando

```
python lab/app.py
python lab/app_corrigido.py
```

Só precisa do Python 3 (usa o módulo `sqlite3`, que já vem com ele). O banco é em memória e some ao fechar.

## Roteiro de teste com o agente

1. Peça ao agente, como especialista em AppSec, que analise o `app.py`. Ele deve perguntar o contexto antes de concluir.
2. Observe se ele identifica a falha, explica a causa raiz, cita a técnica do MITRE ATT&CK e avalia impacto, probabilidade e severidade.
3. Tente corrigir por conta própria, depois compare com o `app_corrigido.py`.
4. Peça uma nova análise do código corrigido para validar a mitigação.
5. Repare que o agente deve apontar um segundo problema: a senha guardada em texto puro.

Para provar a falha no seu laboratório, digite `admin' --` no campo de usuário e qualquer coisa na senha: no `app.py` o login passa (o `--` comenta o resto da consulta, incluindo a verificação da senha); no `app_corrigido.py` ele deve falhar.
