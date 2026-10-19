
##Empresa Ficticia: Innovation Inc:
## Controle De Estoque

import csv
from pathlib import Path


arquivo_dados = Path(__file__).with_name("dados.csv")
with arquivo_dados.open(encoding="utf-8", newline="") as arquivo:
    produtos_csv = [linha[0] for linha in csv.reader(arquivo) if linha]

print(
    "Lista de produtos em dados.csv:\n"
    + "\n".join(f"- {produto}" for produto in produtos_csv),
    flush=True,
)

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

#Etapa 2- Organização

prateleira_estoque = [
    [supermercado_estoque[codigo] for codigo in range(1, 6)],
    [supermercado_estoque[codigo] for codigo in range(6, 11)],
]

print("Matriz das prateleiras de estoque:")
for numero_prateleira, prateleira in enumerate(prateleira_estoque, start=1):
    posicoes = " | ".join(
        f"Posição {numero_posicao}: {produto}"
        for numero_posicao, produto in enumerate(prateleira, start=1)
    )
    print(f"Prateleira {numero_prateleira}: {posicoes}")

# Etapa 3- Menu

print("\nMenu de acesso ao estoque:")
for codigo, produto in supermercado_estoque.items():
    print(f"{codigo} - {produto}")

opcao = input("Digite um número de 1 a 10 para consultar o produto: ")

if opcao.isdigit() and int(opcao) in supermercado_estoque:
    print(f"Produto selecionado: {supermercado_estoque[int(opcao)]}")
else:
    print("Opção inválida. Digite um número de 1 a 10.")
