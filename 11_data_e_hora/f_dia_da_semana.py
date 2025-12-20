import datetime

def dia_da_semana(valor):
    dia = [ "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo" ]
    return dia[valor]

hoje = datetime.datetime.now()
amanha = hoje + datetime.timedelta(days=1)
meia_noite = datetime.time()
tarefa = datetime.datetime.combine(amanha, meia_noite)

print(f"\nTarefa: {tarefa}")
print(f"type(tarefa): {type(tarefa)}")
print(f"repr(tarefa): {repr(tarefa)}")
print(f"\nDia da semana: {dia_da_semana(tarefa.weekday())}\n")