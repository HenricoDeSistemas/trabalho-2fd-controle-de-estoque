
##Innovation Inc.: Controle de Estoque 


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

