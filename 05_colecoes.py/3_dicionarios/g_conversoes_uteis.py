# Dicionários podem ser convertidos para listas de chaves, valores ou tuplas


d = { "nome": "Azul", "idade": 30, "ativo": True }

print(f"\nd: {d}")
print(f"list(d.keys()): {list(d.keys())}")
print(f"list(d.values()): {list(d.values())}")
print(f"list(d.items()): {list(d.items())}")
print(f"dict([('a', 1), ('b', 2)]): {dict([('a', 1), ('b', 2)])}\n")