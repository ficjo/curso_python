
quadrados = [ x * x for x in range(10)]
print(f"\nQuadrados: {quadrados}")

pares = [ num for num in range(20) if num % 2 == 0]
print(f"Pares: {pares}")

nomes = [ "ana", "luiz", "marcos" ]
maiusculas = [ nome.upper() for nome in nomes ]
print(f"Maiúsculos: {maiusculas}")

mistura = [ 12, "a", 5.5, True, 8 ]
numeros = [ x for x in mistura if type(x) == int ]
print(f"Apenas inteiros: {numeros}\n")
