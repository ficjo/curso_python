d = { "nome": "Azul", "idade": 30, "ativo": True }

print(f"\nd: {d}")
print(f"d.keys(): {d.keys()}")
print(f"d.values(): {d.values()}")
print(f"d.items(): {d.items()}")

# Iteração

for chave, valor in d.items():
    print(f"{chave}: {valor}")

print()

for chave in d:
    print(chave)

print()

for value in d.values():
    print(value)

print()

# Verofica se uma chave existe
print(f"\n'nome' in d: {"nome" in d}")      # True
print(f"'x' in d: {"x" in d}\n")            # False