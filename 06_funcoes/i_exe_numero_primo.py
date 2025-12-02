def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

print()

for i in range(20):
    if eh_primo(i):
        print(f"{i} é primo.")
        
# Versão avançada
def eh_primo_2(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print()

for i in range(20):
    if eh_primo_2(i):
        print(f"{i} é primo.")

print()