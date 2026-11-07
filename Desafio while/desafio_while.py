# INTEGRADOR - ENCUESTA TECNOLOGICA
# ==========================================

# VARIABLES INICIALES

contador = 1

cantidad_masculinos_IA_IOT = 0
cantidad_no_IA = 0

mayor_edad = 0
nombre_mayor = ""
tecnologia_mayor = ""

# INGRESO DE DATOS DE 10 EMPLEADOS

while contador <= 10:

    print("\nEMPLEADO", contador)

    # VALIDAR NOMBRE

    nombre = input("Ingrese el nombre: ")

    while nombre == "":
        print("El nombre no puede estar vacio.")
        nombre = input("Ingrese el nombre: ")

    # VALIDAR EDAD

    edad = int(input("Ingrese la edad: "))

    while edad < 18:
        print("La edad debe ser de 18 años o mas.")
        edad = int(input("Ingrese nuevamente la edad: "))

    # VALIDAR GENERO

    genero = input("Ingrese el genero (Masculino/Femenino/Otro): ").lower()

    while genero != "masculino" and genero != "femenino" and genero != "otro":
        print("Genero incorrecto.")
        genero = input("Ingrese Masculino, Femenino u Otro: ").lower()

    # VALIDAR TECNOLOGIA

    tecnologia = input("Ingrese tecnologia (IA/RV/RA/IOT): ").upper()

    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        print("Tecnologia incorrecta.")
        tecnologia = input("Ingrese IA, RV/RA o IOT: ").upper()

    # ==========================================
    # PUNTO 1
    # Hombres de entre 25 y 50 años que votaron por IOT o IA
    # ==========================================

    if genero == "masculino" and edad >= 25 and edad <= 50 and (tecnologia == "IA" or tecnologia == "IOT"):
        cantidad_masculinos_IA_IOT += 1

    # ==========================================
    # PUNTO 2
    # Empleados que no votaron por IA, que no sean femeninos y tengan entre 33 y 40 años
    # ==========================================

    if genero != "femenino" and edad >= 33 and edad <= 40 and tecnologia != "IA":
        cantidad_no_IA += 1

    # ==========================================
    # PUNTO 3
    # Buscar el empleado masculino de mayor edad
    # ==========================================

    if genero == "masculino":

        if edad > mayor_edad:
            mayor_edad = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia

    contador += 1


# ==========================================
# RESULTADOS
# ==========================================

print("\n================================")
print("       RESULTADOS ENCUESTA")
print("================================")

# PUNTO 1

print("1. Hombres que votaron por IA o IOT:", cantidad_masculinos_IA_IOT)

# PUNTO 2

porcentaje = (cantidad_no_IA * 100) / 10

print("2. Porcentaje de empleados que cumplen las condiciones:", porcentaje, "%")

# PUNTO 3

if mayor_edad > 0:

    print("3. Empleado masculino de mayor edad:")
    print("Nombre:", nombre_mayor)
    print("Edad:", mayor_edad)
    print("Tecnologia elegida:", tecnologia_mayor)

else:
    print("3. No se ingresaron empleados masculinos.")

print("================================")
print("Encuesta finalizada.")