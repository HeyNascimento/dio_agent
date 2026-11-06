# Fundamentos de segurança da informação

Base de conhecimento usada pela skill `vulnerability-analysis`. Consulte quando a conversa envolver segurança.

## Conceitos-chave

- **Ativo:** qualquer coisa que tenha valor e precise ser protegida (dados, sistemas, servidores, a reputação de uma empresa).
- **Vulnerabilidade:** uma fraqueza em um ativo (um erro de código, uma configuração insegura, um serviço sem atualização) que pode ser explorada.
- **Ameaça:** algo ou alguém que pode se aproveitar de uma vulnerabilidade e causar dano (um atacante, um malware, até um erro humano).
- **Exploração:** o ato de aproveitar uma vulnerabilidade. Um *exploit* é a técnica ou ferramenta usada para isso.
- **Risco:** a chance de uma ameaça explorar uma vulnerabilidade somada ao dano que isso causaria. De forma didática: risco = probabilidade × impacto.
- **Controle (ou mitigação):** o que reduz o risco (correção, firewall, monitoramento, treinamento).

Analogia: a vulnerabilidade é uma janela destrancada, a ameaça é alguém que pode entrar por ela, e o risco é o quanto isso importa (a casa está cheia de objetos de valor? está numa rua movimentada?).

## A tríade CIA

| Pilar | Pergunta que ele responde | Exemplo de quebra |
| --- | --- | --- |
| **Confidencialidade** | Só quem deve ver, vê? | Vazamento de dados de clientes |
| **Integridade** | Os dados estão corretos e sem alteração indevida? | Alguém altera um valor no banco |
| **Disponibilidade** | O sistema está disponível quando precisa? | Ataque que derruba o serviço, ransomware |

Ao avaliar o impacto de uma falha, pergunte qual desses três pilares ela afeta.

## Severidade, probabilidade e risco

- **Severidade** é a gravidade da falha em si. Padrões como o **CVSS** atribuem uma nota de 0.0 a 10.0, com faixas: Baixa (0.1 a 3.9), Média (4.0 a 6.9), Alta (7.0 a 8.9) e Crítica (9.0 a 10.0).
- **Probabilidade** é o quão provável é a exploração naquele ambiente.
- **Risco** é o que sobra quando você combina tudo com o contexto. Uma falha de severidade alta pode ter risco baixo num ambiente isolado.

Matriz didática simplificada (não substitui o CVSS):

| Impacto \ Probabilidade | Baixa | Média | Alta |
| --- | --- | --- | --- |
| **Baixo** | Baixa | Baixa | Média |
| **Médio** | Baixa | Média | Alta |
| **Alto** | Média | Alta | Crítica |

## Identificadores e referências

- **CVE:** número único de uma vulnerabilidade conhecida e pública (formato CVE-ANO-NÚMERO). Consulta: nvd.nist.gov.
- **CWE:** catálogo de *tipos* de fraqueza de software. Exemplo: CWE-89 é SQL Injection. Consulta: cwe.mitre.org.
- **CVSS:** sistema de pontuação da severidade. Consulta: first.org/cvss.
- **OWASP Top 10:** lista das categorias mais críticas de risco em aplicações web, entre elas a categoria *Injection*. Consulta: owasp.org.
- **MITRE ATT&CK:** base de conhecimento de táticas (o objetivo do atacante) e técnicas (como ele alcança o objetivo). Consulta: attack.mitre.org. Exemplo: a técnica T1190, *Exploit Public-Facing Application*, cobre a exploração de aplicações expostas, incluindo SQL Injection.

Regra: se não tiver certeza de um identificador, diga isso e mande conferir na fonte. Nunca invente.

## SQL Injection, resumindo

Acontece quando uma aplicação monta um comando SQL juntando texto digitado pelo usuário, de modo que a entrada pode mudar o significado do comando. Afeta principalmente confidencialidade e integridade (e, em alguns casos, disponibilidade).

Correções, da mais importante para as complementares:

1. **Consultas parametrizadas** (prepared statements): a entrada vai separada do comando e é tratada sempre como dado.
2. Validação de entrada como camada extra, nunca como única defesa.
3. Privilégio mínimo para a conta do banco usada pela aplicação.
4. Não exibir mensagens de erro detalhadas ao usuário e manter logs.
5. Armazenar senhas com hash forte e salt (bcrypt, scrypt ou Argon2), nunca em texto puro.

## Servidor Linux exposto: o que verificar

Perguntas de contexto: distribuição e versão, serviços rodando, como é o acesso remoto (SSH com senha ou chave), existe firewall, quem tem acesso de administrador, quando foi a última atualização.

Pontos de atenção comuns: serviços desnecessários escutando em portas abertas, SSH com senha fraca ou login direto como root, pacotes desatualizados, firewall desativado, ausência de logs e backups.

Comandos de leitura úteis em laboratório (apenas consultam): `ss -tulpn` (portas em escuta), `sudo ufw status` (firewall, quando usa UFW), `apt list --upgradable` (atualizações pendentes). Explique o que cada um mostra antes de pedir que o estudante rode.

## Boas práticas gerais

- **Defesa em profundidade:** várias camadas, para que uma falha isolada não derrube tudo.
- **Privilégio mínimo:** cada pessoa e cada serviço com apenas o acesso de que precisa.
- **Manter tudo atualizado** e remover o que não é usado.
- **Autenticação forte:** senhas longas, gerenciador de senhas e MFA.
- **Segredos fora do código:** chaves e senhas nunca vão para o repositório.
- **Logs e monitoramento:** o que não é registrado não é investigado.
- **Backups testados**, de preferência isolados.
- **Segurança desde o início do desenvolvimento** (ideia do DevSecOps): revisar mudanças antes de ir para produção.

## Ética e lei

Teste apenas o que é seu ou o que você tem autorização por escrito para testar. No Brasil, invadir dispositivo informático alheio é crime (art. 154-A do Código Penal, incluído pela Lei 12.737/2012). Laboratório próprio é o caminho seguro para praticar.
