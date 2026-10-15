<div align="center">

<img src="branding/seu-madruga-dev-mark1.png" alt="SeuMadruga.dev: marca original" width="100%">

# SeuMadruga Ecosystem 2.0
### Seu conhecimento, seus agentes, seu fluxo de trabalho.

**9 skills especializadas para Claude Code e OpenAI Codex**

**Criado por Rômulo Bezerra** · [Instalação](#instalação) · [Explore as skills](#o-ecossistema) · [Documentação](docs/ECOSYSTEM_V2.md)

</div>

---

## O ecossistema

O SeuMadruga é uma coleção de instruções modulares para ajudar assistentes de programação e criação. Você pode usar apenas a especialidade que interessa à tarefa. O **CORE** ajuda a identificar quais especialidades são relevantes; isso não significa que ele as carregue automaticamente.

| Skill | Especialidade | Abrir |
| :--- | :--- | :--- |
| 🧠 **SeuMadruga CORE** | Orquestração, seleção contextual e planejamento | [SKILL.md](skills/seu-madruga-core/SKILL.md) |
| 🎨 **Design System** | UX, UI, acessibilidade, frontend e design visual | [SKILL.md](skills/design-system/SKILL.md) |
| 🛡️ **Cybersecurity** | Ameaças, autenticação, LGPD e segurança | [SKILL.md](skills/cybersecurity/SKILL.md) |
| 🎬 **Motion Studio** | Storyboard, Remotion, vídeos e animações | [SKILL.md](skills/motion-studio/SKILL.md) |
| 🏗️ **Architecture** | Arquitetura, decisões técnicas e infraestrutura | [SKILL.md](skills/architecture/SKILL.md) |
| ✅ **Quality Assurance** | Testes, regressão e controle de qualidade | [SKILL.md](skills/quality-assurance/SKILL.md) |
| 🤖 **AI Operations** | Agentes, contexto, tokens e modelos | [SKILL.md](skills/ai-operations/SKILL.md) |
| 📊 **Data Experience** | Dashboards, gráficos, métricas e dados | [SKILL.md](skills/data-experience/SKILL.md) |
| ✍️ **Content Studio** | Conteúdo, narrativas e comunicação | [SKILL.md](skills/content-studio/SKILL.md) |


## Instalação

Uma skill não é um programa independente: o agente precisa reconhecê-la. É possível instalar seletivamente por meio do instalador compatível com sua ferramenta:

```bash
npx skills add quickplus2027/seu-madruga-dev --skill seu-madruga-core
```

Para outra especialidade, altere o argumento `--skill`, por exemplo `design-system` ou `motion-studio`. O comando `npx` utiliza um instalador de terceiros: inspecione a origem e os arquivos antes de executá-lo.

Consulte [instalação e ativação](docs/ECOSYSTEM_V2.md), [compatibilidade](docs/COMPATIBILITY.md) e [diagnóstico das regras do projeto](docs/ACTIVATION.md). A presença de um arquivo `SKILL.md` não comprova que o agente o descobriu ou ativou.

## Uso em linguagem natural

Peça, por exemplo:

> Use SeuMadruga CORE e Design System para revisar este dashboard. Preserve a arquitetura atual, explique as melhorias de UX e execute apenas os testes realmente disponíveis. Avise o que não foi validado.

Se quiser uma sugestão determinística das especialidades relevantes:

```bash
python tools/skill_router.py "Crie um dashboard responsivo com autenticação"
```

Este roteador **não instala skills, não troca o modelo e não modifica o projeto**: apenas devolve recomendações por palavras-chave.

## Estrutura do projeto

```text
skills/
  seu-madruga-core/         # triagem e coordenação
  design-system/            # experiência visual
  cybersecurity/            # segurança
  motion-studio/            # vídeo e animação
  architecture/             # arquitetura
  quality-assurance/        # testes e qualidade
  ai-operations/            # operação de agentes
  data-experience/          # dados e dashboards
  content-studio/           # produção de conteúdo
  seu-madruga-dev/          # skill original preservada
core/                       # registro e contratos
tools/                      # utilitários Python
tests/                      # testes automatizados
docs/                       # instruções e referências
branding/                   # logomarcas originais
```

## Qualidade, segurança e transparência

O repositório mantém testes offline, verificações de estrutura e um workflow em GitHub Actions. Validações estáticas e unitárias **não** comprovam execução operacional das skills no Claude Code ou Codex, nem substituem auditorias completas de segurança, acessibilidade ou produção audiovisual.

- [Contrato de qualidade](core/QUALITY_CONTRACT.md)
- [Política de roteamento](core/ROUTING_POLICY.md)
- [Registro das nove skills](core/skill-registry.json)
- [Segurança](SECURITY.md)
- [Contribuições](CONTRIBUTING.md)
- [Licença MIT](LICENSE)

A skill original `seu-madruga-dev`, seus scripts, testes e referências continuam disponíveis para compatibilidade. O Ecosystem 2.0 é uma ampliação modular, não uma garantia de automatização invisível ou economia fixa de tokens.

---

<div align="center">

**SeuMadruga.dev** · *Token não dá em árvore.*

**Idealizado e criado por Rômulo Bezerra**

<img src="branding/seu-madruga-dev-mark.png" alt="Marca original do projeto" width="170">

<sub>Projeto independente, sem afiliação oficial com OpenAI, Anthropic ou titulares da série Chaves. Consulte as notas de propriedade intelectual e licença antes de uso comercial.</sub>

</div>
