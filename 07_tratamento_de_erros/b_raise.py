def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b

print(f"\n{dividir(10, 2)}")
print(f"\n{dividir(10, 0)}")
