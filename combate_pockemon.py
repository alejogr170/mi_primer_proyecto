#Usuario elige adversario#
pockemon_elegido = input("Contra que pockemon quieres combatir? ( Squirtle / Charmander / Bulbasaur ):").upper()

vida_pikachu = 100
vida_enemigo = 0
nombre_pockemon = 0
ataque_pockemon = 0

if pockemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
    nombre_pockemon = "Squirtle"
    ataque_pockemon = 8

elif pockemon_elegido == "CHARMANDER":
    vida_enemigo = 80
    nombre_pockemon = "CHARMANDER"
    ataque_pockemon = 7

elif pockemon_elegido == "BULBASAUR":
    vida_enemigo = 100
    nombre_pockemon = "BULBASAUR"
    ataque_pockemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    #Usuario elige atque#
    ataque_elegido = input("¿Que ataque deseas usar ( Bola voltio / Chispazo)?:").upper()

    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12
    elif ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10

    vida_pikachu -= ataque_pockemon

    print("La vida de {} es {}".format(nombre_pockemon, vida_enemigo))

    print("{} hace un ataque de {}".format(nombre_pockemon, ataque_pockemon))

    print("La vida de pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("{} esta fuera de combate".format(nombre_pockemon))

elif vida_pikachu <= 0:
    print("PIKACHU esta fuera de combate")

print("Final del combate")