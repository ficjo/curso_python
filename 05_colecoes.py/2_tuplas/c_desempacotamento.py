t = (10, 20, 30)
a, b, c = t

print(f"\nt = {t}")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

x, y = 5, 10
print(f"\nx = {x}")
print(f"y = {y}")

x, y = y, x
print("x, y = y, x")
print(f"x = {x}")
print(f"y = {y}")

t2 = (1, 2, 3, 4, 5)
a, *meio, b = t2
print(f"\nt2 = {t2}")
print(f"a = {a}")
print(f"meio = {meio}")
print(f"type(meio): {type(meio)}")
print(f"b = {b}\n")