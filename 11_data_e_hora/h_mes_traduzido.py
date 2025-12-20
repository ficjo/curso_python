import datetime

def retorna_data(hoje):
    meses = [ "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
              "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]
    return f"{hoje.day} de {meses[hoje.month]} de {hoje.year}"

hoje = datetime.datetime.now()
hoje_formatado = retorna_data(hoje)

print(f"\nHoje: {hoje}")
print(f"Hoje formatado: {hoje_formatado}\n")