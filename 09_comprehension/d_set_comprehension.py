print()

palavra = "Leopardo"
resultado = { (f"{c}: vogal" if c in "aeiou" else f"{c}: consoante") for c in palavra}
print(resultado)

a = {n for n in range(20) if n % 3 == 0}
print(a)

print()