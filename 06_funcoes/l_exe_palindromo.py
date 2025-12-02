def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

print()
print(eh_palindromo("radar"))
print(eh_palindromo("Python"))
print()