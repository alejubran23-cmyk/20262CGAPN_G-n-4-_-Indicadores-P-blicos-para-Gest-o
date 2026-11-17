# Projeto 4 — Painel Interativo do Censo Escolar em Python

**Análise de Dados para Pesquisas em Políticas Públicas (CGAPN)**

## Objetivo

O painel permite explorar os dados do Censo Escolar 2024 de 3.110 escolas em atividade em 30 municípios de quatro regiões do estado de São Paulo. Os filtros permitem consultar o total de escolas e matrículas, comparar características e condições de infraestrutura e visualizar as escolas selecionadas no mapa e na tabela.

## Como usar

### Como abrir o painel

1. Tenha o Python 3 instalado no computador.
2. Baixe `painel.py` e `escolas_sp_regioes_2024_geo.csv` desta pasta e salve os dois arquivos juntos. Mantenha esses nomes, pois o programa procura o CSV pelo nome exato.
3. Abra o terminal na pasta onde salvou os arquivos. No Windows, abra a pasta no Explorador de Arquivos, clique na barra de endereço, digite `cmd` e pressione Enter.
4. Instale o pandas e o Streamlit:

   ```bash
   python -m pip install pandas streamlit
   ```

5. No mesmo terminal, execute:

   ```bash
   python -m streamlit run painel.py
   ```

   No Windows, se você usa `py` para abrir o Python, substitua `python` por `py` nos dois comandos. Se o painel não abrir automaticamente, copie o endereço que aparece ao lado de **Local URL** no terminal e cole no navegador. Mantenha o terminal aberto enquanto usa o painel.

### Como usar os filtros

Os sete filtros ficam **no topo da página**, acima dos indicadores. Se quiser analisar um município específico, escolha primeiro a **Região** e o **Porte** e depois abra **Escolha o município**. A lista de municípios acompanha as opções selecionadas. Os outros filtros são **Localização**, **Dependência administrativa**, **Água potável** e **Etapa de ensino**.

Os indicadores, os gráficos, o mapa e a lista de escolas **são atualizados automaticamente** quando você muda uma seleção. Role a página para consultar os gráficos e, abaixo deles, o mapa e a lista. Para voltar à visão geral, selecione **Todos** ou **Todas** em cada filtro.

**Exemplo para testar:** selecione **Litoral Norte** em Região, **Média** em Porte, **São Sebastião** em Município, **Sim** em Água potável e **Ensino Médio** em Etapa de ensino. Deixe Localização e Dependência administrativa em **Todas**. O painel deve mostrar **8 escolas e 2.363 matrículas**. Esse total reúne as matrículas de todas as etapas das oito escolas selecionadas. No gráfico por etapa, a barra do Ensino Médio mostra **1.423 matrículas**.

## O que mudou em relação às versões anteriores

| Versão | Base e funcionamento |
| --- | --- |
| Projeto 2 — Excel | A base de São Paulo foi substituída pela base nacional do Censo Escolar 2024. O recorte por UF e município era definido no Power Query. A opção **Atualizar Tudo** aplicava o novo recorte à planilha, que apresentava tabelas dinâmicas, gráficos dinâmicos e segmentações de dados. |
| Aula 21 — Streamlit | O painel inicial usava o CSV de 30 municípios paulistas. Já tinha um filtro por região, dois indicadores, gráficos de porte e de abastecimento de água, mapa e lista de escolas. |
| Projeto 4 — versão final | Mantivemos a base da Aula 21 e acrescentamos **seis filtros e sete gráficos**. O pandas filtra a base e calcula os resultados, e o Streamlit atualiza o painel no navegador a cada seleção. |

## Prints do resultado

### São Sebastião — escolas de médio porte com matrículas no Ensino Médio

Selecionamos **Litoral Norte**, porte **Média**, município **São Sebastião**, fornecimento de água potável **Sim** e etapa **Ensino Médio**. Localização e Dependência administrativa ficaram em **Todas**.

O painel mostrou **8 escolas e 2.363 matrículas**. O gráfico complementar detalha as matrículas das escolas selecionadas por etapa de ensino.

<img width="1600" height="783" alt="image" src="https://github.com/user-attachments/assets/968aeaf7-07b5-48be-9a19-e96a991814b0" />

<img width="1148" height="519" alt="image" src="https://github.com/user-attachments/assets/e1e0994a-e035-4369-ae0a-f38c44210d66" />

