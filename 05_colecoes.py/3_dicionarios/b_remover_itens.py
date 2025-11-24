d = { "nome": "Azul", "idade": 30, "ativo": True }

print(f"\nd: {d}")
d.pop("idade")    # remove pela chave (e retorna o valor)
print(d)
d.popitem()       # remove o último par inserido
print(d)
del d["nome"]     # remove diretamente
print(d)
d.clear()         # apaga tudo
print(d)