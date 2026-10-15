# Como tornar as regras persistentes

A instalação via skills.sh disponibiliza a Skill; não injeta regras permanentes em cada repositório. Para impor convenções de projeto, execute um preview do bootstrap e, após revisar, aplique os blocos identificados em `AGENTS.md` e `CLAUDE.md`.

```powershell
python tools/madruga.py bootstrap --project D:\DEV\MeuProjeto
python tools/madruga.py bootstrap --project D:\DEV\MeuProjeto --apply
python tools/madruga.py doctor --project D:\DEV\MeuProjeto
```

Use `tools/madruga.py` a partir de um clone local deste repositório; instalar apenas a Skill pode não instalar essa ferramenta. O bootstrap preserva o conteúdo anterior, adiciona um bloco delimitado, cria cópias `.seumadruga.bak` antes de modificar arquivos existentes e não sobrescreve backups. Compare o diff e reinicie a sessão do agente.

## Limites reais

* Regras persistentes são instruções, não alterações da hierarquia de sistema nem bloqueios invioláveis.
* O comando `doctor` verifica arquivos locais, não prova ativação no modelo.
* A Skill não altera motores, contexto ou Plan Mode automaticamente.
* Para travessões em textos markdown revisáveis, use `python tools/madruga.py lint-prose arquivo.md`.
* Hooks e CI opcionais são necessários para bloquear violações automaticamente; a aplicação depende da plataforma.
