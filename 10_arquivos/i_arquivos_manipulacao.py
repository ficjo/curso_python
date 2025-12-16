import os

os.mkdir("dados")
os.remove("novo.txt")

print()

print(os.path.exists("leitura.txt"))
print(os.path.isfile("leitura.txt"))
print(os.path.isdir("dados"))

print()