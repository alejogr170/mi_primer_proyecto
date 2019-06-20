
pockemon_elegido = input("Contra que pockemon quieres combatir? ( Squirtle / Charmander / Bulbasaur ):").upper()

vida_pikachu = 100
vida_enemigo = 0

if pockemon_elegido == "SQUIRTLE":
    vida_enemigo = 90
elif pockemon_elegido == "CHARMANDER":
    vida_enemigo = 80
elif pockemon_elegido == "BULBASAUR":
    vida_enemigo = 100

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque deseas usar ( Bola voltio / Chispazo)?:").upper()
    if ataque_elegido == "BOLA VOLTIO":
        vida_enemigo -= 12
    elif ataque_elegido == "CHISPAZO":
        vida_enemigo -= 10
    print("La vida de tu oponente es {}".format(vida_enemigo))
    if pockemon_elegido == "SQUIRTLE":
        vida_pikachu -= 8
        print("Squirtle te hace un ataque de 8 de daño")
        print("La vida de pikachu es de {}".format(vida_pikachu))
    elif pockemon_elegido == "CHARMANDER":
        vida_pikachu -= 7
        print("Charmander te hace un ataque de 7 de daño")
        print("La vida de pikachu es de {}".format(vida_pikachu))
    elif pockemon_elegido == "BULBASAUR":
        vida_pikachu -= 10
        print("Bulbasaur te hace un ataque de 10 de daño")
        print("La vida de pikachu es de {}".format(vida_pikachu))
if vida_enemigo <= 0:
    print("{} esta fuera de combate".format(pockemon_elegido))
elif vida_pikachu <= 0:
    print("PIKACHU esta fuera de combate")
print("Final del combate")