numeros = [ 10, 20, 30, 40 ]
misturada = [ 1, "Luna", 3.5, True ]

print()

print(numeros)
print(misturada)

print(numeros[1])           # Primeiro
print(numeros[-1])          # Último 
print(numeros[-2])          # Penúltimo

print()

# --- ACESSO E MODIFICAÇÃO ---
nomes = [ "Ana", "Bruno", "Carla" ]
nomes [1] = "Beatriz"

print(f"Lista de nomes: {nomes}")

# --- VERIFICA SE EXISE ---
if "Carla" in nomes:
    print("Carla está na lista.")

print(f"Ana está na lista? -> {'Ana' in nomes}")
print(f"João está na lista? -> {'João' in nomes}")

print()