print("\nCria novo arquivo (erro se existir)")

with open("novo.txt", "x", encoding="utf-8") as f:
    f.write("Arquivo criado")

with open("novo.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

print("\nLeitura + Escrita")

with open("numeros.txt", "r+") as f:
    conteudo = f.read()
    f.write("\n50")

with open("numeros.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

print()