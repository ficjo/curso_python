d = { "nome": "Azul", "idade": 30, "ativo": True }      # Criação padrão
vazio = {}                                              # Vazio
d2 = dict(nome="Azul", idade=30, ativo=True)            # Usando dict
d3 = dict([("a", 1), ("b", 2)])                         # Lista de tuplas

print(f"\nvazio: {vazio}")
print(f"d: {d}")
print(f"d1: {d2}")
print(f"d3: {d3}\n")

# Acessando valores

print(f"d['nome']: {d["nome"]}")
print(f"d.get('idade'): {d.get("idade")}")              # Retorna None se não existir
print(f"d.get('x', 0): {d.get("x", 0)}\n")              # Retorna 0 se x não existir
