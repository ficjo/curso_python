print()

combinacao = [ (x, y) for x in [1,2] for y in ["a", "b"]]
print(combinacao)

matriz = [ [1,2,3], [4,5,6], [7,8,9] ]
flat = [ num for linha in matriz for num in linha ]
print(flat)

print()