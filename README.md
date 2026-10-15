<p align="center"><img src="branding/ecosystem-v2/seu-madruga-core.webp" alt="SeuMadruga Ecosystem 2.0 — Capa Master CORE" width="100%"></p>

<h1 align="center">SeuMadruga Ecosystem 2.0</h1>
<p align="center"><strong>9 skills especializadas · Uma forma mais inteligente de organizar tarefas com IA</strong></p>
<p align="center"><strong>Idealizado e criado por Rômulo Bezerra</strong></p>

<p align="center"><a href="#visão-geral">Visão geral</a> · <a href="#-comece-aqui-instale-o-seumadruga-em-poucos-passos">🚀 Instale agora</a> · <a href="#as-nove-skills">As nove skills</a> · <a href="#exemplos-de-uso">Exemplos</a> · <a href="#validação-e-limites">Qualidade</a></p>

---

## Visão geral

O **SeuMadruga Ecosystem 2.0** reúne um núcleo de orquestração e oito especialidades que orientam agentes a trabalhar de maneira mais organizada em código, interface, segurança, motion, arquitetura, testes, inteligência artificial, dados e conteúdo. Você pode começar com uma skill ou combinar várias conforme a tarefa.

O sistema prioriza **resultado verificável e economia inteligente de contexto**, em vez de carregar todas as referências em toda solicitação. A skill original **SeuMadruga.dev** continua disponível e compatível.

### Princípios do ecossistema

1. **Objetivo antes de ferramenta:** descobrir o problema e o resultado desejado antes de escolher tecnologia.
2. **Contexto sob demanda:** ler arquivos e referências proporcionais ao risco e ao escopo.
3. **Experiência visual com propósito:** valorizar clareza, usabilidade, acessibilidade e boa direção artística.
4. **Segurança desde o planejamento:** não comprometer dados e permissões em nome da velocidade.
5. **Qualidade demonstrável:** distinguir verificações executadas, avisos e tarefas não testadas.
6. **Autoria e continuidade:** manter histórico, decisões e material do projeto original.

## 🚀 COMECE AQUI: Instale o SeuMadruga em poucos passos

**Nunca instalou uma skill? Sem problema.** Este tutorial ensina o básico, sem pressupor conhecimento de programação. Você pode instalar primeiro o **CORE** e, depois, adicionar as especialidades desejadas.

<p align="center"><strong>1. Prepare → 2. Instale → 3. Use → 4. Confira</strong></p>

### ✅ Antes de começar: o que você precisa?

- **Computador Windows, macOS ou Linux.** Os exemplos abaixo também funcionam em terminais integrados de editores, quando configurados.
- **Claude Code ou OpenAI Codex instalado e configurado.** Uma skill complementa o agente; não substitui o aplicativo.
- **Node.js e npm disponíveis**, para executar o instalador `npx`. Se já usa `npx`, pode seguir diretamente.

Não precisa baixar cada arquivo manualmente nem criar pastas à mão ao utilizar o instalador.

<details>
<summary><strong>🧩 Sou iniciante: onde digito os comandos?</strong></summary>

**Windows:** abra o menu Iniciar, procure **PowerShell** e abra o aplicativo. Se você usa o VS Code, também pode ir ao menu **Terminal → Novo Terminal**.

**macOS:** abra o aplicativo **Terminal**.

**Linux:** abra seu terminal habitual.

Digite os comandos no terminal, não na barra de endereços do navegador. Para verificar se o Node.js está disponível, execute:

```bash
node --version
npm --version
```

