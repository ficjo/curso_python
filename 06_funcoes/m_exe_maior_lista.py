def max_lista(lista):
    maior = lista[0]
    for n in lista:
        if n >= maior:
            maior = n
    return maior

lista = [3, 9, 2, 7]
print(f"\nLista: {lista}")
print(f"Maior: {max_lista(lista)}\n")