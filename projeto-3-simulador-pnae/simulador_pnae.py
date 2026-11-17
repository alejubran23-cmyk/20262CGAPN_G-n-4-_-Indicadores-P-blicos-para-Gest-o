### Simulador de Repasse do PNAE ###
# Calcula o repasse anual do PNAE para uma escola, classifica o porte
# e estima quanto do custo dos alimentos o repasse federal consegue cobrir.

### Parâmetros ###
# Valores per capita diários (Resolução CD/FNDE nº 1/2026)
PER_CAPITA_CRECHE = 1.57
PER_CAPITA_PRE_ESCOLA = 0.82
PER_CAPITA_FUNDAMENTAL = 0.57

# Custo dos alimentos (só matéria-prima) de uma refeição escolar
# Fonte: Sanches e Silva, "Alimentos e alimentação coletiva: análise dos gastos reais x
# repasse de verbas para a alimentação escolar de duas escolas estaduais do interior do
# Estado de São Paulo" (dados de ago-nov/2023) - https://static.even3.com/anais/1072522.pdf
CUSTO_ALIMENTOS_REFEICAO = 3.60


### Funções ###
def ler_numero(mensagem):
    numero = input(mensagem)
    while not numero.isdigit():
        print("Você digitou um número incorreto. Digite apenas números inteiros, sem sinal.")
        numero = input(mensagem)
    numero = int(numero)
    return numero


def calcular_repasse(dias_letivos, creche, pre_escola, fundamental):
    repasse_creche = creche * PER_CAPITA_CRECHE * dias_letivos
    repasse_pre_escola = pre_escola * PER_CAPITA_PRE_ESCOLA * dias_letivos
    repasse_fundamental = fundamental * PER_CAPITA_FUNDAMENTAL * dias_letivos
    repasse_total = repasse_creche + repasse_pre_escola + repasse_fundamental
    return repasse_creche, repasse_pre_escola, repasse_fundamental, repasse_total


def classificar_porte(total_matriculas):
    # Faixas didáticas do Projeto 1 (aba Parametros_PNAE)
    if total_matriculas <= 200:
        porte = "Pequena"
    elif total_matriculas <= 400:
        porte = "Média"
    else:
        porte = "Grande"
    return porte


def calcular_cobertura(repasse_total, total_alunos, dias_letivos):
    custo_anual = total_alunos * dias_letivos * CUSTO_ALIMENTOS_REFEICAO
    # Arredonda para centavos antes de comparar (evita erro de casas decimais do Python)
    repasse_total = round(repasse_total, 2)
    custo_anual = round(custo_anual, 2)
    if custo_anual == 0:
        cobertura = 0
    else:
        cobertura = repasse_total / custo_anual * 100
    if repasse_total >= custo_anual:
        diferenca = 0
    else:
        diferenca = custo_anual - repasse_total
    return custo_anual, cobertura, diferenca


def formata_reais(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto


### Programa Principal ###
print("*** Olá, bem-vindo ao Simulador de Repasse do PNAE ***")
print()
escola = input("Digite o nome da escola: ")
dias_letivos = ler_numero("Quantos dias letivos a escola tem no ano? ")

print()
print("Digitação das matrículas (digite 0 se a escola não tiver a etapa)")
creche = ler_numero("Matrículas na creche: ")
pre_escola = ler_numero("Matrículas na pré-escola: ")
fundamental = ler_numero("Matrículas no ensino fundamental: ")

total_alunos = creche + pre_escola + fundamental

repasse_creche, repasse_pre_escola, repasse_fundamental, repasse_total = calcular_repasse(
    dias_letivos, creche, pre_escola, fundamental)
porte = classificar_porte(total_alunos)
custo_anual, cobertura, diferenca = calcular_cobertura(repasse_total, total_alunos, dias_letivos)

print()
print("===== Resultado para", escola, "=====")
print("Total de matrículas:", total_alunos)
print("Porte da escola:", porte)
print()
print("Repasse anual da creche:", formata_reais(repasse_creche))
print("Repasse anual da pré-escola:", formata_reais(repasse_pre_escola))
print("Repasse anual do ensino fundamental:", formata_reais(repasse_fundamental))
print("Repasse anual total:", formata_reais(repasse_total))
print()
print("Custo anual estimado dos alimentos:", formata_reais(custo_anual))
print(f"Cobertura do repasse federal: {cobertura:.1f}%".replace(".", ","))
print("Diferença a ser coberta por outras fontes:", formata_reais(diferenca))
if diferenca == 0:
    print("O repasse federal cobre o custo estimado dos alimentos.")
