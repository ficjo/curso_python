print("\nCriando ou sobrescrevendo arquivo.\n")

with open("saida.txt", "w", encoding="utf-8") as f:
    f.write("Primeira linha\n")
    f.write("Segunda linha\n")

with open("saida.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

print("\nAcrescentando conteúdo\n")

with open("saida.txt", "a", encoding="utf-8") as f:
    f.write("Linha adicionada.\n")

with open("saida.txt", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())

print()