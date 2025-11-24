numero_for = input("\nDigite um número: ")
soma_for = 0

# Usando for
for digito in numero_for:
    soma_for += int(digito)

print(f"\nSoma dos dígitos usando for: {soma_for}")

print()

numero_while = int(input("Digite um novo número: "))
soma_while = 0
resta_while = 0

while numero_while != 0:
    resta = numero_while % 10               # Pega o último número
    soma_while += resta                     # Soma esse número à soma
    numero_while = int(numero_while / 10)   # Remove o último dígito 

print(f"\nSoma dos dígitos usando while: {soma_while}\n")

