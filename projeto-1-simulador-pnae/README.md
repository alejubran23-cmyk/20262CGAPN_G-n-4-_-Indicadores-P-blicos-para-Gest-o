# Simulador de Repasse do PNAE

**20262CGAPN_G-n-4 – Indicadores Públicos para Gestão**

## Objetivo

O projeto simula, em uma página HTML interativa, o cálculo do repasse anual do Programa Nacional de Alimentação Escolar (PNAE) para uma escola municipal fictícia, a partir do número de matrículas por modalidade de ensino, do valor per capita diário de cada modalidade e dos dias letivos do ano.

O simulador também classifica a escola por porte, aplica uma regra didática de elegibilidade para complementação municipal e permite testar variações nas matrículas por meio de um fator de ajuste, reproduzindo em tempo real uma Tabela de Dados originalmente construída em Excel.

## Como usar

1. Abra a planilha `SimuladorExcel.xlsx`, que contém as abas:
   - **Parametros_PNAE**: valores per capita, dias letivos e faixas de porte.
   - **Simulador_Escola**: matrículas da escola, cálculo do repasse e tabela de cenários.

2. Abra o arquivo `simulador_pnae.html`, que reproduz o mesmo modelo em formato interativo:
   - Preencha o nome da escola, o bairro e as matrículas por modalidade.
   - O repasse, o porte e a elegibilidade são recalculados automaticamente.
   - No campo **"Fator de Ajuste"**, digite um percentual (ex.: `10` para +10%, `-10` para -10%) e observe o impacto sobre as matrículas ajustadas e o repasse.
   - O botão **"Próximo cenário"** percorre os cenários de -20% a +20%, em passos de 5 pontos percentuais, reconstruindo a Tabela de Dados.

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic)

**Para que foi usada:** gerar o artefato HTML interativo do simulador, transformando o modelo construído em Excel (abas `Parametros_PNAE` e `Simulador_Escola`) em uma página web com campos editáveis, cálculo automático do repasse (equivalente ao `SUMPRODUCT` de matrículas × valor per capita × dias letivos), classificação de porte, regra de elegibilidade com `SE` aninhado/`E`/`OU` e a simulação por fator de ajuste com o percurso dos cenários.

**Exemplo de prompt utilizado:**
> "Transforme esta planilha do simulador de repasse do PNAE, com as abas Parametros_PNAE e Simulador_Escola, em uma página HTML interativa. Mantenha os mesmos valores per capita, dias letivos e a fórmula de cálculo do repasse (matrículas × valor per capita × dias letivos). Inclua um campo de matrículas por modalidade editável, a classificação de porte da escola, a regra de elegibilidade para complementação municipal e um simulador com fator de ajuste que reproduza a Tabela de Dados de -20% a +20%, em passos de 5%."

**O que foi ajustado manualmente:**
- Conferência dos valores per capita e dos dias letivos gerados pela IA contra os valores originais da planilha (aba `Parametros_PNAE`).
- Revisão do texto dos avisos didáticos, para deixar claro que a escola, o nome, as matrículas e as faixas de porte/elegibilidade são fictícias e não correspondem a critérios oficiais do FNDE.
- Correção de arredondamentos na tabela de cenários do fator de ajuste.
- Ajustes de redação e formatação para deixar o simulador mais claro para quem não acompanhou a construção da planilha.

## Fonte de Dados

**Fonte oficial:** Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026, que altera a Resolução CD/FNDE nº 6, de 2020, com reajuste médio de 14,35% em relação a 2025 nos valores per capita do PNAE, em vigor desde a primeira parcela de 2026.

**Link oficial:** https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf/view

**O que os dados representam:**
Os dados oficiais utilizados são os valores per capita diários (em R$) pagos por modalidade de ensino (creche, pré-escola, fundamental, médio, EJA, indígena/quilombola e AEE em contraturno) e o número de dias letivos considerados no ano para o cálculo do repasse. Esses dois elementos, aplicados às matrículas de uma escola, permitem estimar o valor anual que ela receberia do PNAE.

Já a escola (EMEB Vila Quitaúna), o número de matrículas por modalidade, as faixas de porte (Pequena, Média, Grande) e a regra de elegibilidade para complementação municipal são **fictícios e didáticos**, criados apenas para exercitar o cálculo — não refletem uma escola real nem um critério oficial de classificação ou complementação do FNDE. O bairro (Quitaúna) e o município (Osasco/SP) são reais, usados apenas como ambientação do exercício.

**Estrutura (principais variáveis):**

| Variável | Descrição |
|---|---|
| Modalidade | Categoria de ensino |
| Valor per capita (R$/dia) | Valor oficial repassado por aluno/dia em cada modalidade |
| Dias letivos (ano) | Fixado em 200 |
| Matrículas | Número de alunos por modalidade, editável no simulador |
| Faixa de porte | Classificação didática da escola conforme o total de matrículas: até 200 = Pequena, de 201 a 400 = Média, acima de 400 = Grande |
| Fator de Ajuste | Percentual aplicado às matrículas base, na forma matrículas × (1 + fator), usado para simular cenários de -20% a +20% |

## Participação do Grupo

**O que aprendemos com este projeto:**
Aprendemos a estruturar um cálculo de política pública (o repasse do PNAE) a partir de dados oficiais, a organizar esse cálculo em uma planilha com parâmetros separados dos dados da escola, a construir uma Tabela de Dados para testar hipóteses de variação nas matrículas, e a transformar esse modelo em uma ferramenta interativa (HTML) com apoio de IA, revisando criticamente o que a ferramenta gerou. Também aprendemos a importância de documentar claramente o que é dado oficial e o que é suposição didática, para não passar a impressão de que regras fictícias (como porte e elegibilidade) são critérios reais do FNDE.

**Papel de cada integrante:**

| Integrante | Papel |
|---|---|
| Alexandre Jubram | Criação do repositório do projeto e organização das pastas do grupo |
| Bettina Kalassa | Upload dos arquivos da planilha e do simulador HTML; redação da primeira versão do README do Projeto 1 (descrição e disclaimers) |
| Izabel Born | Upload dos arquivos e redação do README do Projeto 1, com revisão dos disclaimers de dados e de IA |
| Maria Eduarda Pereira | Upload dos arquivos e redação do README do Projeto 2 (descrição e disclaimers) |
| Maria Thereza Favaro | Upload dos arquivos e redação do README do Projeto 2, com revisão da estrutura e dos dados utilizados |
| Yuri Neres | Reunião dos prints do simulador em funcionamento e registro da entrega no eClass |
