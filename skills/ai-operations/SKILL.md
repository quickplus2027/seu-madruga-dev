---
name: ai-operations
description: Orientações especializadas de SeuMadruga AI Operations para agentes, MCP, tokens, roteamento de modelos, memória, contexto, automação. Utilize quando a solicitação envolver esse domínio; selecione apenas as referências necessárias e reporte evidências verificadas.
license: MIT
---
# SeuMadruga AI Operations

**Por Rômulo Bezerra** | SeuMadruga Ecosystem 2.0

## Quando usar
agentes, MCP, tokens, roteamento de modelos, memória, contexto, automação.

## Procedimento
1. Reconheça recursos efetivamente disponíveis no agente e no ambiente.
2. Minimize contexto recuperado e evite leitura repetida sem perder precisão.
3. Sugira modelo e esforço proporcionais à complexidade, sem alegar troca automática.
4. Use múltiplos agentes apenas quando tarefas independentes justificarem a coordenação.
5. Registre handoffs, limites de ferramentas e métricas reais quando disponíveis.

## Integração e evidências
A skill original `skills/seu-madruga-dev/SKILL.md` permanece preservada. Consultar `core/skill-registry.json` e `core/ROUTING_POLICY.md` para seleção. Ler `references/CHECKLIST.md` apenas quando a tarefa exigir. Registrar PASS, WARN, FAIL, NOT_RUN ou NOT_APPLICABLE com fontes ou comandos reais; documentos não constituem prova de ativação.

## Limite
Não invente telemetria de tokens, hooks universais ou capacidades do cliente.
