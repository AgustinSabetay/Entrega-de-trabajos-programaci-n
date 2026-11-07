# GUIA WHILE - VALIDACIONES
# EJERCICIOS 1 AL 5
# ==========================================

# EJERCICIO 1
def ejercicio_1():

    clave_correcta = "1234"

    clave = input("Ingrese la clave: ")

    while clave != clave_correcta:
        print("Clave incorrecta.")
        clave = input("Vuelva a ingresar la clave: ")

    print("Clave correcta. Acceso permitido.")


# EJERCICIO 2
def ejercicio_2():

    clave_correcta = "1234"
    intentos = 1

    clave = input("Ingrese la clave: ")

    while clave != clave_correcta and intentos < 3:

        print("Clave incorrecta.")
        intentos += 1

        clave = input("Vuelva a ingresar la clave: ")

    if clave == clave_correcta:
        print("Clave correcta. Acceso permitido.")
    else:
        print("Supero la cantidad de intentos permitidos.")


# EJERCICIO 3
def ejercicio_3():

    nota = int(input("Ingrese una nota entre 1 y 10: "))

    while nota < 1 or nota > 10:

        print("Nota incorrecta. Debe estar entre 1 y 10.")
        nota = int(input("Ingrese nuevamente la nota: "))

    print("Nota valida:", nota)


# EJERCICIO 4
def ejercicio_4():

    color = input("Ingrese un color (Rojo, Verde o Azul): ").lower()

    while color != "rojo" and color != "verde" and color != "azul":

        print("Color incorrecto.")
        color = input("Ingrese Rojo, Verde o Azul: ").lower()

    print("Color valido:", color)


# EJERCICIO 5
def ejercicio_5():

    # VALIDAR APELLIDO

    apellido = input("Ingrese su apellido: ")

    while apellido == "":
        print("El apellido no puede estar vacio.")
        apellido = input("Ingrese su apellido: ")

    # VALIDAR EDAD

    edad = int(input("Ingrese su edad: "))

    while edad < 18 or edad > 90:
        print("Edad incorrecta. Debe estar entre 18 y 90.")
        edad = int(input("Ingrese nuevamente su edad: "))

    # VALIDAR ESTADO CIVIL

    estado_civil = input(
        "Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a o Viudo/a): "
    ).lower()

    while (
        estado_civil != "soltero/a"
        and estado_civil != "casado/a"
        and estado_civil != "divorciado/a"
        and estado_civil != "viudo/a"
    ):

        print("Estado civil incorrecto.")

        estado_civil = input(
            "Ingrese Soltero/a, Casado/a, Divorciado/a o Viudo/a: "
        ).lower()

    # VALIDAR NUMERO DE LEGAJO

    legajo = int(input("Ingrese su numero de legajo (4 cifras): "))

    while legajo < 1000 or legajo > 9999:

        print("Legajo incorrecto. Debe tener 4 cifras.")

        legajo = int(input("Ingrese nuevamente su legajo: "))

    # MOSTRAR LOS DATOS

    print("\n===== DATOS INGRESADOS =====")

    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Estado civil:", estado_civil)
    print("Numero de legajo:", legajo)
