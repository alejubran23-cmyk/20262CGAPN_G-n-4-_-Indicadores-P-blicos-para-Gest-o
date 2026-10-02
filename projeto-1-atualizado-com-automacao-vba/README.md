# Projeto 1 — Simulador de Repasse do PNAE com Automação VBA

**20262CGAPN_G-n-4 – Indicadores Públicos para Gestão**

## Objetivo

Este projeto corresponde à atualização do **Projeto 1 — Simulador de Repasse do PNAE**, desenvolvido anteriormente pelo grupo, com a incorporação de uma automação em VBA para registrar e armazenar as simulações realizadas na planilha.

A automação permite guardar não apenas o resultado numérico de cada simulação, mas também informações que ajudam a compreender o contexto em que ela foi realizada, como a data e hora do registro, o Fator de Ajuste escolhido, o Racional da Taxa e o nome do usuário responsável pela simulação.

O arquivo-base fornecido para esta etapa já continha o campo **Racional da Taxa**, a aba `Banco_de_Dados` e a macro `RegistrarSimulacao`, responsável por validar e registrar os dados da simulação. A tarefa desenvolvida pelo grupo nesta atualização foi a implementação completa do campo **Usuário**, incluindo sua leitura, validação, gravação e limpeza por meio do código VBA.

## Como usar

1. Abra o arquivo `Simulador-PNAE-Monitorada_24_09. Grupo 4.xlsm` no Microsoft Excel.

2. Caso o Excel apresente um aviso de segurança, habilite a execução das macros para que o botão de registro funcione corretamente.

3. Na aba `Simulador_Escola`, informe os dados necessários para a simulação:
   - **Fator de Ajuste:** percentual utilizado para simular aumento ou redução das matrículas;
   - **Racional da Taxa:** justificativa para a escolha do Fator de Ajuste;
   - **Usuário:** nome da pessoa responsável pela simulação.

4. Observe os valores calculados de matrículas ajustadas e repasse ajustado.

5. Clique no botão **Salvar Simulação**.

6. A macro `RegistrarSimulacao` verifica se os campos necessários foram preenchidos corretamente. Caso algum campo obrigatório não esteja preenchido, o registro é interrompido e uma mensagem de erro é exibida.

7. Se os dados estiverem válidos, a simulação é registrada automaticamente na aba `Banco_de_Dados`.

8. Após o registro, os campos de entrada são limpos para permitir uma nova simulação.

### Informações registradas no Banco de Dados

| Campo | Descrição |
|---|---|
| ID | Identificador sequencial da simulação |
| Data/Hora | Momento em que a simulação foi registrada |
| Fator de Ajuste | Percentual aplicado às matrículas |
| Racional da Taxa | Justificativa para o fator escolhido |
| Total de Matrículas Ajustadas | Total de matrículas após a aplicação do fator |
| Repasse Ajustado | Valor estimado do repasse após o ajuste |
| Nome do usuário | Pessoa responsável pela realização da simulação |

## O que mudou em relação à versão anterior

A versão anterior do Projeto 1 permitia simular o repasse do PNAE e testar diferentes cenários de variação das matrículas por meio do Fator de Ajuste.

Nesta atualização, foi incorporada uma automação em VBA que permite manter um histórico das simulações realizadas.

O arquivo disponibilizado para a atividade já continha:

- o campo **Racional da Taxa**;
- a aba `Banco_de_Dados`;
- a macro `RegistrarSimulacao`;
- a leitura e validação do Fator de Ajuste e do Racional da Taxa;
- o registro das informações da simulação no banco de dados;
- a limpeza dos campos após o salvamento.

A implementação realizada pelo grupo nesta etapa acrescentou o campo **Usuário**, incluindo:

- criação do campo Usuário na aba `Simulador_Escola`;
- declaração da variável `usuario` no código VBA;
- leitura do nome informado no campo;
- inclusão do Usuário na função de validação;
- bloqueio do registro quando o campo Usuário está vazio;
- gravação do nome do usuário na coluna G da aba `Banco_de_Dados`;
- limpeza automática do campo Usuário após o registro de uma simulação.

## Uso de Inteligência Artificial

**Ferramenta utilizada:** ChatGPT.

**Para que foi utilizada:** a Inteligência Artificial foi utilizada apenas como apoio para compreender trechos mais complexos do código VBA já fornecido na atividade e entender a lógica de funcionamento da macro.

A implementação do campo Usuário, as alterações realizadas no arquivo e os testes da automação foram feitos manualmente no Microsoft Excel.

**Exemplo de prompt utilizado:**

> Explique de forma simples o que este trecho de código VBA faz e em qual parte do código o campo Usuário deve ser incluído, considerando a lógica de leitura, validação, gravação e limpeza já existente.

