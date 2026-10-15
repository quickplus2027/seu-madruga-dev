<p align="center">
  <img src="branding/seu-madruga-dev-mark1.png" alt="Banner SeuMadruga.dev" width="100%">
</p>

<h1 align="center">SeuMadruga.dev</h1>
<p align="center"><strong>Token não dá em árvore.</strong></p>
<p align="center">Uma Skill aberta para Claude Code e OpenAI Codex · <strong>Por Rômulo Bezerra</strong></p>

## Instalação rápida

```bash
npx skills add quickplus2027/seu-madruga-dev --skill seu-madruga-dev
```

> O instalador `npx` pode obter e executar código externo. Confira o repositório e o instalador antes de utilizá-lo. Também é possível instalar a pasta [`skills/seu-madruga-dev`](skills/seu-madruga-dev) manualmente conforme a documentação do seu agente.


## Como usar sem decorar comandos

**Basta conversar com o agente depois de instalar a Skill.** Exemplos de pedidos:

- **"Seu Madruga, confira o que mudou no projeto."** O agente identifica alterações e propõe verificações direcionadas. Se tiver acesso às ferramentas, executa verificações autorizadas e relata o que realmente examinou.
- **"Seu Madruga, prepare este projeto para usar suas regras."** O agente inspeciona as configurações e apresenta uma prévia. **Só modifica arquivos depois de você aprovar.**
- **"Seu Madruga, esse design está ruim. Avalie e proponha melhorias."** O agente consulta as diretrizes visuais pertinentes e avalia resultados reais quando possível.
- **"Seu Madruga, estou gastando muitos tokens."** O agente avalia contexto, estratégia, tarefas e modelo disponível, sem inventar métricas.
- **"Seu Madruga, as regras estão sendo ignoradas."** O agente verifica a instalação e distingue presença dos arquivos de cumprimento real das instruções.

**Importante:** instalar uma Skill não garante que o agente a carregue em todas as tarefas. Se necessário, invoque `seu-madruga-dev` explicitamente e configure, mediante aprovação, as regras persistentes no projeto. Veja [Ativação guiada](docs/ACTIVATION.md).

## Verificações de qualidade sem complicação

O agente pode utilizar as verificações de arquivos alterados, escrita e acessibilidade HTML disponíveis no projeto. Essas verificações são **limitadas**: não equivalem a auditoria WCAG, teste visual completo ou prova de economia de tokens. As ferramentas opcionais estão documentadas em [Quality Gates para mantenedores](docs/QUALITY_GATES.md); usuários comuns não precisam decorar seus parâmetros.

## O que é o SeuMadruga.dev?

É um **conjunto de instruções para assistentes de programação**. Ele orienta o Claude Code e o Codex a selecionar a quantidade necessária de contexto, planejar tarefas complexas, sugerir modelos adequados e executar testes proporcionais às alterações.

**Não é um modelo de IA novo, um aplicativo em segundo plano ou um contador automático de tokens.** É uma Skill: o agente lê orientações e decide como aplicá-las às tarefas, dentro das capacidades e permissões da ferramenta utilizada.

## Para que isso é útil?

| Situação do dia a dia | O que a Skill orienta o agente a fazer |
| --- | --- |
| Você pede para corrigir uma função pequena | Localizar primeiro os arquivos relacionados, em vez de ler o projeto inteiro. |
| Você pede uma reformulação grande | Propor um plano e pedir aprovação antes de alterar vários módulos. |
| Você pede uma tarefa grande que poderia envolver vários agentes | Decidir se paralelizar ajuda de verdade; usar apenas os agentes necessários, evitando repetir leituras ou editar os mesmos arquivos ao mesmo tempo. |
| A conversa começa a ficar longa | Sugerir inspecionar o contexto disponível e realizar um handoff, compactação ou nova sessão, conforme o agente. |
| O agente quer usar o modelo mais caro para tudo | Recomendar um modelo e nível de raciocínio proporcionais à dificuldade; a troca depende do usuário e da ferramenta. |
| Você muda um componente | Rodar primeiro testes afetados, ampliando para integração e suíte completa quando o risco exigir. |
| Você encontra uma Skill externa no GitHub | Avaliar origem, manutenção, comandos, permissões e riscos antes de recomendar instalação. |
| O agente repete buscas ou comandos sem progresso | Reavaliar a abordagem e aproveitar descobertas já documentadas. |
| Builds, testes ou caches estão enchendo seu perfil do Windows | Avaliar os caminhos utilizados, priorizar ajustes locais e pedir aprovação antes de mover ou apagar qualquer arquivo. |

