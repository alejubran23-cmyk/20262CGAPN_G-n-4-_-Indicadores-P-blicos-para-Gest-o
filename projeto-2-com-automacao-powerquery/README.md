Painel do Censo Escolar 2024 com Power Query
Objetivo
O projeto apresenta um dashboard interativo construído no Excel a partir dos Microdados do Censo Escolar 2024, disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP).
Nesta versão, o projeto foi atualizado para utilizar a base nacional completa do Censo Escolar, contendo municípios de todo o Brasil. O tratamento dos dados é realizado no Power Query, que filtra a base de acordo com a UF e o Município definidos pelo usuário, permitindo que o dashboard trabalhe apenas com os dados do município selecionado.
Além da identificação e localização das escolas, foram incorporadas informações sobre dependência administrativa, tamanho da escola, localização diferenciada, situação de funcionamento e condições de infraestrutura, incluindo abastecimento de água, energia, esgoto e destinação do lixo.
O dashboard permite analisar diferentes características das escolas e das matrículas de forma dinâmica, utilizando tabelas e gráficos dinâmicos conectados a segmentações de dados.
Como usar
Abra o arquivo:
Projeto2_Painel_Censo_PowerQuery_Grupo 4.xlsx
Na aba Parâmetros, informe:
- UF: sigla do estado desejado;
- Município: nome do município que será analisado.
Após alterar o município, acesse a guia Dados do Excel e clique em Atualizar Tudo.
O Power Query utiliza os valores informados em Parâmetros para filtrar a base nacional do Censo Escolar e carregar somente os registros correspondentes ao município escolhido.
As tabelas dinâmicas e os gráficos do DASH DA EDUCAÇÃO são então atualizados com os novos dados.
📸 PRINT 1 — COLOCAR AQUI
Tire um print da aba Parâmetros mostrando a tabelinha com UF e Município.
Exemplo: SP | São Paulo.
Legenda que você pode colocar embaixo da imagem:
Seleção do município: a UF e o Município informados na aba Parâmetros são utilizados pelo Power Query para definir o recorte apresentado no dashboard.

Tratamento dos dados com Power Query
A principal atualização desta versão do projeto foi a substituição da base anteriormente utilizada, restrita a São Paulo, pela base nacional completa do Censo Escolar 2024.
No Power Query, foi criada uma consulta de filtro a partir dos campos UF e Município definidos na planilha.
A consulta principal foi combinada com esse filtro por meio de uma Junção Interna (Inner Join), utilizando simultaneamente os campos de UF e Município. Dessa forma, embora a fonte original contenha escolas de todo o Brasil, apenas os registros referentes ao município selecionado são carregados para análise.
Também foram realizadas Junções Esquerdas (Left Join) com as tabelas auxiliares de:
- Dependência administrativa;
- Localização;
- Localização diferenciada;
- Situação de funcionamento.
Além disso, foram criadas colunas condicionais para facilitar a análise dos dados no dashboard:
- Tamanho da Escola;
- Água;
- Energia;
- Esgoto;
- Lixo.
Nos indicadores de infraestrutura, foi utilizada uma lógica de prioridade baseada nas variáveis binárias presentes nos microdados.
Dashboard
O DASH DA EDUCAÇÃO apresenta visualizações construídas a partir das tabelas dinâmicas conectadas à base tratada pelo Power Query.
O painel apresenta análises como:
- distribuição das escolas por dependência administrativa;
- distribuição das escolas por tamanho;
- matrículas por etapa de ensino e dependência administrativa;
- matrículas por gênero;
- matrículas por faixa etária;
- matrículas por raça/cor.
Também foram adicionadas segmentações de dados, permitindo combinar diferentes filtros e observar como os indicadores se modificam.
Entre os filtros disponíveis estão:
- Localização;
- Dependência administrativa;
- Tamanho da Escola;
- Água;
- Esgoto;
- Energia.
As segmentações estão conectadas às tabelas dinâmicas utilizadas pelos gráficos, permitindo que diferentes visualizações do dashboard sejam alteradas conjuntamente.
📸 PRINT 2 — COLOCAR AQUI
Tire um print bonito da aba DASH DA EDUCAÇÃO inteira, sem nenhum filtro estranho selecionado e mostrando os 6 gráficos + as segmentações.
Legenda:
Dashboard atualizado: visualizações e segmentações construídas a partir da base tratada pelo Power Query para o município selecionado.

