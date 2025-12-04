def ler_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido.")

idade = ler_int("\nQual a sua idade? ")
print(f"Idade registrada: {idade}\n")