**O que foi ajustado manualmente:**

- criação do campo Usuário na aba `Simulador_Escola`;
- inclusão da variável `usuario` no código VBA;
- leitura do valor preenchido no campo;
- inclusão da validação do campo Usuário;
- gravação do nome do usuário na aba `Banco_de_Dados`;
- limpeza automática do campo após o registro;
- execução dos testes da automação.

## Dados

**Fonte oficial:** Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026, que altera a Resolução CD/FNDE nº 6, de 2020.

**Link oficial:**  
https://www.gov.br/fnde/pt-br/acesso-a-informacao/legislacao/resolucoes/2026/resolucao-cd_fnde-no-1-de-18-de-fevereiro-de-2026-dou-imprensa-nacional.pdf/view 

**O que os dados representam:** os dados utilizados no simulador incluem os valores per capita diários do PNAE por modalidade de ensino e o número de dias letivos considerados para estimar o repasse anual.

Os valores per capita são utilizados em conjunto com o número de matrículas de cada modalidade para estimar o valor anual do repasse.

A escola utilizada no exercício, o número de matrículas por modalidade, as faixas de porte e a regra de elegibilidade para complementação municipal possuem finalidade **fictícia e didática**. Essas informações foram utilizadas para a construção e teste do simulador e não representam critérios oficiais de classificação ou complementação do FNDE.

### Principais variáveis

| Variável | Descrição |
|---|---|
| Modalidade | Categoria de ensino |
| Valor per capita (R$/dia) | Valor considerado por aluno/dia em cada modalidade |
| Dias letivos | Número de dias considerados no cálculo anual |
| Matrículas | Número de alunos por modalidade |
| Fator de Ajuste | Percentual aplicado às matrículas para simular diferentes cenários |
| Racional da Taxa | Justificativa do usuário para o Fator de Ajuste escolhido |
| Usuário | Nome da pessoa responsável pela realização da simulação |
| Matrículas Ajustadas | Total de matrículas após a aplicação do Fator de Ajuste |
| Repasse Ajustado | Valor estimado do repasse após a aplicação do fator |

## Participação do Grupo

**O que aprendemos com este projeto:** nesta atualização, aprendemos a utilizar VBA para automatizar o registro de informações em uma planilha, relacionar campos da interface com uma aba utilizada como banco de dados e criar mecanismos de validação antes do armazenamento das informações.

Também foi possível compreender como uma automação pode transformar uma simulação isolada em um histórico de registros, permitindo consultar posteriormente não apenas os resultados obtidos, mas também quando a simulação foi realizada, qual Fator de Ajuste foi utilizado, qual foi o racional da decisão e quem realizou o registro.

### Implementação do campo Usuário

**Maria Eduarda Pereira** foi responsável pela implementação e pelos testes do campo Usuário nesta atualização do Projeto 1.

O campo foi inserido na aba `Simulador_Escola` e integrado à macro em quatro etapas:

1. **Leitura:** criação da variável `usuario` e leitura do nome informado no campo;
2. **Validação:** inclusão de uma verificação que impede o registro quando o campo Usuário está vazio;
3. **Gravação:** armazenamento do nome do usuário na coluna G da aba `Banco_de_Dados`;
4. **Limpeza:** exclusão automática do conteúdo do campo após uma simulação registrada com sucesso.

### Testes da automação

A automação foi testada com diferentes simulações.

Foi realizado um teste deixando o campo **Usuário vazio**. Nesse caso, a macro exibiu uma mensagem informando que o usuário deveria ser preenchido e impediu corretamente o registro da simulação.

Em seguida, foi realizado um teste com o campo Usuário preenchido. A simulação foi registrada com sucesso na aba `Banco_de_Dados`, incluindo o nome do usuário na coluna correspondente. Após o salvamento, o campo Usuário foi limpo automaticamente, permitindo a realização de uma nova simulação.

Esses testes permitiram verificar o funcionamento das etapas de leitura, validação, gravação e limpeza solicitadas na atividade.

### Papel de cada integrante

| Integrante | Papel |
|---|---|
| Alexandre Jubram | Criação do repositório do projeto e organização das pastas do grupo |
| Bettina Kalassa | Upload dos arquivos e redação da primeira versão do README do Projeto 1 |
| Izabel Born | Upload dos arquivos e revisão da documentação e dos disclaimers do Projeto 1 |
| Maria Eduarda Pereira | Implementação e teste do campo Usuário na atualização com VBA, incluindo leitura, validação, gravação e limpeza |
| Maria Thereza Favaro | Apoio na organização e revisão da documentação dos projetos do grupo |
| Yuri Neres | Organização dos prints e das evidências utilizadas para o registro das entregas |
