# SeuMadruga Ecosystem 2.0

**Autor original: Rômulo Bezerra**

Expansão aditiva da versão experimental legada, sem substituir a skill `seu-madruga-dev`, comandos ou scripts originais.

## Instalação

### CLI compatível com skills.sh
```bash
npx skills add quickplus2027/seu-madruga-dev --skill seu-madruga-core
npx skills add quickplus2027/seu-madruga-dev --skill design-system
```

Repita o comando `--skill` apenas para as especialidades necessárias. Inspecione o instalador de terceiros antes de executá-lo e confirme a compatibilidade com sua versão da ferramenta.

### Claude Code

Utilize as pastas `skills/<nome>/` como origem das skills; configure as skills nos locais de descoberta documentados pela versão instalada do Claude Code. Peça explicitamente: **Use a skill SeuMadruga CORE e as especialidades necessárias nesta tarefa**. `CLAUDE.md` do repositório mantém as instruções existentes. Não se presume descoberta ou carregamento automático.

### OpenAI Codex

Instale ou disponibilize as pastas de cada skill conforme o diretório de descoberta e configurações suportados pela sua versão do Codex. O arquivo `AGENTS.md` do repositório continua valendo; não substitua suas instruções. A disponibilidade de um `SKILL.md` não comprova ativação.

## Uso do roteador

```bash
python tools/skill_router.py "Criar um dashboard acessível com autenticação"
python -m unittest discover -s tests -p "test_*.py"
```

O roteador é uma indicação por palavras-chave. Não modifica configurações de Claude Code/Codex nem oferece hooks universais. Consulte `core/ROUTING_POLICY.md` e `core/QUALITY_CONTRACT.md`.

## Branding

O registro define nove nomes `branding/ecosystem-v2/<skill>.webp`. As imagens pertencem ao pacote de origem; sua publicação deve ser conferida separadamente. Nenhuma logo original deve ser removida ou substituída.

## Crédito

**Criado por Rômulo Bezerra.** Projeto independente. Licença e notas de direitos preexistentes permanecem em `LICENSE` e no README principal.
