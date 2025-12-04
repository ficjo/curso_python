print()

try:
    x = int(input("\nNúmero: "))
    print(10 / x)
except (ValueError, ZeroDivisionError) as e:
    print("Erro: Valor inválido ou divisão por zero.")
    print(e)
    print(type(e))

print()