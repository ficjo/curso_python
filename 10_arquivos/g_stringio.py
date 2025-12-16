from io import StringIO

f = StringIO()
f.write("Linha 1.\n")
f.write("Linha 2.\n")

f.seek(0)

print(f"\n{f.read()}\n")