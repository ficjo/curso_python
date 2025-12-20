import datetime

hoje = datetime.datetime.now()
hoje_formatado = hoje.strftime("%d/%B/%Y %H:%M:%S")

print(f"\nHoje: {hoje}")
print(f"Hoje formatado: {hoje_formatado}\n")