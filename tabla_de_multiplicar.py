print()
print()

numero = int(input("La tabla del numero: "))

for multiplo in range(5, 16):
    print("{} * {} = {}".format(numero, multiplo, numero * multiplo))
