opcao = 4

print()

match opcao:
    case 1:
        print("Iniciar")
    case 2:
        print("Carregar")
    case 3:
        print("Sair")
    case _:
        print("Opção inválida")

print()

comando = "play"

match comando:
    case "play":
        print("Reproduzindo música")
    case "pause":
        print("Música pausada")
    case "stop":
        print("Parado")
    case _:
        print("Comando desconhecido")

print()