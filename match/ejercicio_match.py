print("1 invierno")
print("2 verano")
print("3 otoño")
print("4 primavera")

estacion = int(input("Ingrese un 1, 2, 3 o 4: "))

match estacion:
    case 1:
        print("Se viaja a Bailoche")
    case 2:
        print("Se viaja a Mar del Plata y Cataratas")
    case 3:
        print("Se viaja a todos los lugares")
    case 4:
        print("Se viaja a todos los lugares menos a Bariloche")
    case _:
        print("Opcion incorrecta")
