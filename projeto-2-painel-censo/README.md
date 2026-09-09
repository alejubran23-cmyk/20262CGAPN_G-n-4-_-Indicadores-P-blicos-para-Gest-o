# Dashboard de Escolas Municipais de São Paulo

## Objetivo

O projeto organiza, em uma planilha (`DASHBOARDEXCEL.xlsx`), a base de dados das escolas da rede municipal de São Paulo, com informações de identificação (nome da entidade, dependência administrativa), localização (endereço, bairro, zona urbana/rural, localização diferenciada como terra indígena) e demais variáveis do cadastro escolar.

A partir dessa base, o dashboard permite visualizar e filtrar as escolas por características como dependência, tipo de localização e bairro, servindo de apoio a análises sobre a distribuição da rede municipal de ensino na cidade.

## Como usar

Abra o arquivo `DASHBOARDEXCEL.xlsx`, que contém a aba com a base de dados bruta (uma linha por escola, com colunas de identificação e localização) e o painel/dashboard construído a partir dela.

> ⚠️ **[Grupo: completar]** Descrever aqui a ordem de abas do arquivo, quais filtros/segmentações de dados (slicers) devem ser ajustados antes de olhar os gráficos, e o que precisa ser preenchido ou selecionado para o painel atualizar — por exemplo, filtro de bairro, dependência ou tipo de localização.

## Uso de Inteligência Artificial

**Ferramenta utilizada:** [Grupo: preencher — ex.: Claude, ChatGPT, Copilot do Excel]

**Para que foi usada:** [Grupo: descrever o que foi de fato feito com apoio de IA neste projeto — por exemplo, limpeza/organização das colunas da base de dados, sugestão de fórmulas para os gráficos do dashboard, ou geração de texto explicativo. Se o dashboard foi construído manualmente no Excel, sem apoio de IA, registrar isso explicitamente aqui.]

**Exemplo de prompt utilizado:** [Grupo: colar aqui um prompt real usado pelo grupo, se houver]

**O que foi ajustado manualmente:** [Grupo: descrever os ajustes feitos depois da resposta da IA, como correção de colunas, conferência dos dados do Censo Escolar, ajustes de formatação dos gráficos, etc.]

## Fonte de Dados

**Fonte oficial:** [Grupo: confirmar — pelas colunas da base (`NO_MUNICIPIO`, `NO_ENTIDADE`, `TP_DEPENDENCIA`, `TP_LOCALIZACAO`, `TP_LOCALIZACAO_DIFERENCIADA`, `DS_ENDERECO`), os dados têm o formato dos microdados do Censo Escolar (INEP), provavelmente Censo Escolar 2024, filtrados para o município de São Paulo, rede Municipal]

**Link oficial:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data 

**O que os dados representam:**
A base reúne o cadastro de estabelecimentos de ensino da rede municipal de São Paulo, com uma linha por escola. Cada linha traz a identificação da unidade (nome, dependência administrativa), sua localização (endereço completo, bairro, zona urbana ou rural) e, quando aplicável, se está em localização diferenciada, como terra indígena. Essas informações permitem mapear e analisar como a rede municipal de ensino está distribuída pela cidade.

**Estrutura (principais colunas):**

| Coluna | Descrição |
|---|---|
| `NO_MUNICIPIO` | Município da escola (no caso, São Paulo) |
| `NO_ENTIDADE` | Nome da escola/unidade educacional |
| `TP_DEPENDENCIA` / `DEPENDENCIA` | Código e descrição da dependência administrativa (ex.: Municipal) |
| `TP_LOCALIZACAO` / `LOCALIZAÇÃO` | Código e descrição da zona (urbana ou rural) |
| `TP_LOCALIZACAO_DIFERENCIADA` / `LOC_DIFERENCIADA` | Indicam se a escola está em localização diferenciada, como terra indígena, e se essa condição se aplica |
| `DS_ENDERECO`, `NU_ENDERECO`, `DS_COMPLEMENTO` | Logradouro, número e complemento do endereço |
| `NO_BAIRRO` | Bairro onde a escola está localizada |

A planilha original possui outras colunas além dessas, usadas no dashboard para compor os gráficos e filtros.

> Demais colunas relevantes usadas no painel: matrículas, etapas de ensino ou indicadores calculados.

## Participação do Grupo

**O que aprendemos com este projeto:**
Aprendemos a organizar uma base de dados cadastral extensa (com centenas de escolas e dezenas de colunas) em um dashboard que resume as principais características da rede municipal de ensino, a diferenciar dados de identificação e localização, e a construir visualizações que facilitam a leitura de uma base originalmente extraída de um cadastro oficial e pouco amigável para leitura direta. Também aprendemos a importância de documentar a fonte e a estrutura dos dados para que qualquer pessoa, mesmo sem ter acompanhado a construção do dashboard, entenda o que cada informação representa.

**Papel de cada integrante:**

| Integrante | Papel |
|---|---|
| Alexandre Jubram | Criação do repositório do projeto e organização das pastas do grupo |
| Bettina Kalassa | Upload dos arquivos e redação do README do Projeto 1 (descrição e disclaimers) |
| Izabel Born | Upload dos arquivos e redação do README do Projeto 1, com revisão dos disclaimers de dados e de IA |
| Maria Eduarda Pereira | Upload dos arquivos do dashboard e redação da primeira versão do README do Projeto 2 (descrição e disclaimers) |
| Maria Thereza Favaro | Upload dos arquivos do dashboard e redação do README do Projeto 2, com revisão da estrutura e dos dados utilizados |
| Yuri Neres | Reunião dos prints do dashboard em funcionamento e registro da entrega no eClass |
