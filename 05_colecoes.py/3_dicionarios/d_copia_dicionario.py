import copy

# Cópia rasa
print("\nCópia Rasa.\n")

a = { "nums": [1, 2, 3] }
b = a.copy()

print(f"\na: {a}")
print(f"b: {b}")

b["nums"].append(4)

print("\nDepois do b['nums'].append(4):")
print(f"a: {a}")
print(f"b: {b}")

# Cópia profunda
print("\nCópia Profunda.\n")

c = { "nums": [1, 2, 3] }
d = copy.deepcopy(c)

print(f"c: {c}")
print(f"d: {d}")

d["nums"].append(4)

print("\nDepois do d['nums'].append(4):")
print(f"c: {c}")
print(f"d = {d}\n")