def cadastrar_usuario(nome, idade=0, *tags, **info_extra):
    """
    Cadastra um usuário no sistema.
    - nome: obrigatório
    - idade: padrão 0
    - *tags: lista de características
    - **info_extra: dados adicionais em chave-valor
    """

    print(f"\nNome: {nome}")
    print(f"Idade: {idade}")

    if tags:
        print("TAGS:")
        for t in tags:
            print(f"- {t}")

    if info_extra:
        print("EXTRAS:")
        for chave, valor in info_extra.items():
            print(f"{chave}: {valor}")

    return "Usuário Cadastrado!"

resultado = cadastrar_usuario(
    "Azul",
    30,
    "Programador", "Não gosta de café",
    cidade="Recife",
    ativo=True
)

print(f"\nRetorno: {resultado}\n")