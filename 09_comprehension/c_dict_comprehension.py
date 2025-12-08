print()

quadrados = {n: n**2 for n in range(5)}
print(quadrados)

pares = {n: n*n for n in range (10) if n % 2 == 0}
print(pares)

lista = [1,2,3,4,5,6,7,8,9,10]
classificados = {item: ("par" if item % 2 == 0 else "ímpar") for item in lista}
print(classificados)

# Aninhamento
A = [1,2,3]
B = [4,5,6]
nums = { (x, y): x + y for x in A for y in B}
print(nums)

print()