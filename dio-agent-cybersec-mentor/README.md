# 🛡️ dio-agent-cybersec-mentor

> O [DIO Agent](https://github.com/digitalinnovationone/dio-agent) especializado em **cibersegurança**: um mentor que analisa uma vulnerabilidade do jeito que um profissional de segurança faria.

Projeto do desafio da DIO de evoluir o DIO Agent usando apenas arquivos. **Nenhum modelo é treinado**: o agente aprende pelo que está escrito em Markdown.

## 🎯 A especialização e por quê

Em vez de responder direto ("isso é SQL Injection, use consulta parametrizada"), o agente agora:

1. **pergunta o contexto** antes de agir (ambiente, exposição, dados, defesas);
2. **avalia impacto, probabilidade e severidade**;
3. **orienta a correção** sem entregar tudo pronto;
4. **valida** se a falha foi mitigada.

Escolhi essa especialização porque a mesma falha pode ter gravidade muito diferente conforme o contexto, e entender isso é a base do trabalho de segurança. Também combina com a minha formação em Cibersegurança e meu interesse em engenharia de IA.

## 📁 O que foi criado ou alterado

| Arquivo | Tipo | O que faz |
| --- | --- | --- |
| `skills/vulnerability-analysis/SKILL.md` | novo | O roteiro de 8 passos que o agente segue |
| `skills/vulnerability-analysis/README.md` | novo | Explica a skill para pessoas |
| `skills/vulnerability-analysis/report-template.md` | novo | Formato fixo de relatório (a melhoria escolhida) |
| `agent/knowledge/security-basics.md` | novo | Vulnerabilidade, ameaça, risco, tríade CIA, severidade, referências e boas práticas |
| `agent/persona.md` | alterado | Seção "Postura em cibersegurança" |
| `AGENTS.md` | alterado | Nova linha na tabela de skills, novo arquivo de conhecimento e regra de ética |
| `lab/app.py` e `lab/app_corrigido.py` | novos | Login vulnerável e versão corrigida, para teste |
| `lab/README.md` | novo | Como usar o laboratório |
| `docs/cenarios-de-teste.md` | novo | Prompts para testar a skill |

## ⭐ A melhoria escolhida: saída padronizada

Toda análise termina no mesmo formato (`report-template.md`), com **impacto, probabilidade e severidade**, o que permite comparar casos diferentes lado a lado. A severidade é obtida por uma matriz didática de impacto × probabilidade (em `security-basics.md`), e o agente precisa mostrar o raciocínio.

## ▶️ Como rodar

1. Instale o **Hermes** seguindo a documentação oficial: <https://hermes-agent.nousresearch.com/docs>
2. Baixe o projeto:
   ```
   git clone https://github.com/SEU-USUARIO/dio-agent-cybersec-mentor.git
   ```
3. Abra o terminal **dentro da pasta do projeto** e rode:
   ```
   cd dio-agent-cybersec-mentor
   hermes
   ```
   Se o `hermes` for aberto em outra pasta, ele não encontra os arquivos do agente.
4. Converse. Exemplos em [`docs/cenarios-de-teste.md`](docs/cenarios-de-teste.md).

O projeto também funciona em outros harnesses compatíveis com `AGENTS.md`.

## 🧪 Laboratório

O [`lab/`](lab/README.md) tem um login vulnerável (`app.py`) e a versão corrigida (`app_corrigido.py`), em Python com SQLite. Todos os testes usam **apenas código e servidores meus, de laboratório**.

## 🗂️ Estrutura

```
dio-agent-cybersec-mentor/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── agent/
│   ├── persona.md
│   └── knowledge/
│       ├── dio-platform.md
│       ├── learning-experiences.md
│       └── security-basics.md        (novo)
├── skills/
│   ├── study-plan/
│   ├── unblock-challenge/
│   ├── explain-concept/
│   ├── web-search/
│   └── vulnerability-analysis/       (novo)
├── lab/
│   ├── README.md
│   ├── app.py
│   └── app_corrigido.py
└── docs/
    ├── glossary.md
    └── cenarios-de-teste.md
```

## ⚠️ Aviso

Projeto educacional. Use somente em ambientes próprios ou de laboratório. Testar sistemas de terceiros sem autorização é crime.

## 🙏 Créditos

Base: [digitalinnovationone/dio-agent](https://github.com/digitalinnovationone/dio-agent).

<!--
Depois de tirar os prints, crie a pasta prints/ e adicione aqui uma seção "Evidências" com:
- a análise do app.py pelo agente;
- as perguntas de contexto que ele faz;
- (opcional) a mesma pergunta num chat genérico, para comparação.
-->
