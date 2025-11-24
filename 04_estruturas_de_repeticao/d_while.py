contador = 1

print()

while contador <= 5:
    print(contador)
    contador += 1

print()

comando = ""
soma = 0

while comando != "sair":
    num = int(input("Digite um número: "))
    soma += num
    comando = input("Digite um comando: ")

print(f"\nSoma final: {soma}\n")
