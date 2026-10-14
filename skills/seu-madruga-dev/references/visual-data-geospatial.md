# Visual Analytics, Data Storytelling, mapas e inteligência visual

**Carregar:** dashboards, estatísticas, inteligência de dados, mapas ou interfaces analíticas.

## Dados primeiro
- Definir pergunta, público, unidades, fonte, periodicidade, recorte e incertezas antes de escolher gráfico.
- Priorizar precisão 2D, eixos coerentes, escalas explícitas, acessibilidade, etiquetas, legenda e tooltips; 3D somente para contexto.
- Explorable Explanations, Coordinated Multiple Views, Cross-Filtering, Drill-Down/Through, Brushing & Linking, Semantic Zoom, Heatmaps, Sankey, Sunburst, Treemap, Network Graphs, Temporal Visualization, Uncertainty Visualization e Geospatial Analytics: selecionar somente o necessário.
- Bibliotecas: ECharts para gráficos abrangentes, D3 para visualização sob medida, Observable para protótipos/análises, ferramentas de charts existentes quando suficientes.
- Não inventar dados nem ocultar categorias, zeros, intervalos ou exceções. Descrever estados vazios e erros.

## Cartografia
- Choropleth, Vector Tiles, 3D Terrain, Arc Layers, Heatmap Layers, Animated Flows, Clustering, Fly-to Camera, Map Storytelling, Globe Visualization.
- Considerar MapLibre GL JS, deck.gl, CesiumJS, 3D Tiles apenas conforme necessidade, licença, fontes de mapas e geodados.
- Informar projeção, escala, legenda, fonte e temporalidade. Evitar mapas quando tabela/gráfico comunica melhor.

## IA aplicada a visualização
- NL-to-Viz, explainable analytics e recomendações contextualizadas exigem rastreabilidade da consulta, da transformação e das premissas.
- Transparência em incerteza e decisões humanas; sem resultados inventados ou confiança fabricada.
