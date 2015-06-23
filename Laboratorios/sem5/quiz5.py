directorio = {}

opc = 0

while opc < 5:
    print("\t\t\tBienvenido al Directorio Telefónico\n\n")
    print("1. Imprimir números telefónicos\n2. Agregar números telefónicos\n3. Quitar números telefónicos")
    print("4. Buscar números telefónicos\n5. Salir del Sistema")

    opc = int(input("\nIndique la acción que desea realizar: "))

    if (opc == 1):
        print ("\n***Su selección ha sido imprimir números telefónicos***\n")

        if not directorio:
            print ("El directorio no contiene datos, no hay elementos que mostrar\n")
        else:
            print (directorio)

    elif (opc == 2):

        print ("\n***Su selección ha sido agregar números telefónicos***\n")
        directorio[input("Nombre: ")] = input("Número: ")

    elif (opc == 3):
        print ("\n***Su selección ha sido quitar números telefónicos***\n")
        del directorio[input("Nombre: ")]

    elif (opc == 4):
        print ("\n***Su selección ha sido buscar números telefónicos***\n")

        if not directorio:
            print ("El directorio no contiene datos, no hay elementos que mostrar\n")
        else:
            print("El número es: ", directorio[input("Nombre: ")])

        opc == 6
