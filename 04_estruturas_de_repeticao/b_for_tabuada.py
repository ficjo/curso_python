numero = int(input("\nDigite um número: "))

print(f"Tabuada de {numero}:\n")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

print()