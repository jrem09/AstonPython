def additioner(a, b):
    return a+b


def soustraire(a, b):
    return a-b


def multiplier(a, b):
    return a*b


def diviser(a, b):
    return a/b


print("Menu Calculatrice\r\n1: Additioner\r\n2: Soustraire\r\n3: Multiplier\r\n4: Diviser")

id = input()

a = input("Saisir nombre 1:")
b = input("Saisir nombre 2:")

if id == 1:
    print additioner(a, b)
elif id == 2:
    print soustraire(a, b)
elif id == 3:
    print multiplier(a, b)
elif id == 4:
    print diviser(a, b)