**Exemplo prático:** se você pedir “corrija a validação do campo de e-mail”, a orientação é localizar esse componente e seus testes, propor uma alteração mínima e validar o comportamento afetado. Se o código modificar autenticação ou permissões, a própria regra determina uma verificação mais ampla por risco.

## Frontend, Design e UX: inovação visual com propósito

Para tarefas de interface, o SeuMadruga.dev também orienta o agente a definir uma **direção artística própria**, melhorar navegação e hierarquia, considerar microinterações, componentes interativos, gráficos exploráveis e, quando justificado, experiências 3D. **Não ativa todas as tecnologias ao mesmo tempo:** escolhe somente o que agrega valor real, respeitando desempenho, acessibilidade, celulares e a arquitetura existente.

**Exemplo:** ao criar um dashboard, o agente deve pensar em informações progressivas, filtros claros, tooltips úteis e gráficos compreensíveis, em vez de simplesmente instalar uma biblioteca 3D. A diretriz é aplicada **somente em tarefas visuais**, preservando tokens nas demais. [Veja VISUAL INNOVATION FIRST](skills/seu-madruga-dev/references/visual-excellence.md). A direção visual tem módulos independentes para [Design System](skills/seu-madruga-dev/references/visual-design-system.md), [UX](skills/seu-madruga-dev/references/visual-ux-interactions.md), [Motion](skills/seu-madruga-dev/references/visual-motion.md), [3D](skills/seu-madruga-dev/references/visual-3d-immersive.md), [Dados e Mapas](skills/seu-madruga-dev/references/visual-data-geospatial.md) e [Performance](skills/seu-madruga-dev/references/visual-performance-quality.md).

## Como decide usar um ou vários agentes?

A regra é **começar com um agente**. Para tarefas maiores, a Skill propõe uma classificação de cinco níveis (simples, moderado, complexo, crítico e estratégico) e só considera múltiplos agentes quando as atividades podem ser separadas sem conflito. O limite sugerido é de até quatro agentes para trabalhos estratégicos, **não uma obrigação de usar quatro**. A ferramenta precisa oferecer esse recurso; a Skill não cria agentes por conta própria. [Leia as regras de orquestração](skills/seu-madruga-dev/references/orchestration.md).

**Exemplo:** mudar a cor de um botão não precisa de vários agentes. Refatorar módulos independentes pode justificar delegação, mas só depois de comparar coordenação, risco e trabalho duplicado.

## O que muda e o que não muda

**Ela pode ajudar a:** organizar sessões, evitar leituras redundantes, solicitar planejamento antes de mudanças complexas, produzir resumos de continuidade, escolher testes por impacto e reduzir trabalho desnecessário. Também orienta como diagnosticar desperdício de disco, CPU, RAM e arquivos temporários sem colocar outros projetos em risco.

**Ela não:**
- Garante determinada porcentagem de economia nem um resultado mais barato em toda tarefa.
- Mede o consumo de tokens em tempo real sem suporte da ferramenta.
- Altera modelos, permissões, configurações ou modos automaticamente em todas as plataformas.
- Substitui testes de segurança, revisão humana ou verificações completas exigidas em releases e mudanças críticas.
- Instala outras Skills ou executa alterações destrutivas sem a autorização adequada.
- Limpa automaticamente seu Windows, movimenta caches globais, altera variáveis do sistema ou garante acelerar o computador.