Atualização automática por Município
Uma das principais funcionalidades implementadas nesta versão é a possibilidade de alterar o município analisado sem reconstruir manualmente o dashboard.
Por exemplo, ao informar Osasco/SP na aba Parâmetros e utilizar Atualizar Tudo, o Power Query filtra a base nacional e o dashboard passa a utilizar somente os registros correspondentes a Osasco.
Ao alterar novamente o parâmetro para São Paulo/SP e atualizar as consultas, as tabelas dinâmicas e os gráficos passam a apresentar os dados referentes ao município de São Paulo.
Esse processo permite reutilizar o mesmo painel para diferentes municípios a partir de uma única base nacional.
📸 PRINT 3 — COLOCAR AQUI
Aqui eu faria o print que realmente prova a automação.
Você tem duas opções; eu prefiro a Opção A:
Opção A — melhor:
Tire um print do dashboard com Osasco carregado. Como o Print 2 pode ser de São Paulo, fica visualmente evidente que os gráficos mudaram.
Legenda:
Teste de atualização automática: após alterar o município para Osasco/SP e utilizar a opção Atualizar Tudo, o dashboard é atualizado com os dados correspondentes ao novo município.

Não precisa colocar um print do Power Query aberto se esses três prints estiverem bons. O mais importante para o README é mostrar o resultado funcionando.
Uso de Inteligência Artificial
Para que foram utilizadas: as ferramentas de Inteligência Artificial foram utilizadas como apoio na organização e revisão das informações do projeto, na elaboração do texto explicativo do dashboard e na estruturação da documentação do projeto.
Fonte de Dados
Fonte oficial: Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) — Microdados do Censo Escolar 2024.
Link oficial:
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos
O que os dados representam: a base reúne informações sobre os estabelecimentos de ensino brasileiros registrados no Censo Escolar de 2024. Nesta versão do projeto, é utilizada a base nacional completa, e o recorte do município é realizado dentro do Power Query de acordo com os parâmetros definidos pelo usuário.
Estrutura dos principais dados
Variável	Descrição
SG_UF	Sigla da Unidade da Federação
NO_MUNICIPIO	Município em que a escola está localizada
NO_ENTIDADE	Nome da escola/unidade educacional
TP_DEPENDENCIA / DEPENDENCIA.1	Dependência administrativa
TP_LOCALIZACAO / LOCALIZACAO.1	Localização urbana ou rural
TP_LOCALIZACAO_DIFERENCIADA	Identificação de localização diferenciada
SITUACAO.1	Situação de funcionamento da escola
QT_MAT_BAS	Quantidade de matrículas da educação básica
Tamanho Escola	Classificação da escola de acordo com a quantidade de matrículas
Água	Forma de abastecimento de água identificada na escola
Energia	Forma de fornecimento de energia
Esgoto	Forma de esgotamento sanitário
Lixo	Forma de destinação do lixo


Além dessas variáveis, o dashboard utiliza informações de matrículas por etapa de ensino, gênero, faixa etária e raça/cor.
Participação do Grupo
O que aprendemos com este projeto: aprendemos a trabalhar com uma base de dados de abrangência nacional utilizando o Power Query, aplicando filtros antes do carregamento dos dados para reduzir o volume processado pelo dashboard. Também praticamos junções entre diferentes tabelas, criação de colunas condicionais, tabelas e gráficos dinâmicos, segmentações de dados e atualização automática das visualizações a partir da mudança dos parâmetros de UF e Município.
A atividade também permitiu compreender como estruturar um dashboard reutilizável, no qual o mesmo conjunto de visualizações pode ser aplicado a diferentes municípios sem a necessidade de reconstruir manualmente as análises.
Papel de cada integrante
Integrante	Papel
Alexandre Jubram	Criação do repositório do projeto e organização das pastas do grupo
Bettina Kalassa	Upload dos arquivos e colaboração na documentação dos projetos
Izabel Born	Upload dos arquivos e revisão dos dados e disclaimers
Maria Eduarda Pereira	Atualização do Projeto 2 com a base nacional no Power Query, organização das tabelas e gráficos dinâmicos, segmentações e atualização do README
Maria Thereza Favaro	Revisão da estrutura e dos dados utilizados no Projeto 2
Yuri Neres	Reunião dos prints e organização das evidências para a entrega no eClass
