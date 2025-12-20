import datetime

nascimento = input("\nDigite o ano de nascimento (dd/mm/aaaa): ")
nasc_list = nascimento.split("/")
nasc_data = datetime.date(
    int(nasc_list[2]),
    int(nasc_list[1]),
    int(nasc_list[0])
)

print("\n", nasc_data, "\n")