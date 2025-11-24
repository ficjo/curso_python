# Criar conjuntos

s1 = { 1, 2, 3 }
s2 = set([1, 1, 2, 3])          # -> { 1, 2, 3}

print(f"\ns: {s1}")
print(f"s2: {s2}")

# Adicionar e remover elementos

s1.add(4)
print(f"s1.add(4): {s1}")
s1.add(2)
print(f"s1.add(2): {s1}")

s1.remove(3)                    # ERRO se não existir
print(f"s1.remove(3): {s1}")
s1.discard(3)                   # Não dá erro
print(f"s1.discard(3): {s1}")
s1.pop()                        # Remove um item aleatório
print(f"s1.pop(): {s1}")
s1.clear()
print(f"s1.clear(): {s1}\n")

# Iterar

for item in s1:
    print(item)