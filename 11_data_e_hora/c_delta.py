import datetime

hoje = datetime.datetime.now()
natal = datetime.datetime(2025, 12, 25, 0)

# Calculando o delta
espera = natal - hoje

print(f"\n{type(espera)}")
print(repr(espera))
print(espera)
print(f"\nFaltam {espera.days} dias para o Natal!\n")