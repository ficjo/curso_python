lista = [ 10, 20, 30 ]

# --- ADICIONANDO ---

print(f"\nLista: {lista}")

lista.append(40)                # Final
lista.insert(1, 15)             # Posição específica
lista.extend([50, 60])          # Adiciona vários

print(f"Lista depois de adicionar: {lista}\n")

# --- REMOVENDO ---
valor_removido = lista.pop()    # Remove o último (e retorna)
print(f"Pop removeu: {valor_removido}")

valor_removido_2 = lista.pop(2) # Remove pelo índice
print(f"Pop (2) removeu: {valor_removido_2}")

lista.remove(15)                # Remove pelo valor

print(f"Lista depois das remoções: {lista}\n")

# --- REMOVER COM DEL ---
del lista[0]
print(f"Lista depois do del: {lista}")

# --- CLEAR ---
lista.clear()
print(f"Depois do clear: {lista}\n")