print()
print()

numero = int(input("La tabla del numero: "))

for multiplo in range(-10, 1):
    print("{} * {} = {}".format(numero, -multiplo, -numero * multiplo))
