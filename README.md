# processhoops analytics

Uma plataforma moderna de análise estatística da NBA construída com tecnologias 100% gratuitas.

O objetivo do projeto é reunir estatísticas tradicionais e avançadas em uma interface rápida, intuitiva e altamente interativa, oferecendo uma experiência de exploração de dados superior às soluções existentes.

---

## Objetivos

- Dashboard moderno e responsivo
- Excelente experiência de usuário (UX)
- Atualização automática diária
- Alto desempenho
- Arquitetura escalável
- Utilização exclusiva de ferramentas gratuitas

---

## Principais Funcionalidades

- Dashboard inicial com visão geral da liga
- Standings atualizadas
- Próximos jogos
- KPIs da temporada
- Página completa para cada equipe
- Página completa para cada jogador
- Estatísticas tradicionais e avançadas
- Percentis por posição
- Scatter Plot totalmente configurável
- Comparação entre jogadores e equipes
- Mapas de arremesso
- Game Logs
- Filtros por temporada e splits
- Exportação de gráficos e tabelas

---

## Arquitetura

O projeto é dividido em duas partes independentes:

### Data Pipeline

Responsável por:

- Coletar dados da nba_api
- Processar estatísticas
- Calcular métricas derivadas
- Gerar arquivos JSON

### Web Application

Responsável por:

- Consumir os JSONs gerados
- Exibir gráficos
- Renderizar tabelas
- Aplicar filtros
- Fornecer uma excelente experiência de navegação

---

## Tecnologias

### Front-end

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- Apache ECharts
- TanStack Table

### Data Pipeline

- Python
- nba_api
- pandas

### Deploy

- GitHub
- GitHub Actions
- Vercel

---

## Estrutura do Projeto

```
processhoops-analytics/

docs/
data/
pipeline/
public/
src/

.gitignore
CLAUDE.md
README.md
```

---

## Documentação

Toda a documentação do projeto encontra-se na pasta `docs`.

- 01-vision.md
- 02-requirements.md
- 03-architecture.md

O arquivo `CLAUDE.md` contém as diretrizes para desenvolvimento utilizando Claude Code.

---

## Filosofia

O processhoops analytics segue um princípio simples:

> O Python pensa. O Front-end apresenta.

Toda a lógica de negócio é processada no pipeline de dados.

A aplicação web concentra-se exclusivamente em oferecer uma experiência rápida, limpa e agradável para o usuário.

---

## Roadmap

Versão 1.0

- Estrutura base do projeto
- Pipeline automático
- Dashboard inicial
- Página de equipes
- Página de jogadores
- Scatter Plot
- Comparador

Versões futuras

- Novas ligas
- Novas métricas
- Comparações históricas
- Dashboards personalizados
- Mais fontes de dados

---

## Licença

Projeto desenvolvido para fins de estudo, aprendizado e exploração de dados públicos da NBA.

Todos os dados pertencem aos seus respectivos proprietários.