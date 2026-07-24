# processhoops analytics

## Objetivo

Este documento define a arquitetura técnica do processhoops analytics.

Toda decisão técnica deverá priorizar:

- Performance
- Simplicidade
- Escalabilidade
- Baixo custo
- Facilidade de manutenção

O projeto deverá utilizar exclusivamente ferramentas gratuitas.

---

# Arquitetura Geral

O processhoops analytics será dividido em duas aplicações independentes.

## 1. Data Pipeline

Responsável por:

- Coletar dados da nba_api
- Processar informações
- Calcular métricas derivadas
- Gerar arquivos JSON
- Atualizar automaticamente o repositório

Nenhuma interface visual deverá existir nesta etapa.

Seu único objetivo é produzir dados prontos para consumo.

---

## 2. Web Application

Responsável por:

- Ler os arquivos JSON
- Exibir informações
- Aplicar filtros
- Construir gráficos
- Renderizar tabelas
- Fornecer excelente experiência ao usuário

A aplicação web nunca deverá depender diretamente da nba_api.

Toda informação utilizada pela interface deverá vir dos JSONs previamente gerados.

---

# Fluxo Geral

A arquitetura deverá seguir o fluxo abaixo.

```

nba_api

↓

Python Pipeline

↓

Processamento

↓

JSONs

↓

GitHub

↓

Vercel

↓

Usuário

```

Toda inteligência deverá ficar concentrada no pipeline Python.

A interface deverá apenas consumir os dados processados.

---

# Pipeline de Dados

O pipeline deverá executar diariamente.

Responsabilidades:

- Buscar dados atualizados
- Validar respostas da API
- Calcular rankings
- Calcular percentis
- Calcular estatísticas derivadas
- Organizar dados
- Gerar JSONs finais

Caso algum endpoint falhe, o pipeline deverá registrar o erro sem interromper completamente a atualização.

Sempre que possível deverão ser preservados os últimos dados válidos.

---

# Atualizações

As atualizações deverão ocorrer automaticamente.

Objetivo inicial:

Todos os dias às 05:00 (Horário de Brasília).

Caso futuramente seja necessário, o horário poderá ser alterado facilmente.

---

# Organização dos Dados

Os JSONs deverão ser organizados por domínio.

Exemplo:

```

/data

players.json

teams.json

standings.json

games.json

schedule.json

player_stats.json

team_stats.json

shot_charts/

game_logs/

```

Arquivos extremamente grandes deverão ser divididos em múltiplos JSONs para reduzir tempo de carregamento.

---

# Estrutura do Projeto

Estrutura sugerida:

```

processhoops-analytics

docs/

data/

pipeline/

src/

components/

pages/

hooks/

services/

types/

utils/

public/

```

Cada pasta deverá possuir responsabilidade única.

---

# Responsabilidades

## Pipeline Python

Responsável por:

- Comunicação com nba_api
- Processamento
- Limpeza
- Normalização
- Rankings
- Percentis
- Estatísticas derivadas
- Exportação para JSON

---

## Front-end

Responsável apenas por:

- Interface
- Navegação
- Filtros
- Pesquisa
- Gráficos
- Tabelas
- Tooltips
- Temas
- Responsividade

Nenhum cálculo complexo deverá ocorrer no navegador.

---

# Performance

A aplicação deverá priorizar:

- Carregamento rápido
- Lazy Loading quando necessário
- Componentes reutilizáveis
- Renderização eficiente
- JSONs otimizados

Sempre que possível os cálculos deverão ocorrer durante o pipeline e nunca durante a navegação do usuário.

---

# Cache

Como os dados são atualizados apenas uma vez por dia, deverá ser utilizado cache agressivo.

A atualização dos arquivos JSON deverá invalidar automaticamente o conteúdo publicado.

---

# Escalabilidade

A arquitetura deverá permitir adicionar futuramente:

- Novas métricas
- Novas páginas
- Novas ligas
- Novas fontes de dados
- Comparações históricas
- Novos gráficos

Sem necessidade de reestruturação completa.

---

# Tratamento de Erros

Caso algum endpoint esteja indisponível:

- Registrar erro
- Continuar processamento dos demais endpoints
- Preservar dados válidos da última atualização

A aplicação web nunca deverá deixar de funcionar por falha temporária da API.

---

# Segurança

Nenhuma chave privada deverá ficar disponível no front-end.

Todo processamento deverá ocorrer antes da publicação do site.

---

# Filosofia Arquitetural

O processhoops analytics seguirá um princípio simples.

O Python pensa.

O Front-end apresenta.

Toda lógica de negócio deverá permanecer concentrada no pipeline de dados.

A interface deverá permanecer limpa, rápida e focada exclusivamente na experiência do usuário.
