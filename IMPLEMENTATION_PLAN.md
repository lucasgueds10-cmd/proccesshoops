# IMPLEMENTATION_PLAN.md — Sprint 0

Status: aguardando aprovação. Nenhum código foi criado ainda.

Este documento detalha a Sprint 0, cujo único objetivo é **validar o risco
técnico crítico identificado na análise de arquitetura** (confiabilidade da
`nba_api` rodando dentro de runners hospedados do GitHub Actions) e deixar de
pé o esqueleto mínimo, ponta a ponta, do pipeline automatizado:

`nba_api → Python → JSON → GitHub → Vercel → usuário`

Nenhuma feature de produto (Home, Teams, Players etc.) é construída aqui.
Isso começa na Sprint 1.

---

## 0. Pré-requisitos (ações fora do meu controle)

Antes de eu poder implementar, algumas coisas dependem de você, pois exigem
login em contas externas:

1. **Inicializar o repositório Git local e criar o repositório remoto no
   GitHub.** A pasta atual ainda não é um repositório Git. Eu posso rodar
   `git init` e os commits localmente, mas a criação do repositório remoto
   (`github.com/...`) e o primeiro `git push` para lá precisam da sua conta.
2. **Criar um projeto na Vercel apontando para esse repositório GitHub**
   (import do repo pela interface da Vercel).
3. **Gerar um Deploy Hook na Vercel** (Project Settings → Git → Deploy Hooks)
   e cadastrá-lo como um **GitHub Actions Secret** chamado
   `VERCEL_DEPLOY_HOOK_URL` no repositório.

Sem os itens 2 e 3, o pipeline e o commit automático funcionam normalmente,
mas o deploy final não é disparado automaticamente — nesse caso a Sprint 0
ainda pode ser validada localmente (`npm run dev`) enquanto isso é resolvido.

---

## 1. Estrutura completa de pastas (visão do projeto, não só desta sprint)

```
processhoops-analytics/
├── .github/
│   └── workflows/
│       └── update-data.yml
├── data/
│   └── nba/
│       └── 2025-26/                  # pasta por temporada (D4: pronto para múltiplas)
│           ├── standings.json
│           └── meta.json
├── docs/                              # já existente
├── pipeline/
│   ├── requirements.txt
│   ├── config.py
│   ├── nba_client.py
│   ├── models.py
│   ├── writer.py
│   ├── main.py
│   └── collectors/
│       └── standings.py
├── public/
│   └── images/                        # criado a partir da Sprint 1 (times) / Sprint 3 (jogadores) — ver seção 5
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   ├── components/
│   │   └── standings/
│   │       └── standings-table.tsx
│   ├── lib/
│   │   ├── data.ts
│   │   └── utils.ts
│   └── types/
│       └── standings.ts
├── components.json                    # config shadcn/ui
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
├── package.json
├── .gitignore                         # atualizado
├── CLAUDE.md
├── README.md
├── IMPLEMENTATION_PLAN.md             # este arquivo
└── analise-arquitetura-e-plano-sprints.txt
```

Pastas como `components/pages/hooks/services/types/utils` do doc de
arquitetura original estão representadas dentro de `src/` seguindo a
convenção nativa do Next.js App Router (`src/app` para rotas). `hooks/` e
`services/` serão criadas quando a primeira necessidade real aparecer
(Sprint 1 em diante) — não crio pastas vazias sem função na Sprint 0.

---

## 2. Bibliotecas

### Visão geral do projeto (algumas só entram em sprints futuras)
- **Front-end**: Next.js, React, TypeScript, Tailwind CSS, shadcn/ui, Apache
  ECharts (a partir da Sprint 4), TanStack Table (a partir da Sprint 2/3).
- **Pipeline**: Python, `nba_api`, `pandas` (a partir de domínios com
  processamento tabular mais pesado, ex. Sprint 2 em diante).