Se algum deles não funcionar, instale a versão LTS do [Node.js](https://nodejs.org/) e abra um novo terminal antes de tentar novamente.

</details>

### 📥 Passo 1. Instale o SeuMadruga CORE

Copie e cole este comando no terminal:

```bash
npx skills add quickplus2027/seu-madruga-dev --skill seu-madruga-core
```

O CORE é a especialidade central: ajuda a identificar o objetivo, avaliar o risco e selecionar instruções adequadas para cada tarefa.

**Durante a instalação:** o instalador pode pedir para escolher o agente, o local de instalação ou confirmar operações. Leia as opções e selecione o Claude Code ou Codex que realmente utiliza. Não aceite permissões ou execução de códigos desconhecidos sem revisar.

> **Atenção:** `npx skills` é um instalador de terceiros e pode obter/executar código externo. Confira sua procedência e as permissões solicitadas. O comando de instalação pode variar conforme a versão instalada; consulte [skills.sh](https://skills.sh/) para orientações atualizadas.

### 🎨 Passo 2. Escolha suas especialidades

**Quer melhorar interfaces?** Instale Design System:

```bash
npx skills add quickplus2027/seu-madruga-dev --skill design-system
```

**Quer revisar segurança?** Instale Cybersecurity:

```bash
npx skills add quickplus2027/seu-madruga-dev --skill cybersecurity
```

**Quer criar animações e vídeos?** Instale Motion Studio:

```bash
npx skills add quickplus2027/seu-madruga-dev --skill motion-studio
```

Você não precisa instalar as oito especialidades imediatamente. Escolha as que correspondem ao seu trabalho.

<details>
<summary><strong>📚 Ver comandos das nove skills</strong></summary>

| Skill | Comando de instalação |
| --- | --- |
| CORE | `npx skills add quickplus2027/seu-madruga-dev --skill seu-madruga-core` |
| Design System | `npx skills add quickplus2027/seu-madruga-dev --skill design-system` |
| Cybersecurity | `npx skills add quickplus2027/seu-madruga-dev --skill cybersecurity` |
| Motion Studio | `npx skills add quickplus2027/seu-madruga-dev --skill motion-studio` |
| Architecture | `npx skills add quickplus2027/seu-madruga-dev --skill architecture` |
| Quality Assurance | `npx skills add quickplus2027/seu-madruga-dev --skill quality-assurance` |
| AI Operations | `npx skills add quickplus2027/seu-madruga-dev --skill ai-operations` |
| Data Experience | `npx skills add quickplus2027/seu-madruga-dev --skill data-experience` |
| Content Studio | `npx skills add quickplus2027/seu-madruga-dev --skill content-studio` |

</details>

### 💬 Passo 3. Comece a utilizar no seu agente

Depois da instalação, abra uma nova sessão no Claude Code ou Codex, dentro do projeto em que deseja trabalhar, e experimente pedir:

> Use a skill **seu-madruga-core** neste projeto. Identifique meu objetivo, recomende as especialidades necessárias, mostre seu plano e não modifique arquivos sem minha aprovação.

**Para melhorar um site:**

> Use **design-system** para avaliar o frontend, a versão mobile, a navegação e a acessibilidade. Liste problemas, proponha soluções e mostre como validar o resultado.

**Para melhorar o código:**

> Use **quality-assurance** para identificar os testes necessários, revisar alterações e informar o que passou, falhou ou não foi executado.

**Para criar vídeos:**

> Use **motion-studio** para planejar um vídeo com Remotion. Comece definindo cenas, duração e roteiro antes de implementar.

### 🔍 Passo 4. Verifique se a instalação funcionou

Peça ao seu agente:

> Quais skills SeuMadruga você consegue descobrir nesta sessão? Mostre o caminho do `SKILL.md` de cada uma e explique como utilizaria uma delas na minha próxima tarefa.

Depois, escolha uma tarefa pequena e observe se ele realmente consulta as instruções. **Instalação, descoberta e aplicação efetiva são verificações diferentes**.

### 🛠️ Solução rápida de problemas

<details>
<summary><strong>O comando npx não funciona</strong></summary>

Verifique se Node.js e npm estão instalados com `node --version` e `npm --version`. Se necessário, instale o Node.js LTS e reabra o terminal.

</details>

<details>
<summary><strong>A skill foi instalada, mas o Claude Code ou Codex não a encontra</strong></summary>

Confirme que você selecionou o agente correto no instalador e o local de instalação. Abra uma nova sessão. Se ainda não aparecer, consulte a documentação específica de descoberta de skills da sua versão do [Claude Code](https://code.claude.com/docs) ou [Codex](https://developers.openai.com/codex/).

</details>

<details>
<summary><strong>O agente encontra a skill, mas ignora algumas regras</strong></summary>

Peça que ele leia explicitamente o `SKILL.md` correspondente e explique quais instruções serão aplicadas. Para regras persistentes por projeto, consulte o [guia de ativação](docs/ACTIVATION.md). A skill é uma orientação, não um mecanismo infalível de imposição de regras.

</details>

<details>
<summary><strong>Quero instalar manualmente, sem npx</strong></summary>

Abra a pasta [skills/](skills/) deste repositório, escolha a especialidade e copie a pasta completa, incluindo `SKILL.md` e `references/`, para o local reconhecido pelo seu agente. A localização depende da versão e configuração do Claude Code ou Codex. Consulte [instalação detalhada](docs/ECOSYSTEM_V2.md) e [compatibilidade](docs/COMPATIBILITY.md).

</details>

### 📖 Documentação adicional

[**Guia de ativação**](docs/ACTIVATION.md) · [**Instalação detalhada**](docs/ECOSYSTEM_V2.md) · [**Windows e VS Code**](docs/INSTALL_WINDOWS.md) · [**Compatibilidade**](docs/COMPATIBILITY.md)

---

## Como funciona a orquestração

```text
Solicitação do usuário
      │
      ▼
SeuMadruga CORE: objetivo + escopo + risco
      │
      ▼
Registro de especialidades → escolha seletiva
      │
      ▼
Instruções do projeto + SKILL.md + referências relevantes
      │
      ▼
Plano autorizado → execução → testes → relatório
```

O roteador determinístico pode sugerir skills por palavras-chave, mas não instala nem ativa módulos automaticamente:

```bash
python tools/skill_router.py "Criar um dashboard com autenticação, filtros e tooltips"
```

Consulte [registro](core/skill-registry.json), [política de seleção](core/ROUTING_POLICY.md) e [contrato de qualidade](core/QUALITY_CONTRACT.md).

## Conheça cada especialidade

As oito especialidades abaixo apresentam sua identidade visual original imediatamente antes das instruções. A imagem CORE é a capa Master do projeto.

### 1. SeuMadruga CORE

**O centro de coordenação do ecossistema.** A arte do CORE abre este documento como Capa Master e não é repetida aqui.

**Especialidade:** Orquestração, triagem e economia de contexto.

**O que faz:** Definir o resultado esperado; classificar risco, escopo e autorização; selecionar o mínimo de especialistas; definir critérios verificáveis; registrar evidências e pendências.

**Quando chamar:** orquestração · triagem de tarefas · seleção de skills · política de riscos · economia de contexto.

**Arquivos:** [SKILL.md](skills/seu-madruga-core/SKILL.md) · [Checklist](skills/seu-madruga-core/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga SeuMadruga CORE para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/design-system.webp" alt="Arte oficial SeuMadruga Design System" width="100%"></p>

### 2. Design System

**Especialidade:** Interfaces, UX/UI e design de produto.

**O que faz:** Auditar a interface existente; definir hierarquia, tokens e componentes; planejar comportamento responsivo; rever navegação, foco, teclado e contraste; verificar as telas renderizadas.

**Quando chamar:** frontend · interface · UX · UI · design system · componentização · responsividade · microinterações.

**Arquivos:** [SKILL.md](skills/design-system/SKILL.md) · [Checklist](skills/design-system/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga Design System para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/cybersecurity.webp" alt="Arte oficial SeuMadruga Cybersecurity" width="100%"></p>

### 3. Cybersecurity

**Especialidade:** Segurança, privacidade e controle de acesso.

**O que faz:** Mapear dados e ameaças; avaliar autenticação e autorização; investigar injeção, XSS, SSRF e exposição de segredos conforme o projeto; criar testes negativos; documentar severidade e limites.

**Quando chamar:** segurança · autenticação · autorização · API · SQL · XSS · vulnerabilidade · LGPD · segredos.

**Arquivos:** [SKILL.md](skills/cybersecurity/SKILL.md) · [Checklist](skills/cybersecurity/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga Cybersecurity para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/motion-studio.webp" alt="Arte oficial SeuMadruga Motion Studio" width="100%"></p>

### 4. Motion Studio

**Especialidade:** Vídeo programático, Remotion e animação.

**O que faz:** Confirmar formato, duração, FPS e assets; elaborar roteiro e storyboard; criar movimentos determinísticos; testar legendas, áudio e safe areas; renderizar amostras quando houver infraestrutura.

**Quando chamar:** Remotion · vídeos · reels · motion design · transições · storyboard · renderização.

**Arquivos:** [SKILL.md](skills/motion-studio/SKILL.md) · [Checklist](skills/motion-studio/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga Motion Studio para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/architecture.webp" alt="Arte oficial SeuMadruga Architecture" width="100%"></p>

### 5. Architecture

**Especialidade:** Arquitetura, APIs, bancos e documentação técnica.

**O que faz:** Inspecionar decisões existentes; documentar requisitos e restrições; comparar alternativas; modelar APIs, persistência, migrações e rollback; registrar ADRs e critérios de aceite.

**Quando chamar:** PRD · TRD · arquitetura · escalabilidade · API · banco · infraestrutura · ADR.

**Arquivos:** [SKILL.md](skills/architecture/SKILL.md) · [Checklist](skills/architecture/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga Architecture para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/quality-assurance.webp" alt="Arte oficial SeuMadruga Quality Assurance" width="100%"></p>

### 6. Quality Assurance

**Especialidade:** Testes, qualidade e confiabilidade.

**O que faz:** Identificar partes alteradas; selecionar testes por risco; executar lint, unitários e integração quando disponíveis; adicionar regressões; conferir CI e relatar PASS/WARN/FAIL/NOT_RUN com evidência.

**Quando chamar:** testes · QA · qualidade · lint · CI · revisão · release · regressão.

**Arquivos:** [SKILL.md](skills/quality-assurance/SKILL.md) · [Checklist](skills/quality-assurance/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga Quality Assurance para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/ai-operation.webp" alt="Arte oficial SeuMadruga AI Operations" width="100%"></p>

### 7. AI Operations

**Especialidade:** Agentes, MCP, modelos e eficiência.

**O que faz:** Inventariar ferramentas reais; evitar leitura redundante; revisar permissões de MCPs; otimizar handoffs e sessões; recomendar esforço/modelo sem alegar troca automática; usar métricas reais quando existirem.

**Quando chamar:** agentes · MCP · tokens · roteamento de modelos · memória · contexto · automação.

**Arquivos:** [SKILL.md](skills/ai-operations/SKILL.md) · [Checklist](skills/ai-operations/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga AI Operations para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/data-experience.webp" alt="Arte oficial SeuMadruga Data Experience" width="100%"></p>

### 8. Data Experience

**Especialidade:** Dashboards, KPIs e visualização de dados.

**O que faz:** Validar significado e fonte das métricas; escolher visuais apropriados; implementar filtros, drill-down, tooltips e alternativas tabulares; testar responsividade e acessibilidade; evitar distorções estatísticas.

**Quando chamar:** dashboard · KPI · gráficos · dados · estatística · analytics · storytelling.

**Arquivos:** [SKILL.md](skills/data-experience/SKILL.md) · [Checklist](skills/data-experience/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga Data Experience para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.

---

<p align="center"><img src="branding/ecosystem-v2/content-studio.webp" alt="Arte oficial SeuMadruga Content Studio" width="100%"></p>

### 9. Content Studio

**Especialidade:** Conteúdo, roteiros e narrativa multicanal.

**O que faz:** Definir público e objetivo; planejar narrativa e formatos; produzir roteiro/carrossel/legenda; revisar mobile, claims e licenças; entregar com checklist e sem publicar automaticamente.

**Quando chamar:** instagram · carrossel · legenda · reels · marketing · CTA · conteúdo.

**Arquivos:** [SKILL.md](skills/content-studio/SKILL.md) · [Checklist](skills/content-studio/references/CHECKLIST.md).

**Exemplo:** > Use o SeuMadruga Content Studio para avaliar o trabalho neste domínio, preservar o que já funciona e apresentar testes e evidências.


## Exemplos de uso

| Objetivo | Skills indicadas | Resultado esperado |
| --- | --- | --- |
| Dashboard interativo | CORE + Design System + Data Experience | Hierarquia, filtros, gráficos compreensíveis e revisão de UX |
| Revisar login e permissões | CORE + Cybersecurity + Quality Assurance | Avaliação de risco, testes negativos e recomendações verificáveis |
| Criar vídeos em Remotion | CORE + Motion Studio + Content Studio | Roteiro, cenas, animações e estratégia de exportação |
| Planejar SaaS multiusuário | CORE + Architecture + Cybersecurity | Requisitos, decisões de arquitetura e controles de acesso |
| Reduzir desperdício de contexto | CORE + AI Operations | Leitura seletiva, handoffs e avaliação de eficiência |

## Estrutura do projeto

```text
seu-madruga-dev/
├── AGENTS.md / CLAUDE.md       # Instruções existentes para agentes
├── branding/                   # Marca original do projeto
├── core/                       # Registro e contratos do ecossistema
├── docs/                       # Instalação, ativação, compatibilidade e qualidade
├── skills/
│   ├── seu-madruga-dev/        # Skill original preservada
│   ├── seu-madruga-core/
│   ├── design-system/
│   ├── cybersecurity/
│   ├── motion-studio/
│   ├── architecture/
│   ├── quality-assurance/
│   ├── ai-operations/
│   ├── data-experience/
│   ├── content-studio/
├── tools/                      # Utilitários Python
├── tests/                      # Testes automatizados
├── LICENSE
└── README.md
```

## Validação e limites

- **PASS:** verificação realmente executada e aprovada dentro do escopo.
- **WARN:** risco ou limitação encontrada.
- **FAIL:** verificação executada e reprovada.
- **NOT_RUN:** não foi executada.
- **NOT_APPLICABLE:** não se aplica à tarefa.

Execute os testes do repositório com:

```bash
python tests/validate_skill.py
python -m unittest discover -s tests -p "test_*.py"
python -m py_compile tools/madruga.py tools/quality_gates.py tools/skill_router.py
```

Essas verificações não substituem testes de execução real, avaliações de segurança nem a revisão visual em navegador. O GitHub Actions executa os checks configurados no workflow existente.

## Documentação de referência

- [Instalação e ativação](docs/ACTIVATION.md) · [Ecosystem 2.0](docs/ECOSYSTEM_V2.md)
- [Compatibilidade Claude Code e Codex](docs/COMPATIBILITY.md) · [Quality Gates](docs/QUALITY_GATES.md)
- [Política de segurança](SECURITY.md) · [Avaliação de resultados](EVALUATION.md)
- [Como contribuir](CONTRIBUTING.md) · [Licença MIT](LICENSE)

## Projeto, autoria e direitos

**Criado por Rômulo Bezerra** · [GitHub quickplus2027](https://github.com/quickplus2027)

Projeto independente, sem vínculo oficial com OpenAI, Anthropic ou titulares da série *Chaves*. O uso de nomes, personagens e marcas de terceiros pode exigir autorização específica; a licença do código não concede automaticamente esses direitos.

<p align="center"><img src="branding/seu-madruga-dev-mark.png" alt="Identidade histórica do SeuMadruga.dev" width="150"></p>
<p align="center"><strong>SeuMadruga.dev · Token não dá em árvore.</strong></p>
