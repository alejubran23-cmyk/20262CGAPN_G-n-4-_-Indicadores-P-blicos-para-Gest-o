# Dashboard de Escolas Municipais de São Paulo

## Objetivo

O projeto organiza, em uma planilha (`DASHBOARDEXCEL.xlsx`), a base de dados das escolas da rede municipal de São Paulo, com informações de identificação (nome da entidade, dependência administrativa), localização (endereço, bairro, zona urbana/rural, localização diferenciada como terra indígena) e demais variáveis do cadastro escolar.

A partir dessa base, o dashboard permite visualizar e filtrar as escolas por características como dependência administrativa, tipo de localização e bairro, servindo de apoio a análises sobre a distribuição da rede municipal de ensino na cidade.

## Como usar

Abra o arquivo `DASHBOARDEXCEL.xlsx`, que contém a aba com a base de dados e o painel/dashboard construído a partir dela.

Ao abrir o arquivo, o usuário encontra a página inicial da planilha **“Dash da Educação”**, que apresenta os principais indicadores das escolas municipais de São Paulo. O dashboard possui um filtro de **Localização**, que permite selecionar entre **Rural** e **Urbana**.

A seleção do tipo de localização altera os resultados apresentados nos gráficos, permitindo comparar as características das escolas e das matrículas de acordo com sua localização.

## Resultados do Dashboard

A seguir, são apresentados os prints do dashboard em funcionamento, mostrando os resultados obtidos a partir da seleção do filtro de localização.

### Ao interagir com o gráfico e escolher — Localização Rural

Ao abrir a planilha, o dashboard apresenta inicialmente a opção **Rural** selecionada. Nesse resultado, são apresentados os indicadores referentes às escolas localizadas na zona rural, incluindo quantidade de escolas, distribuição por dependência administrativa, matrículas por etapa de ensino, tamanho das escolas, gênero, faixa etária e raça/cor.

<img width="1158" height="652" alt="image" src="https://github.com/user-attachments/assets/61247078-25e7-47e1-a6a1-91374fe9610d" />


### Ao selecionar — Localização Urbana

Ao selecionar a opção **Urbana** no filtro de localização, os gráficos são atualizados automaticamente, passando a apresentar os dados referentes às escolas localizadas na zona urbana.

<img width="1316" height="748" alt="image" src="https://github.com/user-attachments/assets/6286210c-3613-488a-937e-539f6b284869" />

Dessa forma, o dashboard permite observar como os indicadores educacionais se modificam de acordo com a localização das escolas, facilitando a análise e a interpretação dos dados do Censo Escolar.

## Uso de Inteligência Artificial

**Ferramentas utilizadas:** Claude e ChatGPT.

**Para que foram utilizadas:** as ferramentas de Inteligência Artificial foram utilizadas como apoio na organização e revisão das informações do projeto, na elaboração do texto explicativo do dashboard e na estruturação da documentação do projeto.

**Exemplo de prompt utilizado:**

> “Organize uma descrição para um dashboard construído no Excel com dados do Censo Escolar sobre as escolas municipais de São Paulo, explicando os filtros, gráficos e principais informações apresentadas.”

**O que foi ajustado manualmente:** os integrantes do grupo conferiram as informações, organizaram os dados no Excel, construíram e ajustaram os gráficos e filtros do dashboard e realizaram a conferência dos resultados apresentados.

## Fonte de Dados

**Fonte oficial:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), por meio dos microdados do Censo Escolar.

**Link oficial:** [INEP Data — Dados Abertos](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data?utm_source=chatgpt.com)

**O que os dados representam:** a base reúne informações sobre estabelecimentos de ensino da rede municipal de São Paulo, com uma linha por escola. Cada linha traz informações de identificação da unidade, dependência administrativa, localização, endereço e outras características utilizadas para a construção do dashboard.

### Estrutura dos principais dados

| Coluna                                             | Descrição                                           |
| -------------------------------------------------- | --------------------------------------------------- |
| `NO_MUNICIPIO`                                     | Município da escola (São Paulo)                     |
| `NO_ENTIDADE`                                      | Nome da escola/unidade educacional                  |
| `TP_DEPENDENCIA` / `DEPENDENCIA`                   | Dependência administrativa da escola                |
| `TP_LOCALIZACAO` / `LOCALIZAÇÃO`                   | Localização da escola: urbana ou rural              |
| `TP_LOCALIZACAO_DIFERENCIADA` / `LOC_DIFERENCIADA` | Indica se a escola está em localização diferenciada |
| `DS_ENDERECO`, `NU_ENDERECO`, `DS_COMPLEMENTO`     | Informações referentes ao endereço da escola        |
| `NO_BAIRRO`                                        | Bairro onde a escola está localizada                |

Além dessas informações, outras variáveis da base foram utilizadas para construir os indicadores apresentados no dashboard, como **matrículas, raça/cor, gênero, faixa etária, etapa de ensino e porte das escolas**.

## Participação do Grupo

**O que aprendemos com este projeto:** aprendemos a organizar uma base de dados cadastral extensa, com centenas de escolas e diversas variáveis, em um dashboard capaz de resumir as principais características da rede municipal de ensino. Também aprendemos a utilizar filtros e visualizações para facilitar a interpretação dos dados e a importância de documentar a fonte e a estrutura das informações utilizadas.

**Papel de cada integrante:**

| Integrante            | Papel                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Alexandre Jubram      | Criação do repositório do projeto e organização das pastas do grupo                                                |
| Bettina Kalassa       | Upload dos arquivos e redação do README do Projeto 1                                                               |
| Izabel Born           | Upload dos arquivos e redação do README do Projeto 1, com revisão dos dados e disclaimers                          |
| Maria Eduarda Pereira | Upload dos arquivos do dashboard e redação da primeira versão do README do Projeto 2                               |
| Maria Thereza Favaro  | Upload dos arquivos do dashboard e redação do README do Projeto 2, com revisão da estrutura e dos dados utilizados |
| Yuri Neres            | Reunião dos prints do dashboard em funcionamento e registro da entrega no eClass                                   |
