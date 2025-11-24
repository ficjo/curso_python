idade = 20
tem_carteira = True

print()

if idade >= 18:
    if tem_carteira:
        print("Pode dirigir")
    else:
        print("Falta carteira")
else:
    print("Menor de idade")

print()

usuario = "admin"
senha = "1234"

if usuario == "admin":
    if senha == "1234":
        print("Login autorizado")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")

print()

# Usando operadores lógicos para evitar aninhamento
idade = 20
tem_carteira = True

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and tem_carteira:
    print("Pode dirigir")
else:
    print("Falta carteira")


print()

usuario = "admin"
senha = "1234"

if usuario != "admin":
    print("Usuário não encontrado")
elif usuario == "admin" and senha == "1234":
    print("Login autorizado")
else:
    print("Senha incorreta")

print()
