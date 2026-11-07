# EJERCICIO 1
# Mostrar 10 repeticiones de numeros ascendentes del 1 al 10

def ejercicio_1():
    numero = 1

    while numero <= 10:
        print(numero)
        numero += 1


# EJERCICIO 2
# Mostrar 10 repeticiones de numeros descendentes del 10 al 1

def ejercicio_2():
    numero = 10

    while numero >= 1:
        print(numero)
        numero -= 1


# EJERCICIO 3
# Mostrar la suma de los numeros desde el 1 hasta el 10

def ejercicio_3():
    numero = 1
    suma = 0

    while numero <= 10:
        suma += numero
        numero += 1

    print("La suma es:", suma)


# EJERCICIO 4
# Mostrar la suma de los numeros pares desde el 1 hasta el 10

def ejercicio_4():
    numero = 1
    suma = 0

    while numero <= 10:
        if numero % 2 == 0:
            suma += numero

        numero += 1

    print("La suma de los pares es:", suma)


# EJERCICIO 5
# Solicitar 5 numeros, calcular suma y promedio

def ejercicio_5():
    contador = 1
    suma = 0

    while contador <= 5:
        numero = float(input("Ingrese un numero: "))
        suma += numero
        contador += 1

    promedio = suma / 5

    print("La suma es:", suma)
    print("El promedio es:", promedio)


# EJERCICIO 6
# Solicitar numeros hasta que el usuario no quiera ingresar mas

def ejercicio_6():
    suma = 0
    contador = 0
    continuar = "s"

    while continuar == "s":
        numero = float(input("Ingrese un numero: "))
        suma += numero
        contador += 1

        continuar = input("Desea ingresar otro numero? (s/n): ").lower()

    if contador > 0:
        promedio = suma / contador

        print("La suma es:", suma)
        print("El promedio es:", promedio)


# EJERCICIO 7
# Calcular la suma de positivos y el producto de negativos

def ejercicio_7():
    suma_positivos = 0
    producto_negativos = 1
    cantidad_negativos = 0
    continuar = "s"

    while continuar == "s":
        numero = float(input("Ingrese un numero: "))

        if numero > 0:
            suma_positivos += numero

        elif numero < 0:
            producto_negativos *= numero
            cantidad_negativos += 1

        continuar = input("Desea ingresar otro numero? (s/n): ").lower()

    print("La suma de los positivos es:", suma_positivos)

    if cantidad_negativos > 0:
        print("El producto de los negativos es:", producto_negativos)
    else:
        print("No se ingresaron numeros negativos.")


# EJERCICIO 8
# Ingresar 10 numeros enteros. Determinar maximo y minimo

def ejercicio_8():
    contador = 1

    numero = int(input("Ingrese un numero: "))

    maximo = numero
    minimo = numero

    while contador < 10:
        numero = int(input("Ingrese un numero: "))

        if numero > maximo:
            maximo = numero

        if numero < minimo:
            minimo = numero

        contador += 1

    print("El numero maximo es:", maximo)
    print("El numero minimo es:", minimo)


# EJERCICIO 9
# Solicitar como minimo 5 numeros. Calcular suma y promedio

def ejercicio_9():
    contador = 0
    suma = 0

    while contador < 5:
        numero = float(input("Ingrese un numero: "))
        suma += numero
        contador += 1

    continuar = input("Desea ingresar otro numero? (s/n): ").lower()

    while continuar == "s":
        numero = float(input("Ingrese otro numero: "))
        suma += numero
        contador += 1

        continuar = input("Desea ingresar otro numero? (s/n): ").lower()

    promedio = suma / contador

    print("La suma es:", suma)
    print("El promedio es:", promedio)


# EJERCICIO 10
# Solicitar minimo 5 numeros y maximo 10. Calcular suma y promedio

def ejercicio_10():
    contador = 0
    suma = 0

    while contador < 5:
        numero = float(input("Ingrese un numero: "))
        suma += numero
        contador += 1

    continuar = "s"

    while contador < 10 and continuar == "s":
        continuar = input("Desea ingresar otro numero? (s/n): ").lower()

        if continuar == "s":
            numero = float(input("Ingrese un numero: "))
            suma += numero
            contador += 1

    promedio = suma / contador

    print("La suma es:", suma)
    print("El promedio es:", promedio)

#EJERCICIO 11
def ejercicio_11():

    suma_negativos = 0
    suma_positivos = 0

    cantidad_negativos = 0
    cantidad_positivos = 0
    cantidad_total = 0

    mayor_positivo = None

    continuar = "s"

    while continuar == "s":

        numero = float(input("Ingrese un numero: "))

        cantidad_total += 1

        if numero < 0:

            suma_negativos += numero
            cantidad_negativos += 1

        elif numero > 0:

            suma_positivos += numero
            cantidad_positivos += 1

            if mayor_positivo is None or numero > mayor_positivo:
                mayor_positivo = numero

        continuar = input("Desea ingresar otro numero? (s/n): ").lower()

    print("\n===== RESULTADOS DEL INTEGRADOR =====")

    # A. Suma de numeros negativos
    print("A. Suma de negativos:", suma_negativos)

    # B. Suma de numeros positivos
    print("B. Suma de positivos:", suma_positivos)

    # C. Cantidad de numeros negativos
    print("C. Cantidad de negativos:", cantidad_negativos)

    # D. Promedio de numeros positivos
    if cantidad_positivos > 0:
        promedio = suma_positivos / cantidad_positivos
        print("D. Promedio de positivos:", promedio)
    else:
        print("D. No se ingresaron numeros positivos.")

    # E. Numero positivo mas grande
    if mayor_positivo is not None:
        print("E. Mayor numero positivo:", mayor_positivo)
    else:
        print("E. No se ingresaron numeros positivos.")

    # F. Porcentaje de numeros negativos
    if cantidad_total > 0:
        porcentaje = (cantidad_negativos * 100) / cantidad_total
        print("F. Porcentaje de negativos:", porcentaje, "%")
