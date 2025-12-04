try:
    n = int(input("\nDigite um número: "))
except ValueError:
    print("Isso não é um número!")
else:
    print(f"Número válido: {n}")
finally:
    print("Encerrando a operação.\n")