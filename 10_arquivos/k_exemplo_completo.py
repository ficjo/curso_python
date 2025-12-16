from pathlib import Path

arquivo = Path("produtos.txt")
produtos = {}

with arquivo.open() as f:
    for linha in f:
        nome, preco = linha.strip().split(",")
        produtos[nome] = float(preco)

desconto = { p: v * 0.9 for p, v in produtos.items() }
saida = Path("produtos_com_desconto.txt")

with saida.open("w") as f:
    for p, v in desconto.items():
        f.write(f"{p}: {v:.2f}\n")