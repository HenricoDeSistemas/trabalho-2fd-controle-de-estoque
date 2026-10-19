
##Empresa Ficticia: Innovation Inc:
## Controle De Estoque

import csv
from pathlib import Path


#Etapa 1- Estoque

supermercado_estoque = {
    1: "Arroz 5kg",
    2: "Feijão Carioca 1kg",
    3: "Óleo de Soja 900ml",
    4: "Açúcar Refinado 1kg",
    5: "Café Torrado 500g",
    6: "Leite Integral 1L",
    7: "Pão de Forma",
    8: "Tomate",
    9: "Refrigerante 3L",
    10: "Queijo Mussarela",
}

arquivo_dados = Path(__file__).with_name("dados.csv")
custos_por_produto = {}
with arquivo_dados.open(encoding="utf-8", newline="") as arquivo:
    for numero_linha, linha in enumerate(csv.reader(arquivo), start=1):
        if not linha:
            continue
        if len(linha) != 2:
            raise ValueError(
                f"Formato inválido na linha {numero_linha} de dados.csv: "
                "esperado produto e custo."
            )

        produto, custo_texto = (campo.strip() for campo in linha)
        if produto in custos_por_produto:
            raise ValueError(
                f"Produto duplicado na linha {numero_linha} de dados.csv: {produto}."
            )

        try:
            custo = float(custo_texto.replace("R$", "").strip().replace(",", "."))
        except ValueError as erro:
            raise ValueError(
                f"Custo inválido na linha {numero_linha} de dados.csv: "
                f"{custo_texto!r}."
            ) from erro

        custos_por_produto[produto] = custo

produtos_ausentes = set(supermercado_estoque.values()) - custos_por_produto.keys()
produtos_desconhecidos = custos_por_produto.keys() - set(supermercado_estoque.values())
if produtos_ausentes or produtos_desconhecidos:
    raise ValueError(
        "Os produtos de dados.csv não correspondem ao estoque. "
        f"Ausentes: {sorted(produtos_ausentes)}; "
        f"desconhecidos: {sorted(produtos_desconhecidos)}."
    )

#Etapa 2- Organização

prateleira_estoque = [
    [supermercado_estoque[codigo] for codigo in range(1, 6)],
    [supermercado_estoque[codigo] for codigo in range(6, 11)],
]

total_custos = sum(custos_por_produto.values())

print("=" * 64)
print("PAINEL DE ESTOQUE - Innovation Inc.")
print("=" * 64)
for numero_prateleira, prateleira in enumerate(prateleira_estoque, start=1):
    print(f"\nPrateleira {numero_prateleira}:")
    for numero_posicao, produto in enumerate(prateleira, start=1):
        custo = custos_por_produto[produto]
        custo_formatado = f"{custo:.2f}".replace(".", ",")
        print(
            f"  Posição {numero_posicao}: {produto:<24} "
            f"Custo: R$ {custo_formatado}"
        )

print("-" * 64)
print(f"CUSTO TOTAL DO ESTOQUE: R$ {total_custos:.2f}".replace(".", ","))
print("=" * 64)

# Etapa 3- Menu

print("\nMenu de acesso ao estoque:")
for codigo, produto in supermercado_estoque.items():
    print(f"{codigo} - {produto}")

opcao = input("Digite um número de 1 a 10 para consultar o produto: ")

if opcao.isdigit() and int(opcao) in supermercado_estoque:
    print(f"Produto selecionado: {supermercado_estoque[int(opcao)]}")
else:
    print("Opção inválida. Digite um número de 1 a 10.")
