# Filtrar números positivos
numeros = [-3, -1, 0, 2, 5, -7, 8]
positivos = [n for n in numeros if n > 0]

print(f"\nNúmeros: {numeros}")
print(f"Positivos: {positivos}")

# Extrair nomes com mais de 5 letras (tratan espaços e case)
nomes = ["Ana", "   Roberto", "clara  ", "João", "Fernanda  "]
limpos = [nome.strip().title() for nome in nomes if len(nome.strip()) > 5]

print(f"\nNomes: {nomes}")
print(f"Limpos: {limpos}\n")