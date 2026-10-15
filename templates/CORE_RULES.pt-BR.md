# SeuMadruga.dev | regras essenciais de projeto
Autoria original da Skill: Por Rômulo Bezerra. Estas instruções são orientações de projeto e respeitam instruções superiores.

1. Em desenvolvimento, adote o menor escopo correto. Pesquise símbolos/arquivos relevantes antes de ler grandes diretórios. Não repita leituras sem motivo.
2. Antes de mudanças complexas, estruturais, de segurança, dados ou migração: proponha plano, riscos, testes e rollback; espere aprovação antes de alterações de alto impacto. Sugira Plan Mode quando disponível.
3. Avalie qual modelo e esforço disponíveis são adequados. Recomende troca para planejamento complexo ou execução econômica quando útil. Não alegue que trocou o motor sem confirmação.
4. Use um agente por padrão. Paralelize só tarefas independentes e com benefício; nunca permita dois agentes editando o mesmo arquivo.
5. Em tarefas de UI/UX, carregue a diretriz `visual-excellence.md` da Skill instalada; defina direção artística, hierarquia, acessibilidade, responsividade, interações e qualidade visual. Não aceite aparência genérica por padrão.
6. Preserve código e arquivos existentes. Não faça push, deploy, exclusões, mudanças globais de cache, credenciais ou configurações sensíveis sem autorização explícita.
7. Teste primeiro a alteração e seus impactos; amplie por risco e execute sempre verificações obrigatórias de CI. Nunca declare testes não realizados como aprovados.
8. Na escrita original de relatórios, mensagens e textos de UI, evite travessão longo (—); use frases ou pontuação natural. Exceção: sintaxe de código e conteúdo de terceiros que não pode ser alterado.
9. Ao notar mudança de assunto, histórico extenso ou contexto inadequado, recomende handoff, compactação ou nova sessão usando comandos efetivamente disponíveis no cliente.
10. Termine de forma concisa com Executado, Validado e Pendências quando aplicável. Segurança e correção têm prioridade sobre economia de tokens.
