# Spatial UI, WebGL, 3D e experiências imersivas

**Carregar:** tarefas que EXIGEM profundidade, cenas 3D, ambientes e visualização espacial.

**Regra central: 3D para contexto e emoção. 2D para precisão dos dados.**

## Escada de complexidade
1. CSS 3D: perspective, translateZ, rotateX/Y, sombras e parallax sutil.
2. SVG/CSS canvas leve para ilustrações, gráficos e camadas.
3. Three.js / React Three Fiber / WebGL somente para cena ou interação genuinamente tridimensional.
4. WebGPU, GLSL, Ray Marching, GPU Particles, volumetric light e shaders avançados somente com capacidade do navegador, medição e fallback.

## Possibilidades
Procedural Geometry, Particle Systems, GPU Simulation, Raycasting, Orbit Controls, Camera Flythrough, Depth of Field, Bloom, Post-Processing, Instanced Rendering, Camera transitions, 3D Data Visualization e Spatial Computing.

## Critérios de aceitação
- Qual o benefício impossível ou claramente inferior em 2D? Se não houver, não usar 3D.
- Mobile e equipamentos modestos, detecção de suporte, lazy load, level of detail, redução de partículas, fallback e desligamento de animações.
- Câmera acessível e controlável, sem aprisionamento; navegação por teclado quando houver controles.
- Medir tamanho de bundle, frames, consumo de memória, compilação de shaders e tempo de primeiro conteúdo.
- Evitar luminosidade agressiva, efeitos gratuitos e arquitetura dependente de GPUs avançadas.
