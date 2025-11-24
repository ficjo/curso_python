frutas = [ "maçã", "banana", "uva" ]

print("\nLoop simples")
for fruta in frutas:
    print(fruta)

print("\nLoop com índice")
for i in range(len(frutas)):
    print(i, frutas[i])

print("\nEnumerate")
for indice, valor in enumerate(frutas):
    print(indice, valor)

print()