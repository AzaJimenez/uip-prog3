texto = [] # Lista que almacena la cadena de caracteres a cifrar
caracter = texto # Variable que sirve para recorrer la cadena caracter por caracter
var = 0
var1 = 0
opc = 0 #Variable que controla el menú

while opc < 5: # Inicio del ciclo en el que está el menú de opciones a realizar
    print("\t\t\tCifrado de Mensajes de Correo Electrónico\n\n")
    print("1. Introducir texto por teclado\n2. Cifrar Texto\n3. Descifrar Texto")
    print("4. Imprimir Texto\n5. Salir del Sistema")

    opc = int(input("\nIndique la acción que desea realizar: ")) #Aquí se almacena el valor que conduce a las distintas opciones del menú

    if (opc == 1): # Primera Opcion: Introducir el texto que luego se va a cifrar
        print ("\n***Su selección ha sido: Introducir texto por teclado***\n")
        texto = input("Su texto a almacenar es: ")

    elif (opc == 2): # Segunda Opción: Cifrar el texto previamente almacenado
        print ("\n***Su selección ha sido: Cifrar Texto***\n")
        if not texto: #Ciclo If que muesta un mensaje si al momento de cifrar, no hay datos almacenados previamente.
            print ("El directorio no contiene datos, no hay elementos que cifrar\n")
        else:
            var1 = ""
            for caracter in texto:
                ord(caracter)
                caracter = var
                var = var + 1
                print(chr(var))
                var1 = var1 + chr(var)

    elif (opc == 3): # Tercera Opcion: Descifrar el texto previamente cifrado
        print ("\n***Su selección ha sido: Descifrar Texto***\n")
        if not texto: #Ciclo If que muesta un mensaje si al momento de descifrar, no hay datos cifrados previamente.
            print ("El directorio no contiene datos, no hay elementos que descifrar\n")
        else:
            for caracter in var1:
                ord(var1)
                var1 = var
                var = var - 1
                print (ord(var))
                var1 = var1 + ord(var)

    elif (opc == 4): # Cuarta Opcion: Imprimir El texto, ya sea cifrado o no
        print ("\n***Su selección ha sido: Imprimir Texto***\n")

        if not texto: #Ciclo If que muesta un mensaje si se manda a imprimir, no habiando almacenado datos previamente.
            print ("El directorio no contiene datos, no hay elementos que mostrar\n")
        elif not var1:
            print(texto)
        else:
            print (var1)

        opc == 6
