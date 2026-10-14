# Motion Design | Narrativa antes de espetáculo

**Carregar:** animações, transições, SVG, scroll, layout shifts e microinterações.

## Linguagem visual
Motion Choreography, Cinematic Motion Design, Kinetic Typography, Spring Physics, Motion Tokens, Morphing Animation, Staggered Reveals, Scroll-Driven Animations, Scrollytelling, Parallax, FLIP, Shared Element Transitions, SVG Path Animation, Liquid Transitions, Gesture-Driven, Magnetic Interactions.

## Regra de desenho
- Para cada animação registrar objetivo: continuidade espacial, confirmação de estado, relação entre informações, atenção, narrativa ou orientação.
- Microinterações instantâneas e discretas; evitar atrasos artificiais, revelações que escondam tarefas, animações infantis e scroll-jacking.
- Pensar motion desde o planejamento, mas implementar depois da estrutura utilizável. Compartilhar tokens de timing/easing e evitar durações arbitrárias espalhadas.
- Animação de nascimento progressivo de conexões, quando o produto pedir, deve revelar nós e relações em sequência inteligível, não looping sem propósito.
- Tecnologias: CSS transitions/Web Animations API para simples; Motion/GSAP para coordenação complexa; Rive/Lottie conforme benefício; SVG para linhas e morphs; não instalar as quatro para um efeito pequeno.

## Performance e segurança
- Priorizar transform/opacity; medir jank e animações em hardware modesto. Metas de 60 FPS dependem do dispositivo e não são garantia.
- `prefers-reduced-motion`: fornecer versão estática ou transição mínima; nunca esconder informações na versão reduzida.
- Não causar layout shift significativo, consumo excessivo de CPU/GPU, rolagem bloqueada nem eventos sem limpeza.
