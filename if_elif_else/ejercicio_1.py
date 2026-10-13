altura = int(input("Ingrese su altura en cm del 100 al 280: "))
if altura < 160:
    print("Sos base")
elif 160 <= altura <= 179:
    print("Sos escolta")
elif 180 <= altura <= 199:
    print("Sos alero")
else:
    print("Sos Ala-Pivot o Pivot")