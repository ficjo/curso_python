print()

pares = [n for n in range(10) if n % 2 == 0]
print(pares)

rotulos = [f"{n} é par" if n % 2 == 0 else f"{n} é ímpar" for n in range(10)]
print(rotulos)

print()