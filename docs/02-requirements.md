# processhoops analytics

## Objetivo

Este documento descreve todas as funcionalidades esperadas do processhoops analytics.

Os requisitos aqui definidos representam o comportamento esperado da aplicação e deverão ser respeitados durante todo o desenvolvimento.

Caso exista qualquer dúvida sobre a implementação de alguma funcionalidade, o desenvolvimento deverá ser interrompido para esclarecimento antes da implementação.

Caso alguma funcionalidade não seja suportada pela nba_api, isso deverá ser informado antes da implementação e uma alternativa deverá ser proposta.

---

# 1. Home

## Objetivo

A Home deverá fornecer uma visão geral da temporada atual da NBA, permitindo que o usuário compreenda rapidamente o cenário da liga sem necessidade de navegar para outras páginas.

Ela deverá ser limpa, moderna e objetiva.

O excesso de informações deverá ser evitado.

---

## Componentes obrigatórios

A página inicial deverá possuir:

- Standings completas das duas conferências
- Próximos jogos (considerando o dia mais próximo com partidas)
- Cards com KPIs da temporada
- Barra de navegação para todas as páginas
- Campo de pesquisa global

---

## KPIs

Os KPIs deverão destacar automaticamente os principais desempenhos da temporada.

Exemplos:

- Melhor ataque
- Melhor defesa
- Maior Net Rating
- Maior TS%
- Melhor Offensive Rating
- Melhor Defensive Rating
- Outros indicadores relevantes disponíveis na API

Os KPIs deverão ser apresentados em formato de cartões e permitir interação através de tooltips explicativos.

---

## Standings

As classificações deverão exibir:

- Posição
- Time
- Vitórias
- Derrotas
- Aproveitamento
- Últimos 10 jogos
- Sequência atual
- Jogos atrás do líder (quando disponível)

Sempre que possível deverão possuir:

- Ordenação
- Tooltips
- Destaque visual para classificação aos Playoffs e Play-In

---

## Próximos Jogos

A seção de jogos deverá apresentar:

- Data
- Horário
- Times
- Logos oficiais
- Local (quando disponível)

Caso não existam jogos no dia atual, deverão ser apresentados os jogos do próximo dia disponível.

---

## Pesquisa Global

A Home deverá possuir uma pesquisa rápida permitindo localizar:

- Jogadores
- Times

A pesquisa deverá apresentar sugestões enquanto o usuário digita.

---

# MVP

Obrigatório para a primeira versão.

---

# 2. Teams

## Objetivo

A página de Times deverá fornecer uma análise completa de qualquer equipe da NBA.

Ela deverá permitir compreender rapidamente os pontos fortes, pontos fracos e posicionamento da equipe em relação ao restante da liga.

---

## Seleção do Time

O usuário deverá conseguir selecionar um time através de:

- Pesquisa
- Lista
- Logos dos times

Após a seleção, toda a identidade visual da página deverá adaptar-se ao tema oficial da franquia.

A alteração de tema deverá preservar legibilidade e acessibilidade.

---

## Cabeçalho

O cabeçalho deverá apresentar:

- Logo
- Nome do time
- Conferência
- Divisão
- Campanha
- Aproveitamento

---

## KPIs

A página deverá destacar automaticamente indicadores importantes da equipe.

Exemplos:

- Ranking ofensivo
- Ranking defensivo
- TS%
- eFG%
- Net Rating
- Pace
- Offensive Rating
- Defensive Rating
- Outros indicadores relevantes disponíveis

Sempre que possível os KPIs deverão informar:

- Valor
- Ranking dentro da NBA
- Tooltip explicativo

---

## Comparação com a Liga

Sempre que possível deverão ser apresentados textos ou indicadores como:

- 3º melhor ataque da NBA
- 6ª melhor defesa
- 2º maior TS%
- 12º maior Pace

O objetivo é fornecer contexto para cada estatística.

---

## Desempenho Situacional

Caso os dados estejam disponíveis, apresentar:

- Campanha contra times acima de 50%
- Campanha contra times abaixo de 50%
- Últimos 3 jogos
- Últimos 5 jogos
- Últimos 10 jogos
- Últimos 15 jogos

Esses indicadores deverão ser recalculados automaticamente conforme a classificação atual da liga.

---

## Elenco

O elenco deverá apresentar todos os jogadores da equipe.

Cada jogador deverá possuir acesso rápido à sua página individual.

---

## Estatísticas do Elenco

A tabela de jogadores deverá permitir visualizar:

Estatísticas tradicionais.

Estatísticas avançadas.

A tabela deverá permitir:

- Ordenação em qualquer coluna
- Pesquisa
- Tooltips
- Destaque visual ao passar o mouse

---

## MVP

Obrigatório para a primeira versão.

---

# 3. Players

## Objetivo

A página de jogadores deverá concentrar todas as estatísticas disponíveis para análise individual.

Ela deverá permitir explorar o desempenho de qualquer atleta da NBA durante a temporada selecionada.

---

## Seleção

O usuário deverá conseguir localizar jogadores através de:

- Pesquisa
- Time
- Lista

A pesquisa deverá ser priorizada por velocidade.

---

## Cabeçalho

O cabeçalho deverá apresentar:

- Foto
- Nome
- Time
- Número
- Posição
- Altura
- Peso
- Idade (quando disponível)
- Temporada selecionada

---

## Estatísticas

Sempre que disponíveis na API, deverão ser apresentadas:

- Estatísticas tradicionais
- Estatísticas avançadas
- Game Log
- Splits
- Mapa de arremessos

---

## Percentis

Sempre que possível, o sistema deverá calcular percentis considerando apenas jogadores da mesma posição.

Os percentis deverão ser apresentados visualmente.

---

## Evolução

Quando existirem múltiplas temporadas disponíveis, o usuário deverá conseguir alternar entre elas.

Toda a página deverá ser atualizada automaticamente conforme a temporada selecionada.

---

## Game Log

O histórico de partidas deverá permitir:

- Ordenação
- Pesquisa
- Filtros
- Destaque visual

---

## Navegação

A navegação entre jogadores deverá ser rápida.

Sempre que possível o usuário deverá conseguir trocar de jogador sem necessidade de retornar para outra página.

---

## MVP

Obrigatório para a primeira versão.

# 4. Scatter Explorer

## Objetivo

O Scatter Explorer deverá ser a principal ferramenta de exploração visual do processhoops analytics.

Ele deverá permitir descobrir relações entre quaisquer duas estatísticas disponíveis e identificar padrões entre jogadores ou equipes.

A experiência deverá ser fluida, moderna e altamente interativa.

---

## Seleção de Estatísticas

O usuário deverá conseguir escolher:

- Estatística do eixo X
- Estatística do eixo Y

As opções deverão incluir métricas tradicionais e avançadas disponíveis na aplicação.

A troca de métricas deverá atualizar o gráfico instantaneamente.

---

## Tipos de Entidade

O usuário deverá conseguir alternar entre:

- Jogadores
- Times

---

## Filtros

O gráfico deverá permitir filtrar por:

- Temporada
- Regular Season / Playoffs
- Últimos 3 jogos
- Últimos 5 jogos
- Últimos 10 jogos
- Últimos 15 jogos
- Conferência
- Divisão
- Time
- Posição

---

## Visualização

Os pontos do gráfico deverão ser representados por:

- Foto do jogador (modo jogadores)
- Logo do time (modo times)

O objetivo é criar uma visualização imediatamente reconhecível e visualmente diferenciada.

---

## Interações

Ao passar o mouse sobre um ponto, deverá ser exibido um tooltip contendo:

- Nome
- Time
- Valor do eixo X
- Valor do eixo Y
- Estatísticas adicionais relevantes
- Ranking ou percentil quando disponível

Ao clicar em um ponto:

- abrir a página do jogador ou time correspondente
- preservar o estado do gráfico ao retornar

---

## Seleção de Região

Sempre que possível, o usuário deverá conseguir selecionar uma região do gráfico para filtrar automaticamente a tabela de resultados.

---

## Tabela Vinculada

Abaixo do gráfico deverá existir uma tabela sincronizada com os filtros atuais.

A tabela deverá permitir:

- Ordenação
- Pesquisa
- Exportação
- Seleção rápida de entidades

---

## MVP

Obrigatório para a primeira versão.

---

# 5. Compare

## Objetivo

A página de comparação deverá permitir analisar dois jogadores ou dois times lado a lado.

O foco deverá ser clareza visual e compreensão rápida das diferenças.

---

## Tipos de Comparação

O sistema deverá suportar:

- Jogador vs Jogador
- Time vs Time

Comparações cruzadas não deverão ser permitidas.

---

## Seleção

A seleção deverá ocorrer através de pesquisa rápida.

---

## Layout

O layout deverá exibir as duas entidades lado a lado com:

- Foto ou logo
- Nome
- Time
- Temporada selecionada

---

## Estatísticas

As estatísticas deverão ser organizadas em grupos:

- Tradicionais
- Avançadas
- Eficiência
- Impacto coletivo (quando aplicável)

A melhor marca em cada linha deverá receber destaque visual.

---

## Gráficos

Sempre que possível, apresentar gráficos comparativos simples para facilitar leitura.

---

## Temporada

O usuário deverá conseguir comparar:

- mesma temporada
- temporadas diferentes

---

## MVP

Obrigatório para a primeira versão.

---

# 6. Configurações

## Tema

O usuário deverá conseguir alternar entre:

- Claro
- Escuro

A preferência deverá ser salva localmente.

---

## Preferências

Sempre que possível, salvar:

- última temporada utilizada
- último time selecionado
- último modo de visualização

---

# 7. Exportação

## Gráficos

Os gráficos deverão permitir exportação em:

- PNG
- SVG (quando suportado)

---

## Tabelas

As tabelas deverão permitir exportação em:

- CSV
- XLSX

A exportação deverá respeitar os filtros ativos.

---

# 8. Responsividade

## Desktop

A experiência desktop será a principal prioridade do projeto.

---

## Mobile

A aplicação deverá adaptar:

- tabelas
- filtros
- gráficos
- navegação

sem perda significativa de usabilidade.

---

# 9. Requisitos Gerais

## Performance

A aplicação deverá priorizar velocidade em todas as páginas.

---

## Consistência

Filtros semelhantes deverão funcionar da mesma maneira em toda a aplicação.

---

## Acessibilidade

Garantir contraste adequado e navegação utilizável em diferentes dispositivos.

---

## Estados de Interface

Todas as páginas deverão possuir:

- loading
- vazio
- erro

com mensagens claras para o usuário.

---

## Dados

Todas as informações exibidas deverão vir exclusivamente da nba_api ou de métricas derivadas calculadas localmente.

Caso uma informação não esteja disponível na API, ela não deverá ser exibida sem validação prévia.