### Usadas especificamente nesta Sprint 0
- **Pipeline**:
  - `nba_api` — coleta de dados (`LeagueStandingsV3`).
  - `requests` — já é dependência da `nba_api`, usada diretamente no wrapper
    de retry/backoff.
  - `pydantic` — validação do schema de saída antes de gravar o JSON
    (implementa a exigência do doc de arquitetura: "validar respostas da
    API").
- **Front-end**:
  - `next`, `react`, `react-dom`, `typescript` — base do projeto.
  - `tailwindcss`, `postcss`, `autoprefixer` — estilos.
  - `shadcn/ui` (via `components.json` + `clsx`/`tailwind-merge` para o
    helper `cn()`) — configurado desde já para não retrabalhar em sprints
    futuras, mas nenhum componente visual complexo é instalado ainda.

Nenhuma biblioteca de export (xlsx), gráficos (ECharts) ou tabelas
(TanStack) entra nesta sprint — seriam complexidade prematura para o
objetivo de apenas validar o pipeline.

---

## 3. Arquivos criados na Sprint 0 e responsabilidade de cada um

### Pipeline (Python)

| Arquivo | Responsabilidade |
|---|---|
| `pipeline/requirements.txt` | Lista de dependências Python fixadas por versão. |
| `pipeline/config.py` | Constantes centrais: caminho de `data/`, cálculo da temporada atual da NBA (ex.: `2025-26`) a partir da data corrente, timeouts e número de tentativas de retry. |
| `pipeline/nba_client.py` | Wrapper fino sobre a `nba_api`: define headers recomendados (User-Agent/Referer), timeout e uma função de retry com backoff exponencial simples. Ponto único de contato com a API externa — se algo mudar (proxy, headers, etc.), muda só aqui. |
| `pipeline/models.py` | Modelo Pydantic (`TeamStanding`) descrevendo o formato validado de uma linha de standings. Se a API retornar um formato inesperado, a validação falha de forma explícita em vez de gerar um JSON corrompido. |
| `pipeline/collectors/standings.py` | Chama `nba_client`, busca `LeagueStandingsV3`, mapeia os campos da API para o modelo de `models.py` e devolve uma lista validada. Único responsável por "o que é standings". |
| `pipeline/writer.py` | Escreve `standings.json` de forma atômica (escreve em arquivo temporário e renomeia) e atualiza `meta.json` (timestamp da última execução, status `ok`/`error` por domínio). Se a coleta falhar, **não sobrescreve** os arquivos existentes — implementa a regra do doc de arquitetura de preservar o último dado válido. |
| `pipeline/main.py` | Orquestrador chamado pelo GitHub Actions (`python pipeline/main.py`). Chama o collector, trata exceções, aciona o writer e define o exit code do processo (não-zero em falha real, para que o GitHub Actions marque o workflow como falho e dispare o e-mail padrão — D5). |

### GitHub Actions

| Arquivo | Responsabilidade |
|---|---|
| `.github/workflows/update-data.yml` | Workflow com `schedule` (05:00 BRT / 08:00 UTC) e `workflow_dispatch` (permite rodar manualmente para validar). Passos: checkout → setup Python → instalar dependências → rodar `pipeline/main.py` → commit + push dos JSONs alterados → chamar o Vercel Deploy Hook (via secret `VERCEL_DEPLOY_HOOK_URL`). |

### Front-end (Next.js)

| Arquivo | Responsabilidade |
|---|---|
| `package.json`, `tsconfig.json`, `next.config.js`, `tailwind.config.ts` | Configuração padrão do projeto Next.js + TypeScript + Tailwind. Em `next.config.js` será adicionado `outputFileTracingIncludes` apontando para `data/**`, garantindo que a Vercel inclua os JSONs no deploy mesmo estando fora de `src/`. |
| `components.json` | Configuração base do shadcn/ui, para que comandos `npx shadcn add ...` funcionem a partir da Sprint 1 sem setup adicional. |
| `src/app/layout.tsx` | Layout raiz da aplicação (html/body, metadata básica, import do `globals.css`). Sem tema claro/escuro ainda — isso é requisito da Home (Sprint 1). |
| `src/app/globals.css` | Diretivas do Tailwind e tokens de cor base. |
| `src/app/page.tsx` | Página temporária (Server Component) que lê os standings via `src/lib/data.ts` e renderiza `standings-table.tsx`. Será substituída pela Home real na Sprint 1. |
| `src/lib/data.ts` | Função `getStandings()` que lê `data/nba/{temporada}/standings.json` do sistema de arquivos e retorna os dados tipados. Único ponto de acesso a dados no front-end — nenhum componente lê arquivo diretamente. |
| `src/lib/utils.ts` | Helper `cn()` padrão do shadcn/ui (merge de classes Tailwind). |
| `src/types/standings.ts` | Tipo TypeScript espelhando o modelo Pydantic de `pipeline/models.py`. (Observação: hoje mantido manualmente em sincronia; se o número de domínios crescer muito, uma geração automática de tipos a partir do schema pode ser avaliada — não necessária agora.) |
| `src/components/standings/standings-table.tsx` | Componente de apresentação simples da tabela de classificação, usando dados já prontos vindos de `data.ts`. Versão mínima — o refinamento visual completo (destaques de Playoff/Play-in, tooltips etc.) é da Sprint 1. |
| `.gitignore` (atualizado) | Ignorar `node_modules/`, `.next/`, `pipeline/.venv/` (ou `venv/`), `__pycache__/`, `.env*`. |

---

## 4. Fluxo completo da aplicação (Sprint 0)

1. O workflow `update-data.yml` dispara por `schedule` (05:00 BRT) ou
   manualmente (`workflow_dispatch`, usado para validar o risco 3.1).
2. O runner faz checkout do repositório, instala Python e as dependências de
   `pipeline/requirements.txt`.
3. Executa `python pipeline/main.py`.
4. `main.py` chama `collectors/standings.py`, que usa `nba_client.py` para
   buscar `LeagueStandingsV3` da `nba_api` (com headers e retry/backoff).
5. O resultado é validado contra `models.py` (Pydantic). Se inválido ou se a
   chamada falhar mesmo após as tentativas de retry, o erro é logado e
   `main.py` encerra com código de saída ≠ 0 — os arquivos antigos em
   `data/nba/{temporada}/` permanecem intactos.
6. Se tudo correr bem, `writer.py` grava `standings.json` e `meta.json`
   (status `ok`, timestamp) de forma atômica.
7. O workflow verifica se houve alteração nos arquivos; se sim, comita e faz
   push para o repositório (branch principal).
8. O workflow chama o Vercel Deploy Hook, disparando um novo build.
9. Na Vercel, o Next.js builda a aplicação; `src/app/page.tsx` lê
   `data/nba/{temporada}/standings.json` do sistema de arquivos via
   `src/lib/data.ts` (sem nenhuma chamada à `nba_api` a partir do
   navegador).
10. O usuário acessa a URL da Vercel e vê a tabela de standings com dados
    reais e atualizados — prova de que o fluxo ponta a ponta funciona de
    forma automatizada.

Em paralelo, o mesmo pipeline pode ser rodado localmente
(`python pipeline/main.py`) e a aplicação testada com `npm run dev`, lendo os
mesmos arquivos de `data/`.

---

## 5. Sobre imagens (D3) — decisão de escopo para esta Sprint

Você pediu que logos e fotos fiquem armazenados localmente no projeto.
Concordo com a abordagem e ela **não entra na Sprint 0**, pelos seguintes
motivos técnicos, que quero deixar explícitos antes de qualquer implementação
futura:

- **Fonte**: a `nba_api` não fornece os binários de imagem, apenas IDs. As
  URLs de imagem "oficiais" (`cdn.nba.com/headshots/...`,
  `cdn.nba.com/logos/...`) são convenções conhecidas pela comunidade, não
  documentação oficial — podem mudar sem aviso, então o pipeline precisa
  tratar falha de download como não-crítica (não deve derrubar a atualização
  inteira por causa de uma imagem faltando).
- **Cobertura incompleta**: nem todo jogador tem headshot disponível (ex.:
  novatos recém-draftados, jogadores em contrato two-way no início da
  temporada). É necessário um placeholder padrão como fallback.
- **Peso no repositório**: logos de times (30 arquivos, poucos KB cada) são
  desprezíveis. Fotos de jogadores (450+ arquivos) somam alguns MBs — aceitável,
  mas vale a pena otimizar formato/tamanho (ex.: redimensionar e usar WebP) em
  vez de guardar os arquivos originais em alta resolução.
- **Atualização incremental**: o pipeline deve baixar apenas imagens novas
  ou ausentes (diff por ID de jogador/time), nunca refazer o download de tudo
  todo dia.

Escopo planejado (fora desta sprint):
- **Sprint 1 (Home)**: download dos 30 logos de times, usados em "Próximos
  Jogos".
- **Sprint 3 (Players)**: download das fotos de jogadores, com placeholder de
  fallback.

Se preferir antecipar os logos de time já para a Sprint 0 (são poucos e o
risco é baixo), posso incluir — mas manteria fora por ora para não misturar
objetivos numa sprint que é puramente de validação técnica.

---

## 6. Critérios de aceite da Sprint 0

- [ ] `python pipeline/main.py`, executado localmente, gera
      `data/nba/{temporada}/standings.json` e `meta.json` válidos.
- [ ] O mesmo comando, executado dentro do workflow do GitHub Actions
      (runner hospedado), completa com sucesso em pelo menos **3 execuções
      consecutivas** via `workflow_dispatch` — validação prática do risco
      crítico 3.1 (confiabilidade da nba_api no runner).
- [ ] Uma falha simulada (ex.: endpoint indisponível/erro forçado) **não
      apaga** os dados válidos anteriores, e o workflow é marcado como
      "failed" no GitHub (validando o alerta por e-mail — D5).
- [ ] O workflow comita automaticamente os JSONs atualizados e chama o
      Vercel Deploy Hook.
- [ ] A aplicação publicada na Vercel exibe a tabela de standings com dados
      reais, lendo exclusivamente de `data/`, sem qualquer chamada à
      `nba_api` a partir do navegador.
- [ ] `npm run dev` local também funciona e exibe os mesmos dados.
- [ ] Nenhum segredo ou credencial exposto no front-end ou versionado no
      repositório (o Deploy Hook fica apenas como GitHub Secret).
- [ ] Ao final: decisão registrada sobre o risco 3.1 — runner hospedado é
      viável, ou precisamos revisitar D1.

---

## 7. Fora do escopo desta Sprint (deliberado)

- Qualquer UI final de Home (tema claro/escuro, KPIs, próximos jogos, busca
  global) — isso é Sprint 1.
- Download de imagens (ver seção 5).
- Múltiplos domínios de dados além de standings.
- Testes automatizados formais do pipeline — nesta fase a validação é
  manual/observacional (rodar o workflow repetidas vezes); uma suíte de
  testes pode ser avaliada mais adiante se o projeto crescer, sem
  necessidade agora.

---

Aguardando sua aprovação para iniciar a implementação da Sprint 0 conforme
descrito acima.
