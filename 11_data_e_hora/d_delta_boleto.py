import datetime

hoje = datetime.datetime.now()
regra = datetime.timedelta(days=3)
data_boleto = hoje + regra

print(f"\nHoje: {hoje.strftime('%d/%m/%Y')}")
print(f"Regra: {regra}")
print(f"Data Boleto: {data_boleto.strftime('%d/%m/%Y')}\n")