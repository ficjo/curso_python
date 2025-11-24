s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(f"\ns1: {s1}")
print(f"s2: {s2}")

# União
print("\nUnião")
print(s1 | s2)
print(s1.union(s2))

# Interseção
print("\nInterseção")
print(s1 & s2)
print(s1.intersection(s2))

# Diferença
print("\nDiferença")
print(s1 - s2)
print(s1.difference(s2))

# Diferença simétrica
print("\nDiferença simétrica")
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

# Subconjunto
print("\nSubconjunto")
print(s1 <= s2)
print(s1.issubset(s2))

# Superconjunto
print("\nSuperconjunto")
print(s1 >= s2)
print(s1.issuperset(s2))

# Disjunto
print("\nDisjunto")
print(s1.isdisjoint(s2))

print()