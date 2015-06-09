Vendedor = input("\nNombre del Vendedor: ")
Mes1 = float(input("\nVentas del Mes # 1: "))
Mes2 = float(input("Ventas del Mes # 2: "))
Mes3 = float(input("Ventas del Mes # 3: "))


vent_total = (Mes1 + Mes2 + Mes3)

comisiones = ((vent_total *12.5))/100

print("\nINFORME DE COMISIONES\n\nVendedor\t\tVentas\t\tComision")
print("-------\t\t\t------\t\t--------")
print(Vendedor, "\t\t\t", "$", int(vent_total),"\t\t", "$", int(comisiones))
