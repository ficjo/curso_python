valores = [ 5, 3, 8, 3, 9, 1, 3 ]
cidades = [ "Recife", "São Paulo", "Florianópolis", "Fortaleza", "João Pessoa", "Recife" ]

print(f"\nLista de números: {valores}")
print(f"Lista de cidades: {cidades}")

# --- CONTAGEM ---
print(f"Count(3): {valores.count(3)}")
print(f"Count('Recife'): {cidades.count('Recife')}")

# --- INVERTE AS LISTAS ---
valores.reverse()
cidades.reverse()

print("\nListas invertidas:")
print(f"Valores: {valores}")
print(f"Cidades: {cidades}")

# --- ORDENACAO ---
valores.sort()
cidades.sort()
print(f"\nSort de valores: {valores}")
print(f"Sort de cidades: {cidades}")

# --- CRIAR OUTRA ORDENADA SEM MODIFICAR A ORIGINAL ---

# Redeclarando as listas para resetar o sort
valores = [ 5, 3, 8, 3, 9, 1, 3 ]
cidades = [ "Recife", "São Paulo", "Florianópolis", "Fortaleza", "João Pessoa", "Recife" ]

valores_ordenados = sorted(valores)
cidades_ordenadas = sorted(cidades)

print(f"\nValores originais: {valores}")
print(f"Valores ordenados: {valores_ordenados}")
print(f"Cidades originais: {cidades}")
print(f"Cidades ordenadas: {cidades_ordenadas}\n")

