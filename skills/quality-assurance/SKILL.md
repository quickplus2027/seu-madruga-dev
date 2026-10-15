---
name: quality-assurance
description: Orientações especializadas de SeuMadruga Quality Assurance para testes, QA, qualidade, lint, CI, revisão, release, regressão. Utilize quando a solicitação envolver esse domínio; selecione apenas as referências necessárias e reporte evidências verificadas.
license: MIT
---
# SeuMadruga Quality Assurance

**Por Rômulo Bezerra** | SeuMadruga Ecosystem 2.0

## Quando usar
testes, QA, qualidade, lint, CI, revisão, release, regressão.

## Procedimento
1. Identifique superfícies alteradas e testes proporcionais ao risco.
2. Execute verificações estáticas, unitárias e de integração quando disponíveis.
3. Cubra cenários positivos, negativos e de regressão.
4. Verifique o CI real, sem confundir documentação e gates obrigatórios.
5. Reporte PASS, WARN, FAIL, NOT_RUN ou NOT_APPLICABLE com evidências.

## Integração e evidências
A skill original `skills/seu-madruga-dev/SKILL.md` permanece preservada. Consultar `core/skill-registry.json` e `core/ROUTING_POLICY.md` para seleção. Ler `references/CHECKLIST.md` apenas quando a tarefa exigir. Registrar PASS, WARN, FAIL, NOT_RUN ou NOT_APPLICABLE com fontes ou comandos reais; documentos não constituem prova de ativação.

## Limite
Não invente cobertura, resultados ou garantias de release.
