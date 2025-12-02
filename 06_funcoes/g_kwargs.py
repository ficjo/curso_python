def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

print()

mostrar_info(nome="Azul", idade=30, ativo=True)
mostrar_info(nome="João", endereco={"rua": "Rua top", "numero": "123"})

print()