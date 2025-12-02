def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

print()

print(media([1, 2, 3, 4]))

def media_args(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(media_args(1, 2, 3, 4))

print()
