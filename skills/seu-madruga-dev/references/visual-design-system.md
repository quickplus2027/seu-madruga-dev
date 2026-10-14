# Design de classe mundial e Design System

**Carregar:** identidade, layouts, bibliotecas de componentes, tipografia, tokens e responsividade.

## Direção artística
- Formular tese visual: público, personalidade, narrativa, referências culturais, tom editorial, ritmo e contraste. Registrar o que torna o projeto distintivo.
- Explorar 1–2 conceitos aplicáveis antes de construir; distinguir "premium" de "decorativo". Considerar hierarquia, composição assimétrica, espaço negativo, ritmo, escala tipográfica, densidade e legibilidade.
- Vocabulário: High-End Visual Design, Bespoke UI, Human-Centered Design, Editorial, Emotional Design, Visual Hierarchy, Brand Storytelling, Experimental Interface, Responsive Grid Systems.
- Não introduzir estética impositiva se houver marca/tokens já definidos. Preservar logotipo, cores obrigatórias, componentes, semântica e experiência anterior.

## Tokens e arquitetura
- Em projetos visuais substantivos documentar/atualizar `DESIGN_SYSTEM.md`, salvo se projeto já tiver fonte da verdade equivalente. Centralizar `color`, typography, spacing, radius, elevation, borders, durations, easing, breakpoints, z-index, semantic states, chart colors e `prefers-reduced-motion`.
- Evitar hex dispersos e estilos quase duplicados. Components composable, tokens semânticos e variantes explícitas. Design tokens devem funcionar nos temas claro/escuro quando necessários.
- Avaliar bibliotecas: shadcn/ui, Radix UI, Motion, Rive, Lottie, GSAP e equivalentes apenas quando justificadas e compatíveis com a stack; conferir versões/licenças.

## Padrões seletivos de interface
Bento Grid, cards contextuais, tabs animadas, command palette, spotlight search, expandable panels, skeleton loading, floating panels, visualização progressiva, contextual help, tooltips e guided onboarding. Escolher por objetivo e não por tendência.

## Responsividade
- Mobile-first quando apropriado; desktop não é versão esticada do celular.
- Touch, teclado, zoom de texto, legibilidade, densidade e ações críticas sempre disponíveis.
- Respeitar layout existente; alterações estruturais precisam de plano aprovado e verificação regressiva.
