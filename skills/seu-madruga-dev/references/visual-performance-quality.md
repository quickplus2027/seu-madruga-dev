# Performance, validação visual e qualidade de produção

**Carregar:** checklist de aceite de frontend, perfis de performance e testes visuais.

## Verificações por impacto
- Alteração pequena em componente: unit/component test direcionado + revisão do estado alterado + teclado/foco se interativo.
- Mudança de fluxo ou layout: testes de integração da jornada e capturas em larguras representativas; verificar scroll, touch, loading/empty/error.
- Alteração de tema/design system: conferir componentes dependentes, contraste e regressões visuais, incluindo modo escuro se existir.
- 3D/motion: conferir dispositivo fraco, reduced motion, sem suporte gráfico, memória, desempenho e fallback.
- Antes de release/CI obrigatória: executar suítes exigidas pelas políticas do repositório e avaliações de segurança; não confundir teste seletivo com dispensa de quality gate.

## Engenharia
Creative Frontend Engineering, GPU Acceleration, Frame Budget Optimization, Lazy Loading, Code Splitting, Progressive Enhancement, Dynamic LOD, Accessibility-First Motion, Core Web Vitals, Performance Profiling, Offscreen Rendering, Web Workers, Memory Optimization.
- Otimizar imagens, tipografia, conteúdo acima da dobra e bundle. Evitar renderizações repetidas, watchers excessivos e carregamento de bibliotecas gigantes.
- Não bloquear UI nem depender de conexão contínua sem informar. Fallbacks progressivos e layouts resistentes.
- Proteger acessibilidade: semântica, labels, foco, navegação por teclado, contraste, motion reduzido e zoom.

## Evidência de conclusão
Identidade e originalidade, intuitividade para iniciantes, transições com propósito, resposta a interações, celular, acessibilidade, desempenho, funcionalidade preservada, testes reais reportados. Nunca declarar validação visual se não houve inspeção ou captura.
