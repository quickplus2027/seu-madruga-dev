# Publicar no GitHub, do zero (Windows + VS Code)
**Por Rômulo Bezerra**. Projeto: `quickplus2027/seu-madruga-dev`.

## 1. Revisar localmente
Descompacte na pasta de trabalho, abra a pasta raiz no VS Code e revise `README.md`, `SECURITY.md`, `LICENSE` e `skills/seu-madruga-dev/SKILL.md`. Não publique dados pessoais, arquivos `.env`, senhas nem material de terceiros sem autorização. O nome/semelhança de personagem de TV pode envolver direitos de marca e imagem; os vetores incluídos são originais, mas o nome merece revisão antes de uso comercial.

## 2. Testar no terminal do VS Code (PowerShell)
```powershell
python tests/validate_skill.py
python -m unittest discover -s tests -p 'test_*.py'
```
O validador local é suplementar. Se desejar conferir a especificação oficial, use `skills-ref validate skills/seu-madruga-dev` após instalar o validador oficial conforme sua documentação.

## 3. Criar repositório público
Acesse https://github.com/new (logado na conta `quickplus2027`), Repository name: `seu-madruga-dev`, visibilidade **Public**, sem marcar README/License/gitignore extras pois já existem localmente. Crie o repositório.

## 4. Versionar e enviar
No terminal na raiz descompactada:
```powershell
git init
git branch -M main
git add .
git status
git commit -m "feat: initial SeuMadruga.dev agent skill"
git remote add origin https://github.com/quickplus2027/seu-madruga-dev.git
git push -u origin main
```
Git poderá pedir autenticação no navegador. Se `origin` já existir, revise `git remote -v` antes de alterá-lo. Não use `--force` em repos existentes.

## 5. Ajustes no GitHub
Edite a descrição: `Brazilian-inspired Agent Skill for token optimization, context engineering, selective testing and safe Claude Code/Codex workflows.`
Topics: `agent-skills`, `claude-code`, `codex`, `token-optimization`, `context-engineering`, `ai-agents`, `developer-tools`, `llm-optimization`.
Habilite Issues, Discussions (opcional), Dependabot alerts, private vulnerability reporting (se disponível), proteção da branch `main` e exigência de checks do workflow antes de PR merge. Verifique se Actions executou com sucesso.

## 6. Instalação e Skills.sh
Depois do push, revise a documentação oficial https://www.skills.sh/docs/cli e teste em **projeto descartável**:
```powershell
npx skills add quickplus2027/seu-madruga-dev --skill seu-madruga-dev
```
Esse CLI executa código de pacote: revise o provedor, versão e permissões antes. Use a opção de seleção de agentes oferecida pela versão instalada; não presuma flags disponíveis. Se a Skill for indexada no diretório, confirme a página pública; publicar no GitHub não garante aparição instantânea nem ranking.

## 7. Release e manutenção
Crie tag `v0.1.0` e GitHub Release indicando "experimental, no verified savings claims". Abra issues para benchmarks reais, análise de terceiros, compatibilidade e acessibilidade. Quando benchmarks passarem, publique os dados e critérios antes de afirmar porcentagens de economia.

## 8. Atualizar futuramente
```powershell
git status
git pull --ff-only
# edite arquivos, rode testes, revise o diff
git add .
git commit -m "docs: improve efficiency workflow"
git push
```
Em times, faça branch e Pull Request em vez de push direto no `main`.
