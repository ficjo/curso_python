# Aplica 10% de desconto em cada produto
produtos = {"camisa": 80, "calça": 120, "tênis": 300}
com_desconto = {p: preco * 0.9 for p, preco in produtos.items()}

print(f"\nProdutos: {produtos}")
print(f"Com desconto: {com_desconto}")

# Contar quantas vogais tem em cada palavra
palavras = ["Python", "Azul", "Programação"]
vogais = "aeiouAEIOU"
contador = {p: sum(1 for letra in p if letra in vogais) for p in palavras}

print(f"\nPalavras: {palavras}")
print(f"Quantas vogais: {contador}\n")



