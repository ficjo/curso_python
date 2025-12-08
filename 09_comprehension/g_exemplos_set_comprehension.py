# Coletar as primeiras letras únicas de uma lista de nomes
nomes = ["Ana", "Alice", "Bruno", "Bia", "Carlos"]
iniciais = {nome[0].upper() for nome in nomes}

print(f"\nNomes: {nomes}")
print(f"Iniciais: {iniciais}")

# Quadrados únicos de uma lista
nums = [1, 2, 2, 3, 3, 4, 5, 5, 6]
quadrados_unicos = {n * n for n in nums}

print(f"\nNúmeros: {nums}")
print(f"Quadrados únicos: {quadrados_unicos}\n")
