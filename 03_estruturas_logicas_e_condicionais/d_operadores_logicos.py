idade = 25
tem_carteira = True

pode_dirigir = idade >= 18 and tem_carteira

print()
print(pode_dirigir)

sol = False
feriado = True

pode_sair = sol or feriado

print(pode_sair)
print(not pode_sair)

lista = []                  # Listas vazias são False
lista_vazia = not lista

print(lista_vazia)
print()