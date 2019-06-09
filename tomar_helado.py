

te_apetece_un_helado= input("Te apetece un helado? (Si/No)").upper()
tienes_dinero = input("Tienes dinero? (Si/No)").upper()
alguien_te_invita= input("Tienes a alguien que te invite? (Si/No)").upper()
esta_el_carrito = input("Esta el carrito de los helados? (Si/No)").upper()

if te_apetece_un_helado == "SI" and (tienes_dinero== "SI" or alguien_te_invita == "SI") and esta_el_carrito == "SI":
    print("Entonces.... ¡Que aproveche!")
else:
    print("Otro dia sera!")