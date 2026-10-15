# Como conversar com o SeuMadruga.dev

**Por Rômulo Bezerra**

O SeuMadruga.dev é uma Skill, não um programa que roda sozinho. Depois de instalar, converse normalmente com Claude Code ou Codex e, se não for reconhecida, peça explicitamente para usar a Skill `seu-madruga-dev`.

## Cinco pedidos prontos

1. **"Seu Madruga, revise as alterações desta tarefa, sem mudar nada."** Resposta esperada: arquivos afetados, verificações realizadas e pendências.
2. **"Seu Madruga, prepare as regras neste projeto."** Resposta esperada: inspeção e prévia para aprovação antes de instalar qualquer regra.
3. **"Seu Madruga, qual motor e esforço são adequados?"** Resposta esperada: recomendação conforme opções realmente disponíveis; nada de troca fictícia.
4. **"Seu Madruga, avalie o visual e a experiência desta tela."** Resposta esperada: direção artística, usabilidade, acessibilidade e critérios verificáveis; não basta dizer que ficou bonito.
5. **"Seu Madruga, esta conversa está enorme."** Resposta esperada: orientação de handoff ou nova sessão, sem perder decisões.

## Quando pedir aprovação?

Ler arquivos e executar diagnósticos não destrutivos pode fazer parte da análise autorizada. Instalar hooks, adicionar instruções persistentes, apagar arquivos, trocar configurações, instalar pacotes e fazer deploy exigem aprovação apropriada.

## O que a Skill não garante

Não monitora tokens sozinha, não ativa modelos automaticamente e não consegue impor regras acima da política do agente. Um diagnóstico confirma arquivos e configurações, não obediência. Não presume que os scripts opcionais estejam incluídos no diretório de instalação da Skill.
