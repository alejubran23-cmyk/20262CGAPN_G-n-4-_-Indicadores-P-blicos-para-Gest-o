# Simulador de Repasse do PNAE em Python

**20262CGAPN_G-n-4 – Indicadores Públicos para Gestão**

## Objetivo

O simulador calcula, no terminal, o repasse anual do Programa Nacional de Alimentação Escolar (PNAE) para uma escola, a partir das matrículas de creche, pré-escola e ensino fundamental, dos valores per capita de 2026 e dos dias letivos. Ele também classifica o porte da escola e estima quanto do custo dos alimentos da merenda o repasse federal consegue cobrir.

É a versão em Python do simulador que o grupo construiu em Excel no Projeto 1. Neste projeto, o programa ganhou o cálculo de cobertura do custo dos alimentos e foi aplicado a uma escola real da rede municipal de São Paulo, a EMEF Dilermando Dias dos Santos.

## Como usar

1. Tenha o Python 3 instalado no computador. O programa não usa bibliotecas extras.
2. Baixe o arquivo `simulador_pnae.py` desta pasta.
3. Abra o terminal na pasta onde está o arquivo e execute:

   ```bash
   python simulador_pnae.py
   ```

   Se o comando `python` não for reconhecido, tente `py simulador_pnae.py` no Windows ou `python3 simulador_pnae.py` no Mac.

4. Responda às perguntas do programa:

   | Pergunta | O que digitar |
   |---|---|
   | Nome da escola | O nome da escola que você quer simular |
   | Dias letivos no ano | Um número inteiro. Use `200` para reproduzir os exemplos deste projeto |
   | Matrículas na creche | Um número inteiro igual ou maior que zero |
   | Matrículas na pré-escola | Um número inteiro igual ou maior que zero |
   | Matrículas no ensino fundamental | Um número inteiro igual ou maior que zero |

   Digite `0` quando a escola não tiver matrículas em uma etapa. Se você digitar letras, um número negativo ou um valor com vírgula, o programa pedirá o número novamente.

5. O programa mostra o total de matrículas, o porte, o repasse por etapa e o repasse total. Também exibe o custo anual estimado dos alimentos, o percentual coberto pelo repasse federal e a diferença a ser coberta por outras fontes.

## Prints do resultado

### Escola real — EMEF Dilermando Dias dos Santos

<img width="1182" height="854" alt="image" src="https://github.com/user-attachments/assets/946e6f94-acd4-47db-ab00-5f217a81d112" />

Com 200 dias letivos e 625 matrículas no ensino fundamental, o repasse anual é de **R$ 71.250,00**. O custo anual estimado dos alimentos é de **R$ 450.000,00**, e o repasse federal cobre **15,8%** desse custo.

### Conferência com o Projeto 1

<img width="1186" height="832" alt="image" src="https://github.com/user-attachments/assets/2dcda14b-2c90-440b-bd08-0cd1d0a082a4" />

Com os dados do Projeto 1 (200 dias letivos, 60 matrículas na creche, 80 na pré-escola e 50 no ensino fundamental), o programa reproduz o repasse anual de **R$ 37.660,00** e a classificação de porte **Pequena**, os mesmos resultados da planilha.

## Escola simulada

| Informação | Valor |
|---|---|
| Nome | EMEF Dilermando Dias dos Santos |
| Código INEP | 35053521 |
| Endereço | Rua Paulo Franco, 815, Vila Leopoldina, CEP 05305-031 |
| Município e UF | São Paulo, SP |
| Dependência administrativa | Municipal |
| Situação de funcionamento | Ativa |
| Matrículas na creche | 0 |
| Matrículas na pré-escola | 0 |
| Matrículas no ensino fundamental | 625 |

O grupo partiu do recorte do Censo Escolar 2024 usado no Projeto 2, na aba `microdados_ed_basica_2024` da planilha `DASHBOARD.EXCEL.xlsx`. A partir do recorte do município de São Paulo, filtramos as escolas de dependência municipal (`TP_DEPENDENCIA = 3`) e em atividade (`TP_SITUACAO_FUNCIONAMENTO = 1`). Entre elas, escolhemos a EMEF Dilermando Dias dos Santos.

As 625 matrículas no ensino fundamental vieram da variável `QT_MAT_FUND`. Como a escola tinha zero matrículas na educação infantil (`QT_MAT_INF = 0`), inserimos zero para creche e pré-escola. O recorte da planilha não trazia o código INEP. Por isso, consultamos o código no cadastro da escola e conferimos se o endereço correspondia ao da base do Censo.

## Custo dos alimentos

| Item | Informação |
|---|---|
| Valor adotado | **R$ 3,60 por refeição** em gêneros alimentícios |
| Fonte | Milena Ernandes Sanches e Tânia Muzy da Silva, *Análise dos gastos reais x repasse de verbas para a alimentação escolar de duas escolas estaduais do interior do Estado de São Paulo* |
| Período dos dados | Agosto a novembro de 2023 |
| Publicação | 17 de julho de 2025 |

