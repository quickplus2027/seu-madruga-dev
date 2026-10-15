# Instalação no Windows / VS Code

O SeuMadruga Ecosystem 2.0 pode ser usado pelo instalador externo `npx skills add` ou com cópia manual das pastas `skills/<identificador>/` para os diretórios suportados pelo Claude Code e Codex na versão instalada.

1. Faça backup do projeto.
2. Clone o repositório ou baixe o código de origem.
3. Leia `AGENTS.md`, `CLAUDE.md` e `docs/ACTIVATION.md`.
4. Copie somente as skills necessárias seguindo a documentação do seu agente.
5. Verifique a descoberta e faça invocação explícita da skill quando necessário.
6. Execute os testes existentes e valide o comportamento com um pedido real.

O roteador `python tools/skill_router.py "pedido"` é opcional, apenas recomenda especialidades. A instalação não substitui revisão de permissões, testes ou aprovação humana.
