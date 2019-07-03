print()
print()

numero = int(input("La tabla del numero: "))

for multiplo in range(1, 1001):
    print("{} * {} = {}".format(numero, multiplo, numero * multiplo))