### Osasco — escolas estaduais urbanas de grande porte com matrículas no Ensino Fundamental

Selecionamos **Região Metropolitana de SP**, porte **Grande**, município **Osasco**, localização **Urbana**, dependência **Estadual**, fornecimento de água potável **Sim** e etapa **Ensino Fundamental**.

O painel mostrou **46 escolas e 52.298 matrículas**. No gráfico de destinação do lixo, **45 escolas** registraram coleta e **uma** registrou destino final público.

<img width="1600" height="819" alt="image" src="https://github.com/user-attachments/assets/b5de0037-b883-47a1-b8ce-d3b5af543405" />

<img width="878" height="405" alt="image" src="https://github.com/user-attachments/assets/9585dc71-ab58-4370-a431-7d282e44db10" />

## Elementos do painel

| Tipo | Elemento | Coluna usada e o que mostra |
| --- | --- | --- |
| Indicador | Quantidade de escolas | Conta as linhas da base que atendem aos filtros. Cada linha representa uma escola. |
| Indicador | Total de matrículas | Soma `matriculas`, o total de matrículas registrado em cada escola selecionada. |
| Filtro | Região | `regiao` identifica a região à qual pertence o município da escola. |
| Filtro | Porte | `porte` é calculado a partir de `matriculas`. A escola é pequena até 200 matrículas, média de 201 a 400 e grande acima de 400. |
| Filtro | Município | `municipio` identifica o município onde está a escola. |
| Filtro | Localização | `localizacao` indica se a escola está em área urbana ou rural. |
| Filtro | Dependência administrativa | `dependencia` indica se a escola é federal, estadual, municipal ou privada. |
| Filtro | Água potável | `agua_potavel` indica se a escola informa fornecer água potável. |
| Filtro | Etapa de ensino | `mat_infantil`, `mat_fundamental` e `mat_medio` registram as matrículas na Educação Infantil, no Ensino Fundamental e no Ensino Médio. A seleção mantém as escolas com pelo menos uma matrícula na etapa escolhida. |
| Gráfico | Escolas por porte | Conta as escolas por faixa de matrículas, usando `porte`. |
| Gráfico | Escolas por abastecimento de água | Conta as escolas por principal forma de abastecimento, usando `agua`. |
| Gráfico | Escolas por dependência administrativa | Conta as escolas por tipo de dependência, usando `dependencia`. |
| Gráfico | Escolas por fonte de energia | Conta as escolas por principal fonte de energia elétrica, usando `energia`. |
| Gráfico | Escolas por localização diferenciada | Conta as escolas por categoria de `loc_diferenciada`, como terra indígena, comunidade quilombola, comunidade tradicional ou assentamento. |
| Gráfico | Escolas por esgotamento sanitário | Conta as escolas por principal forma de esgotamento, usando `esgoto`. |
| Gráfico | Escolas por destinação do lixo | Conta as escolas por principal forma de destinação, usando `lixo`. |
| Gráfico | Escolas por localização urbana ou rural | Conta as escolas urbanas e rurais, usando `localizacao`. |
| Gráfico | Matrículas por etapa de ensino | Soma separadamente `mat_infantil`, `mat_fundamental` e `mat_medio` nas escolas selecionadas. O indicador geral soma o total registrado na coluna `matriculas`. |
| Mapa | Mapa das escolas | Usa `latitude` e `longitude` para representar as escolas selecionadas por pontos no mapa. |
| Tabela | Lista de escolas | Exibe `municipio`, `escola` (nome da escola), `matriculas` e `porte`. |

## O que o painel mostra

No recorte de São Sebastião, a seleção de escolas de médio porte com matrículas no Ensino Médio retornou **8 escolas e 2.363 matrículas**. Em Osasco, a seleção de escolas estaduais urbanas de grande porte com matrículas no Ensino Fundamental retornou **46 escolas e 52.298 matrículas**. Os totais correspondem às combinações de filtros mostradas nos prints e incluem todas as etapas das escolas selecionadas.

## Organização do programa

O `painel.py` começa com a função que classifica o porte das escolas. Em seguida, carrega o CSV e cria a coluna `porte`. Os filtros vêm antes dos indicadores, dos gráficos, do mapa e da lista, para que todos esses elementos usem o mesmo conjunto de escolas selecionadas.