## Proteção do ambiente: seu computador também importa

Economizar tokens não adianta se o projeto deixar seu computador lento ou encher o perfil do sistema com arquivos gerados. Quando a tarefa envolve **caches, builds, temporários ou consumo de recursos**, a Skill recomenda investigar primeiro, usar caminhos configuráveis **por projeto** e proteger dados, perfis e configurações existentes.

**Exemplo:** se o `node_modules` ou os artefatos de teste ocuparem muito espaço, a Skill sugere medir a origem do problema e apresentar opções reversíveis. Ela **não exclui pastas**, **não altera o cache global** e **não presume que você tenha unidade `D:`**. Leia a [diretriz específica](skills/seu-madruga-dev/references/environment-efficiency.md).

## Como começar a usá-la

Depois de instalada e reconhecida pelo seu agente, você pode pedir:

> Use a Skill `seu-madruga-dev` nesta tarefa. Primeiro identifique o escopo mínimo, diga se precisamos de um plano aprovado e proponha apenas os testes necessários, ampliando-os se houver riscos. Não altere arquivos ainda.

Os comandos de sessão variam entre produtos e versões. Por exemplo, `/context`, `/compact` e `/clear` são referências de fluxos do Claude Code quando disponíveis; não presuma que esses comandos existam no Codex. Consulte a [compatibilidade](docs/COMPATIBILITY.md).

## Transparência e confiança

- **Código e instruções abertos:** leia o ponto de entrada [`SKILL.md`](skills/seu-madruga-dev/SKILL.md) e os módulos em [`references/`](skills/seu-madruga-dev/references/).
- **Sem serviço próprio ou API paga:** a Skill é composta por arquivos locais; a instalação e o agente utilizado podem ter seus próprios custos e requisitos.
- **Sem coleta de dados própria:** os arquivos da Skill não implementam telemetria; as políticas do Claude Code, Codex, GitHub e instaladores usados são independentes.
- **Testes existentes:** verificações estruturais offline e testes unitários simples. Isso **não** equivale a auditoria de segurança nem demonstra economia de tokens.
- **Evidências futuras:** medições devem comparar a mesma tarefa com e sem Skill, incluindo consumo, custo, tempo e qualidade. Veja [`EVALUATION.md`](EVALUATION.md).
- **Status:** **v0.4.0 experimental**, sem benchmarks públicos conclusivos de redução de tokens.

## In English

**SeuMadruga.dev** is an open-source Agent Skill that guides Claude Code and OpenAI Codex toward leaner context retrieval, approval-first planning for complex changes, risk-based targeted testing, session handoffs, optional multi-agent orchestration, environment/profile protection and thoughtful model selection. It does not guarantee token savings, silently switch models, or run background monitoring. Read [`SKILL.md`](skills/seu-madruga-dev/SKILL.md) and [`SECURITY.md`](SECURITY.md) before installing.

## Projeto e créditos

**Criado por Rômulo Bezerra** · [GitHub quickplus2027](https://github.com/quickplus2027)

[Segurança](SECURITY.md) · [Avaliação e métricas](EVALUATION.md) · [Compatibilidade](docs/COMPATIBILITY.md) · [Contribuições](CONTRIBUTING.md) · [Licença MIT](LICENSE)

> Projeto independente, não afiliado à OpenAI, Anthropic ou aos titulares da série *Chaves*. Nome e imagens inspirados no personagem podem implicar direitos de terceiros; avalie permissões ou substituição do mascote antes de divulgação comercial. A licença MIT do código não concede direitos sobre marcas ou personagens de terceiros.

<p align="center">
  <img src="branding/seu-madruga-dev-mark.png" alt="Mascote SeuMadruga.dev" width="220">
</p>


## Ativação consistente por projeto
A instalação da Skill sozinha não torna as regras permanentes. Consulte [Ativação e diagnóstico](docs/ACTIVATION.md) para adicionar instruções preservando seus arquivos e auditar o resultado. O comando `doctor` não confirma que o modelo obedeceu às instruções.
