original = [ 1, 2, 3 ]

errado = original
errado[0] = 99

print(f"\nOriginal alterada por acidente: {original}")
print(f"Maneira errada: {errado}")

# --- CÓPIA CORRETA ---
original = [ 1, 2, 3 ]
copia = original.copy()
copia[0] = 777

print(f"\nOriginal: {original}")
print(f"Cópia correta: {copia}\n")