| Parte do programa | O que faz | Correspondência com o Projeto 2 (Excel) |
| --- | --- | --- |
| Função `classifica_porte` | Classifica cada escola em pequena, média ou grande conforme o total de matrículas. | Segue a lógica de criar uma categoria a partir de uma variável da base. |
| Carregamento dos dados | O pandas lê o CSV e acrescenta a coluna `porte`. | Importação e preparação da base no Power Query. |
| Filtros | As caixas de seleção determinam quais escolas entram no recorte. | Seleção de recortes e segmentações de dados do painel. |
| Indicadores | Contam as escolas e somam as matrículas depois dos filtros. | Totais calculados a partir dos dados filtrados nas tabelas dinâmicas. |
| Gráficos | Contam escolas por categoria ou somam matrículas por etapa. | Gráficos dinâmicos que acompanham as seleções no painel. |
| Mapa | Mostra as escolas selecionadas a partir de suas coordenadas. | Visualização geográfica acrescentada no Projeto 4. |
| Lista de escolas | Exibe os registros que atendem aos filtros. | Consulta aos registros da base filtrada. |

## Uso de Inteligência Artificial

**Ferramenta utilizada**

ChatGPT.

**Para que foi utilizada**

O ChatGPT foi usado para elaborar o README, ajudar a localizar a fonte oficial dos dados do Censo Escolar e esclarecer dúvidas pontuais sobre o código, como a escolha de colunas para novos filtros e gráficos.

**Exemplo de prompt utilizado, com redação ajustada para clareza**

> Com base nas colunas do CSV, que filtro e que gráfico adicionais fariam sentido para o painel? 

**O que foi ajustado manualmente**

A partir do painel da Aula 21, foram acrescentados novos filtros e gráficos ao painel.py. As alterações foram aplicadas pelo grupo e testadas no Streamlit com diferentes combinações de filtros. Durante os testes, foi conferido se a quantidade de escolas, o total de matrículas e os gráficos eram atualizados a cada seleção. Para o README, foram escolhidos os recortes de São Sebastião e Osasco e feitas capturas dos filtros e dos indicadores de cada um. O recorte de São Sebastião foi acompanhado pelo gráfico de matrículas por etapa de ensino, e o de Osasco pelo gráfico de destinação do lixo.

## Fonte de Dados

A fonte oficial é o **Censo Escolar da Educação Básica de 2024**, do Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP). O arquivo `escolas_sp_regioes_2024_geo.csv`, adaptado para a atividade, reúne escolas em funcionamento de 30 municípios da Região Metropolitana de São Paulo, da Baixada Santista, do Litoral Norte e do Vale do Ribeira. Cada linha representa uma escola e reúne dados de matrículas, características, infraestrutura e coordenadas geográficas.

A tabela em [Elementos do painel](#elementos-do-painel) descreve as colunas usadas e o significado de cada uma.

[Microdados do Censo Escolar — INEP](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)

## Participação do Grupo

**O que aprendemos com este projeto**

Aprendemos a reproduzir em Python a lógica de filtragem que tínhamos usado no painel em Excel. Com o pandas, carregamos o CSV, criamos a coluna de porte e combinamos filtros antes de calcular contagens e somas. Com o Streamlit, aprendemos a ligar os filtros aos indicadores, aos gráficos, ao mapa e à tabela. O teste do filtro de etapa de ensino também ajudou a distinguir o total de matrículas das escolas selecionadas das matrículas de uma etapa específica.

**Papel de cada integrante**

| Integrante | Papel no Projeto 4 |
| --- | --- |
| Alexandre Jubram | Conferência da base do Censo Escolar, da cobertura dos municípios e das colunas descritas na seção de fonte de dados. |
| Bettina Kalassa | Revisão das categorias de infraestrutura e das descrições dos gráficos de água, energia, esgotamento sanitário e destinação do lixo. |
| Izabel Born | Revisão da organização do código e da correspondência entre o painel em Streamlit e os elementos do Projeto 2 em Excel. |
| Maria Eduarda Pereira | Adaptação do painel da Aula 21, inclusão dos filtros e gráficos, testes no Streamlit, seleção dos recortes e captura dos prints. |
| Maria Thereza Favaro | Conferência da descrição dos recortes de São Sebastião e Osasco e revisão da interpretação dos resultados apresentados no README. |
| Yuri Neres | Revisão das instruções de uso e organização dos arquivos, dos prints e dos links no repositório. |
