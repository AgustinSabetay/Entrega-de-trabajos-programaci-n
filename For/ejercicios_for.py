# GUIA ESTRUCTURAS REPETITIVAS - FOR
# ==========================================

# EJERCICIO 1
def ejercicio_1():

    for numero in range(1, 11):
        print(numero)

# EJERCICIO 2
def ejercicio_2():

    for numero in range(10, 0, -1):
        print(numero)

# EJERCICIO 3
def ejercicio_3():

    numero = int(input("Ingrese un numero: "))

    for i in range(0, numero + 1):
        print(i)

# EJERCICIO 4
def ejercicio_4():

    numero = int(input("Ingrese un numero: "))

    for i in range(0, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

# EJERCICIO 5
def ejercicio_5():

    suma = 0
    contador = 0

    for i in range(1, 11):

        numero = float(input("Ingrese un numero (0 para terminar): "))

        if numero == 0:
            break

        suma += numero
        contador += 1

    if contador > 0:

        promedio = suma / contador

        print("La suma es:", suma)
        print("El promedio es:", promedio)

    else:
        print("No se ingresaron numeros.")

# EJERCICIO 6
def ejercicio_6():

    for numero in range(1, 11):

        if numero % 3 == 0:
            print(numero)

# EJERCICIO 7
def ejercicio_7():

    for numero in range(1, 51):

        if numero % 2 == 0:
            print(numero)

# EJERCICIO 8
def ejercicio_8():

    numero = int(input("Ingrese un numero: "))

    for fila in range(1, numero + 1):

        for columna in range(1, fila + 1):
            print(columna, end="")

        print()

# EJERCICIO 9
def ejercicio_9():

    numero = int(input("Ingrese un numero: "))

    cantidad = 0

    for i in range(1, numero + 1):

        if numero % i == 0:

            print(i)
            cantidad += 1

    print("Cantidad de divisores:", cantidad)

# EJERCICIO 10
def ejercicio_10():

    numero = int(input("Ingrese un numero: "))

    es_primo = True

    if numero <= 1:
        es_primo = False

    else:

        for i in range(2, numero):

            if numero % i == 0:
                es_primo = False
                break

    if es_primo:
        print("El numero es primo.")

    else:
        print("El numero no es primo.")

# EJERCICIO 11
def ejercicio_11():

    numero = int(input("Ingrese un numero: "))

    cantidad_primos = 0

    for num in range(2, numero + 1):

        es_primo = True

        for i in range(2, num):

            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            print(num)
            cantidad_primos += 1

    print("Cantidad de numeros primos encontrados:", cantidad_primos)