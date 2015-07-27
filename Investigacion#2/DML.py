import mysql.connector
import config_mysql

opc = 0

cursor = config_mysql.cursor
conector = config_mysql.conector


while opc < 5:
    print("\n\t\tManejo de MySQL desde Python\n\n",
        "\t\t1. Visualizar Datos en la BD\n",
        "\t\t2. Ingresar Datos en la BD\n",
        "\t\t3. Actualizar Datos en la BD\n",
        "\t\t4. Eliminar Datos en la BD\n",
        "\t\t5. Salir del Sistema\n")

    opc = int(input("\n\t\tElija una opcion: "))

    if (opc == 1):
        #import visualizarDatos

        print("\n******VISUALIZAR DATOS*****\n\nLos datos dentro de la BD son:\n")
        cursor = conector.cursor()
        cursor.execute("SELECT * FROM `tabla1` WHERE 1")
        for tabla1 in cursor.fetchall():
            print (tabla1)

    elif (opc == 2):
        print("\n*****INGRESAR DATOS*****")
        #import ingresarDatos
        ID = int(input("Ingresa el ID: "))
        Nomb = input("Ingresa el Nombre: ")
        Apell = input("Ingresa el Apellido: ")
        cursor = conector.cursor()
        # Ejecutamos la consulta
        cursor.execute ("INSERT INTO `tabla1`(`ID`, `Nombre`, `Apellido`) VALUES ('%i', '%s', '%s')" % (ID, Nomb, Apell))
        # Confirma los cambios en la base de datos
        conector.commit()
        # Cerramos cursor
        cursor.close()

        print("\nLos datos insertados en la tabla son: " + "\n\nID: " + str(ID) + "\nNombre: " + Nomb + "\nApellido: " + Apell)

    elif (opc == 3):
        print("\n*****ACTUALIZAR DATOS*****")
        #import actualizarDatos
        ID = int(input("ID: "))
        print("Que dato deseas actualizar?"+ "\nNombre = 1; Apellido = 2; Ambos = 3     ")
        mod = int(input())

        while mod < 4:

            if (mod == 1):
                Nomb = input("Nuevo Nombre: ")
                cursor = conector.cursor()
                cursor.execute ("UPDATE `practica`.`tabla1` SET `Nombre` = '%s' WHERE `tabla1`.`ID` = '%i'" % (Nomb, ID))
                print("\n\nLos datos dentro de la BD luego de actualizar son:\n")
                cursor.execute("SELECT `ID`, `Nombre`, `Apellido` FROM `tabla1` WHERE 1")
                for tabla1 in cursor.fetchall():
                    print (tabla1)
                    # Confirma los cambios en la base de datos
                    conector.commit()
                    # Cerramos cursor
                    cursor.close()
            elif (mod == 2):
                Apell = input("Nuevo Apellido: ")
                cursor = conector.cursor()
                cursor.execute ("UPDATE `practica`.`tabla1` SET `Apellido` = '%s' WHERE `tabla1`.`ID` = '%i'" % (Apell, ID))
                print("\n\nLos datos dentro de la BD luego de actualizar son:\n")
                cursor.execute("SELECT `ID`, `Nombre`, `Apellido` FROM `tabla1` WHERE 1")
                for tabla1 in cursor.fetchall():
                    print (tabla1)
                    # Confirma los cambios en la base de datos
                    conector.commit()
                    # Cerramos cursor
                    cursor.close()
            elif (mod == 3):
                Nomb = input("Nuevo Nombre: ")
                Apell = input("Nuevo Apellido: ")
                cursor = conector.cursor()
                cursor.execute("UPDATE `practica`.`tabla1` SET `Nombre` = '%s', `Apellido` = '%s' WHERE `tabla1`.`ID` = '%i'"% (Nomb, Apell, ID))
                print("\n\nLos datos dentro de la BD luego de actualizar son:\n")
                cursor.execute("SELECT `ID`, `Nombre`, `Apellido` FROM `tabla1` WHERE 1")
                for tabla1 in cursor.fetchall():
                    print (tabla1)
                    # Confirma los cambios en la base de datos
                    conector.commit()
                    # Cerramos cursor
                    cursor.close()
                mod == 5

    elif (opc == 4):
        print("\n*****ELIMINAR DATOS*****")
        #import eliminarDatos
        ID = int(input("Inserte ID correspondiente a la entrada que desea eliminar: "))
        cursor = conector.cursor()
        # Ejecutamos la consula SQL
        cursor.execute ("DELETE FROM `practica`.`tabla1` WHERE `tabla1`.`ID` = '%i'" % (ID))
        print("\n\nLos datos dentro de la BD luego de la eliminacion son:\n")
        cursor = conector.cursor()
        cursor.execute("SELECT `ID`, `Nombre`, `Apellido` FROM `tabla1` WHERE 1")
        for tabla1 in cursor.fetchall():
            print (tabla1)
            # Confirma los cambios en la base de datos
            conector.commit()
            # Cerramos cursor
            cursor.close()

        opc == 6
