def q0(cadena, indice):
    if len(cadena) == 0:
        print("Cadena Invalida")
    elif indice == tam-1:
        print("Cadena Invalida")
    elif indice < tam-1:
        if cadena[indice] == "b":
            q3(cadena, indice)
        elif cadena[indice] == "a":
            q1(cadena, indice)
        else:
            print("Cadena invalida")


def q1(cadena, indice):
    if indice < tam-1:
        if cadena[indice+1] == "a":
            indice = indice+1
            q2(cadena,indice)
        elif cadena[indice+1] == "b":
            indice = indice +1
            q0(cadena, indice)
        else:
            print("Cadena Invalida")

    elif indice == tam-1:
        print("Cadena invlida")


def q2(cadena,indice):
    #print(str(indice+1))
    if indice == tam-1:
        print("Cadena válida")
    elif indice < tam-1:
        indice = indice +1
        #print(cadena[indice] + " " + str(indice))
        if cadena[indice] == "b":
            #indice = indice + 1
            q2(cadena, indice)
        elif cadena[indice] == "a":
            #indice = indice + 1
            q2(cadena, indice)
        else:
            print("Cadena Invalida")


def q3 (cadena, indice):
    if indice < tam-1:
        if cadena[indice+1] == "b":
            indice = indice+1
            q2(cadena,indice)
        elif cadena[indice+1] == "a":
            indice = indice +1
            q0(cadena, indice)
        else:
            print("Cadena Invalida")

    elif indice == tam-1:
        print("Cadena invlida")


def q4(cadena, indice):
    if indice == tam-1:
        print("Cadena válida")
    elif indice < tam-1:
        indice = indice +1
        #print(cadena[indice] + " " + str(indice))
        if cadena[indice] == "b":
            #indice = indice + 1
            q2(cadena, indice)
        elif cadena[indice] == "a":
            #indice = indice + 1
            q2(cadena, indice)
        else:
            print("Cadena Invalida")


cadena = input("ingresa la cadena que quieras validar con la expresion regular: (a|b)*(aa|bb)(a|b)*: \n")

#print(cadena[1])
tam = len(cadena)
#print(str(tam))
ind = 0
q0(cadena, ind)