[Resumo do estudo nos anais do Congresso Nacional de Alimentos e Nutrição](https://www.even3.com.br/anais/conan2025/1072522-analise-dos-gastos-reais-x-repasse-de-verbas-para-a-alimentacao-escolar-de-duas-escolas-estaduais-do-interior-do/)

Escolhemos essa referência porque o estudo mediu o gasto com os ingredientes de refeições servidas em duas escolas públicas paulistas. Esse é o custo que faz sentido comparar com o repasse federal do PNAE, destinado à compra de gêneros alimentícios. A estimativa exclui gastos com equipe, gás, equipamentos e estrutura das cozinhas.

- **Rede e município.** O estudo analisou escolas estaduais de uma cidade do interior paulista. A escola escolhida é municipal e fica na capital, onde os preços e os cardápios podem ser diferentes.
- **Ano.** Os dados de custo são de 2023, enquanto os valores do repasse aplicados na simulação são de 2026. Se os ingredientes custarem mais do que R$ 3,60 por refeição, a cobertura será menor do que a estimada.
- **Etapa de ensino.** O resumo do estudo não informa a etapa atendida. Os tipos de refeição e o tamanho das porções podem variar conforme o público escolar.

## Resultados e reflexão

| Indicador | EMEF Dilermando Dias dos Santos |
|---|---:|
| Total de matrículas | 625 |
| Porte | Grande |
| Repasse anual do PNAE | R$ 71.250,00 |
| Custo anual estimado dos alimentos | R$ 450.000,00 |
| Cobertura do repasse federal | 15,8% |
| Diferença a ser coberta por outras fontes | R$ 378.750,00 |

Na simulação, o repasse federal cobre uma parte do custo dos alimentos. Para cada aluno do ensino fundamental, o PNAE repassa R$ 0,57 por dia letivo. Com o custo estimado de R$ 3,60 por refeição, faltariam R$ 3,03 por aluno por dia, o equivalente a R$ 378.750,00 no ano.

A nota técnica do Todos Pela Educação (2023) explica que a atualização dos valores per capita é necessária para recompor o poder de compra do programa e aponta outros desafios do seu desenho. O Observatório da Alimentação Escolar (2025) discute como a falta de reajuste dificulta o cumprimento de metas como ampliar as compras da agricultura familiar e reduzir a presença de ultraprocessados. A reportagem do Brasil de Fato (2025) mostra que a capacidade de complementar o repasse varia entre as redes.

Quando o estado ou o município não consegue cobrir a diferença, a escola pode ter menos recursos para manter a variedade e a qualidade das refeições. Isso pode levar a cardápios mais repetitivos, porções menores e menor oferta de alimentos frescos. Como muitos alunos dependem da merenda para fazer uma de suas principais refeições do dia, essas mudanças podem afetar sua segurança alimentar. Redes com menor capacidade de complementar o repasse enfrentam mais dificuldade para manter a qualidade da alimentação escolar.

**Simplificações do simulador**

- As matrículas são do Censo Escolar de 2024 e os valores per capita são de 2026.
- O cálculo considera apenas creche, pré-escola e ensino fundamental, sem aplicar valores diferenciados por modalidade ou jornada.
- A estimativa supõe uma refeição por aluno por dia letivo.
- O custo por refeição é uma referência de 2023, obtida em outra rede e em outro município.

**Leituras utilizadas**

- [Todos Pela Educação — Nota técnica sobre a recomposição orçamentária e o fortalecimento do PNAE (2023)](https://todospelaeducacao.org.br/wordpress/wp-content/uploads/2023/03/nota-pnae-reajuste-nos-valores-do-programa-nacional-de-alimentacao-escolar.pdf)
- [Observatório da Alimentação Escolar — Apesar de ousadas novas metas, ausência de reajuste ameaça a alimentação escolar (2025)](https://alimentacaoescolar.org.br/noticias/2025/10/21/apesar-de-ousadas-novas-metas-ausencia-de-reajuste-ameaca-a-alimentacao-escolar/)
- [Brasil de Fato — Alimentação escolar: Brasil ainda enfrenta desafio do financiamento, diz estudo (2025)](https://www.brasildefato.com.br/podcast/bem-viver/2025/10/16/alimentacao-escolar-brasil-ainda-enfrenta-desafio-do-financiamento-diz-estudo/)

## Organização do programa

O arquivo segue a organização vista em aula. Os parâmetros ficam no topo, seguidos pelas funções e pelo programa principal, que recebe os dados e mostra os resultados.

| Parte do programa | O que faz | Correspondência no Projeto 1 (Excel) |
|---|---|---|
| Parâmetros | Guardam os valores per capita e o custo dos alimentos por refeição. As fontes aparecem em comentários no código. | Os valores per capita correspondem às células B5 a B7 da aba `Parametros_PNAE`. O custo dos alimentos foi acrescentado no Projeto 3. |
| `ler_numero` | Pede um número ao usuário e repete a pergunta até receber um número inteiro válido. | Preenchimento das entradas na aba `Simulador_Escola`. |
| `calcular_repasse` | Multiplica as matrículas de cada etapa pelo valor per capita e pelos dias letivos e soma os repasses. | Cálculo do repasse anual total na célula B21 da aba `Simulador_Escola`. |
| `classificar_porte` | Classifica a escola em Pequena (até 200 matrículas), Média (201 a 400) ou Grande (acima de 400). | Classificação exibida na célula B19 da aba `Simulador_Escola`, com as faixas da aba `Parametros_PNAE`. |
| `calcular_cobertura` | Calcula o custo anual dos alimentos, a cobertura do repasse e a diferença. Quando o repasse é igual ou superior ao custo, a diferença é zero. | Função acrescentada no Projeto 3. |
| `formata_reais` | Mostra os valores no formato de moeda brasileira. | Formatação de moeda das células da planilha. |
| Programa principal | Faz as perguntas, chama as funções e mostra os resultados no terminal. | Equivale ao uso da aba `Simulador_Escola` como um todo. |

## Uso de Inteligência Artificial

**Ferramentas utilizadas**

Claude e ChatGPT.

**Para que foram utilizadas**

As ferramentas foram utilizadas como apoio na organização do código em Python, na elaboração e no teste do cálculo de cobertura do repasse e na revisão do README.

**Exemplo de prompt utilizado**

> esse simulador ta pronto? essa é uma das partes do projeto 3, certo? tem tudo que a pro pediu?

**O que foi ajustado manualmente**

Na revisão do simulador, retomamos a orientação da professora de que o programa deve informar quando o repasse federal cobre todo o custo dos alimentos. Pedimos ao Claude que testasse o caso em que os dois valores são iguais. O teste mostrou que a tela já exibia 100,0% de cobertura e R$ 0,00 de diferença, mas a mensagem exigida ainda não aparecia. O Claude ajustou o arredondamento dos dois valores para centavos antes da comparação. Depois, conferimos a versão atualizada com apoio do ChatGPT e verificamos que a mensagem passou a aparecer e que o exemplo do Projeto 1 continuou retornando R$ 37.660,00 e porte Pequena.

## Fonte de Dados

O Censo Escolar 2024, do INEP, reúne informações de identificação, funcionamento e matrículas das escolas. A Resolução CD/FNDE nº 1/2026 informa os valores por aluno e por dia letivo usados no cálculo do repasse federal.

- [Microdados do Censo Escolar — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)
- [Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026](https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf)

| Variável do Censo | Significado |
|---|---|
| `NO_ENTIDADE` | Nome da escola |
| `NO_MUNICIPIO` | Município da escola |
| `TP_DEPENDENCIA` | Dependência administrativa. Os códigos são 1 para federal, 2 para estadual, 3 para municipal e 4 para privada |
| `TP_SITUACAO_FUNCIONAMENTO` | Situação de funcionamento. O código 1 indica escola em atividade |
| `QT_MAT_INF` | Total de matrículas na educação infantil, incluindo creche e pré-escola |
| `QT_MAT_FUND` | Total de matrículas no ensino fundamental |

A referência de custo dos alimentos é o estudo de Sanches e Silva, publicado em julho de 2025, com dados de agosto a novembro de 2023. [Resumo do estudo](https://www.even3.com.br/anais/conan2025/1072522-analise-dos-gastos-reais-x-repasse-de-verbas-para-a-alimentacao-escolar-de-duas-escolas-estaduais-do-interior-do/)

## Participação do Grupo

**O que aprendemos com este projeto**

Aprendemos a passar para Python a lógica que tínhamos usado no Excel, separando os parâmetros, as funções e as perguntas ao usuário. Ao aplicar o simulador a uma escola real, aprendemos a identificar as matrículas no Censo Escolar e a avaliar se uma referência de custo de outra rede e de outro ano é adequada para a estimativa. Também conseguimos calcular, para uma escola concreta, quanto do custo dos alimentos seria coberto pelo repasse federal e quanto dependeria de outras fontes.

**Papel de cada integrante**

| Integrante | Papel no projeto |
|---|---|
| Alexandre Jubram | Seleção da escola no Censo Escolar 2024, levantamento das matrículas por etapa e registro dos filtros usados para localizar os dados. |
| Bettina Kalassa | Pesquisa do custo dos alimentos por refeição, escolha da referência de R$ 3,60 e elaboração da justificativa para usar esse valor na simulação. |
| Izabel Born | Adaptação do simulador da Aula 18 para o Projeto 3, organização dos parâmetros e das funções em Python e integração do cálculo de cobertura ao programa. |
| Maria Eduarda Pereira | Teste do simulador com os dados do Projeto 1 e da escola escolhida, conferência dos resultados com as orientações da professora e verificação do caso em que o repasse cobre exatamente o custo dos alimentos. |
| Maria Thereza Favaro | Organização da tabela de resultados e elaboração da reflexão sobre o que a cobertura estimada representa para a escola, com base nas leituras indicadas. |
| Yuri Neres | Elaboração da seção “Como usar”, captura dos prints do terminal e organização da pasta do Projeto 3 no GitHub, com o link na página inicial do repositório. |
