print()

with open("leitura.txt", "r", encoding="utf-8") as f:
    print(f.read(6))
    print(f.tell())
    f.seek(0)
    print(f.read(12))

print()