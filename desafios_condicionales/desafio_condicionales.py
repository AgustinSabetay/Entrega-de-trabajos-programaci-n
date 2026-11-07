print("GOTITA S.A")

tipo_cliente = input("Ingrese que tipo de cliente es (residencial, comercial o industrial): ")
mtrs_consumidos = int(input("Ingrese la cantidad de metros consumidos: "))

tarifa_base = 7000
costo_mtr_cubico = 200
costo_consumo = mtrs_consumidos * costo_mtr_cubico
bonificacion = 0
recargos = 0

match tipo_cliente:
    case "residencial":
        if tipo_cliente == "residencial" and mtrs_consumidos < 30:
            bonificacion = costo_consumo * 10 / 100
        elif tipo_cliente == "residencial" and mtrs_consumidos > 80:
            recargos = costo_consumo * 15 / 100

            subtotal = tarifa_base + costo_consumo - bonificacion + recargos
            IVA_aplicado = subtotal * 21 / 100
            total_final = subtotal + IVA_aplicado
    case "comercial":
        if tipo_cliente == "comercial" and mtrs_consumidos > 150:
            bonificacion = costo_consumo * 8 / 100
        elif tipo_cliente == "comercial" and mtrs_consumidos > 300:
            bonificacion = costo_consumo * 12 / 100
        elif tipo_cliente == "comercial" and mtrs_consumidos < 50:
            recargos = costo_consumo * 5 / 100
