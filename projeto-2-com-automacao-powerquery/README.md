# Projeto 2 — Painel do Censo Escolar 2024

## Sobre o projeto

Este projeto foi desenvolvido pelo Grupo 4 para a disciplina de **Análise de Dados para Pesquisas em Políticas Públicas**.

O objetivo foi construir, no Microsoft Excel, um painel interativo a partir dos **Microdados do Censo Escolar 2024**, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

A base contempla escolas de diferentes dependências administrativas — federal, estadual, municipal e privada. O tratamento dos dados foi realizado por meio do Power Query, com utilização de parâmetros de UF e município e integração de tabelas auxiliares.

## Como usar

1. Baixe o arquivo Excel da versão atualizada do Projeto 2 e abra-o no Excel.
2. Na aba `Parâmetros`, preencha os campos **UF** e **Município**. Por exemplo, informe `SP` em **UF** e `Osasco` em **Município**.
3. Na faixa de opções do Excel, vá em **Dados → Atualizar Tudo** e aguarde o fim da atualização.
4. Volte ao painel para ver os dados do município selecionado. Para consultar outro município, altere os campos na aba `Parâmetros` e clique novamente em **Dados → Atualizar Tudo**.

## O que mudou em relação à versão anterior

A versão anterior usava uma base restrita a São Paulo. Na versão atualizada, substituímos essa base pelos dados nacionais do Censo Escolar 2024. Os valores de UF e município preenchidos na aba `Parâmetros` são usados pelo Power Query para selecionar os registros em que os dois campos coincidem, por meio de uma junção interna (`Inner Join`). Quando o usuário clica em **Dados → Atualizar Tudo**, a consulta aplica o recorte e atualiza os dados usados no painel.

---

## Tratamento dos dados

Os Microdados do Censo Escolar 2024 foram importados e tratados por meio do **Power Query**.

Durante o tratamento, foram utilizadas tabelas auxiliares para identificação de:

- Dependência administrativa;
- Localização;
- Localização diferenciada;
- Situação de funcionamento.

Também foram criadas classificações e indicadores para facilitar a análise dos dados, incluindo:

- Tamanho da escola;
- Abastecimento de água;
- Fonte de energia;
- Esgotamento sanitário;
- Destinação do lixo.

### Parâmetros

O projeto utiliza parâmetros de **UF e município** como parte da organização e filtragem da base de dados utilizada no painel.

<img width="2204" height="1466" alt="image" src="https://github.com/user-attachments/assets/c6b46d03-a3e1-4da2-a080-401c72ac22aa" />

---

## Dashboard

O dashboard foi desenvolvido para apresentar as informações do Censo Escolar de maneira visual e interativa, facilitando a análise de características das escolas e das matrículas.

Entre as informações apresentadas estão:

- Dependência administrativa;
- Matrículas por etapa de ensino;
- Distribuição das escolas por tamanho;
- Matrículas por gênero;
- Matrículas por faixa etária;
- Matrículas por raça/cor.

### Visão geral do dashboard

<img width="2284" height="1254" alt="image" src="https://github.com/user-attachments/assets/f9e5dc8f-ad4f-4a77-bbc2-d9fd956e6cce" />

---

## Segmentações de dados

Foram utilizadas segmentações de dados para permitir diferentes recortes das informações apresentadas no painel.

As segmentações possibilitam a aplicação de filtros relacionados às características das escolas e da infraestrutura disponível na base.

Entre as categorias utilizadas estão:

- Localização;
- Dependência administrativa;
- Tamanho da escola;
- Água;
- Energia;
- Esgoto.

### Segmentações do painel

<img width="906" height="1266" alt="image" src="https://github.com/user-attachments/assets/eef5df46-3dd4-45e3-8d82-35097b809123" />

<img width="918" height="728" alt="image" src="https://github.com/user-attachments/assets/22a0eedb-2901-42d2-a3b0-d2c37495ae57" />

Os filtros permitem explorar diferentes recortes dos dados diretamente no dashboard.

### Exemplo de aplicação dos filtros

<img width="2224" height="1220" alt="image" src="https://github.com/user-attachments/assets/8fc2d635-c10f-4b4e-857c-9115c0dd8096" />

---

## Fonte dos dados

Os dados utilizados são provenientes dos **Microdados do Censo Escolar 2024**, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).

Fonte oficial:  
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data
---

## Uso de Inteligência Artificial

### Ferramenta utilizada

ChatGPT (OpenAI).

### Para que foi utilizada

A ferramenta de Inteligência Artificial foi utilizada como apoio na organização e revisão das informações do projeto e na elaboração e estruturação do README.

### Exemplo de prompt utilizado

> "Organize uma descrição para um dashboard construído no Excel com dados do Censo Escolar sobre as escolas de São Paulo, explicando os filtros, gráficos e principais informações apresentadas."

O conteúdo gerado foi revisado e adaptado pelo grupo de acordo com as características do projeto desenvolvido.

---

## Observações sobre os dados

Os resultados apresentados no painel dependem das informações disponibilizadas na base original do Censo Escolar 2024 e do tratamento realizado no projeto.

Valores ausentes ou categorias sem informação podem aparecer no painel como valores não informados ou em branco.

O projeto possui finalidade acadêmica e foi desenvolvido como exercício de tratamento, análise e visualização de dados públicos.

---

### O que o grupo aprendeu

Aprendemos a trabalhar com uma base nacional no Power Query e a filtrar os dados antes de carregá-los no painel. Usamos duas células nomeadas no Excel para definir a UF e o município e aplicamos uma junção interna para manter os registros que correspondem aos dois valores. Também aprendemos a combinar a base do Censo com tabelas auxiliares e a atualizar o painel a partir dos parâmetros escolhidos. Com isso, a mesma planilha pode ser usada para consultar municípios diferentes.

## Participação do grupo

### Alexandre Jubram
Participou da organização da base de dados e da revisão das variáveis utilizadas na construção dos indicadores e das visualizações.

### Bettina Kalassa
Participou da estruturação das tabelas dinâmicas e da organização dos indicadores utilizados no dashboard.

### Izabel Born
Participou da construção e organização das visualizações, dos gráficos e dos elementos do dashboard.

### Maria Eduarda Pereira
Participou da atualização do tratamento dos dados, da inclusão e revisão dos indicadores de infraestrutura, dos ajustes nas segmentações e visualizações do dashboard e da atualização da documentação do projeto.

### Maria Thereza Favaro
Participou da revisão do dashboard, da organização visual do painel e da verificação dos filtros e segmentações utilizados.

### Yuri Neres
Participou da conferência dos dados e indicadores, dos testes das funcionalidades do painel e da revisão final do projeto.
