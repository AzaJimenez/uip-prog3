
list_sup = []

opc = 0

while opc < 4:

    """print ("\t\t\t\tStartUP ABC\n\t\t\tLISTA DE SUPERMERCADO\n\t\t\t")
    print ("\t", "1. Agregar elementos a su lista de supermercado")
    print ("\t", "2. Eliminar elementos de su lista de supermercado")
    print ("\t", "3. Ver los elementos existentes en su lista de supermercado\n")"""

    opc = int(input("Indique la acción que desea realizar: "))

    if (opc == 1):
        print ("Ha seleccionado agregar elementos a su lista de supermercado")
        list_sup.append(input())

    elif (opc == 2):

        print ("Ha seleccionado eliminar elementos de su lista de supermercado")
        del list_sup[int(input())]

    elif (opc == 3):
        print ("Ha seleccionado ver los elementos de su lista de supermercado")

        if not list_sup:
            print ("La lista está vacía, no hay elementos que mostrar\n")
        else:
            print (list_sup)

        opc == 5
