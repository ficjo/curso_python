texto_1 = "Python"
texto_2 = 'Aprender é divertido'
texto_3 = """Texto com
várias linhas"""

# Concatenação e Repetição
nome = "Azul"
saudacao = f"Olá, " + nome + "!"
print(saudacao)
print("Ha" * 3)

# Interpolação (f-strings)
idade = 22
print(f"Meu nome é {nome}, tenho {idade} anos.")

# Acesso por índice
print(texto_1[0])               # P
print(texto_1[1])               # y
print(texto_1[-1])              # n

# Fatiamento (Slicing)
# sintaxe -> string[inicio:fim:passo]
texto = "Programar"
print(texto[0:5])               # Progr (0 ao 4)
print(texto[3:])                # gramar (3 até o fim)
print(texto[:6])                # Progra (do início até 5)
print(texto[::2])               # Pormr (de 2 em 2)
print(texto[::-1])              # ramargorP (interte a string)
print(texto[::-2])              # rmroP (2 em 2 invertido)

# Principais métodos string
frase = "   Python é incrível!     "
print(frase.lower())
print(frase.upper())
print(frase.title())
print(frase.capitalize())

# Remoção e substituição
print(frase.strip())
print(frase.lstrip())
print(frase.rstrip())
print(frase.replace("Incrível", "Fenomenal"))
print(frase)
print(frase.strip().capitalize())

# Divisão e Junção
palavras = frase.split()
print(palavras)
print("-".join(palavras))

# Busca e contagem
print(frase.count("i"))
print(frase.find("Python"))     # Retorna o íncide inicial
print("Python" in frase)        # True
print("Java" in frase)          # False
print("COBOL" not in frase)     # True

# Caracteres especiais
"""
    \n -> Quebra de linha
    \t -> Tabulação
    \\ -> Barra invertida
    \" -> Aspas duplas
    \' -> Aspas simples
"""
print("Olá,\nMundo!")
print("Aprender\tPython")

# Funções úteis
print(len("Python"))            # 6 -> Retorna a quantidade de caracteres
print(str(123))                 # '123' -> Converte número em string

# Verificações (True ou False)
print(texto_1.startswith("Py")) # True
print(texto_1.endswith("on"))   # True
print(texto_1.isalpha())        # True
print(texto_1.isdigit())        # False
print(texto_1.isalnum())        # True
print(" ".isspace())            # True
print("python".islower())       # True
print("PYTHON".isupper())       # True
print("Python".islower())       # False

# Busca e localização
print("banana".find("na"))      # 2
print("banana".rfind("na"))     # 4
print("banana".count("na"))     # 2

# Formatação
print(f"Olá, {nome}")
print("Olá, {}!".format(nome))
print("{} tem {} anos".format(nome, idade))
print("{nome} tem {idade} anos.".format(nome="Vermelho", idade=30))
