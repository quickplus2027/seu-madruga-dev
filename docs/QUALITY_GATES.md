# Quality Gates opt-in | SeuMadruga.dev

**Por Rômulo Bezerra**. A Skill recomenda. Os quality gates verificam indícios objetivos. Nenhum dos dois garante obediência integral, UI premiada ou segurança certificada.

## Regras fundamentais

1. Nunca instalar hooks ou alterar configurações existentes automaticamente.
2. Usar verificações rápidas e restritas aos arquivos alterados como primeiro passo. CI e risco podem exigir testes completos.
3. A verificação HTML é heurística, não equivale à auditoria WCAG, testes de leitor de tela ou testes em navegador.
4. Testes visuais reais requerem um navegador ou ferramenta de comparação de screenshots do projeto (por exemplo, Playwright), com baseline revisada por humano. A Skill não instala dependências por conta própria.
5. Não executar scripts arbitrários de dependências ou pacotes externos sem revisão e aprovação.

## Qualidade editorial + acessibilidade HTML (offline)

No repositório da Skill, aponte para um projeto real:

```powershell
python D:\DEV\SeuMadruga\tools\quality_gates.py check --project D:\DEV\MeuProjeto --changed --editorial
```

Para indicar arquivos específicos:

```powershell
python D:\DEV\SeuMadruga\tools\quality_gates.py check --project D:\DEV\MeuProjeto index.html README.md --editorial
```

O verificador não percorre o repositório inteiro sem você selecionar arquivos. Alterações já commitadas não aparecem em `--changed`, portanto selecione arquivos explicitamente nesses casos. HTML: procura `alt`, `lang`, certos campos de formulário e nomes de botões. JSX/TSX precisam de ferramenta específica do framework; não há análise AST neste validador.

## Hooks do Claude Code (opt-in, projeto local)

```powershell
python D:\DEV\SeuMadruga\tools\madruga.py hooks-claude --project D:\DEV\MeuProjeto
python D:\DEV\SeuMadruga\tools\madruga.py hooks-claude --project D:\DEV\MeuProjeto --apply
```

O instalador só cria `.claude/settings.local.json` se esse arquivo **não existir**. Caso exista, interrompe para mesclagem manual. Não alteramos hooks da conta do usuário. Os hooks fornecem lembrete no início da sessão e feedback consultivo em Edit/Write. Verifique com `/hooks` no Claude Code. O resultado real depende da versão do cliente e da confiança dada aos hooks.

**Codex:** `AGENTS.md` e Quality Gates manuais/CI continuam disponíveis. O projeto não altera automaticamente `config.toml` nem presume compatibilidade do mesmo esquema de hooks. Configurações de ciclo de vida variam conforme versão e distribuição, portanto exigem integração e teste separados.

## Regressão visual e UX

Quando projeto usar Playwright, considere adicionar testes específicos para: estados mobile/desktop, contraste, navegação por teclado, foco visível, `prefers-reduced-motion`, fluxo de filtros, tooltips por toque e screenshots estáveis. Testes de screenshot exigem revisão humana para falsos positivos e regressões semânticas.

## Gates de release

- **Obrigatórios**: checks de CI já definidos, alterações com risco de segurança, migrações e fluxos críticos.
- **Direcionados**: unitários de componentes/símbolos alterados, lint local e verificações de acessibilidade da tela modificada.
- **Opcionais condicionais**: suíte completa, benchmarks, lighthouse, browsers multiplataforma e snapshots, conforme risco e autorização.

## Limitações

O `doctor` confirma a presença de regras, não que o agente as aplicou. O quality checker usa heurísticas simples, não mede tokens faturados e não executa testes e2e automaticamente. Não instalar ou ativar hooks em projetos que não confiam nos comandos locais.
