print("\nLendo arquivo inteiro.\n")

with open("leitura.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

print(conteudo)

print("\nLendo linha por linha.\n")

with open("leitura.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

print()