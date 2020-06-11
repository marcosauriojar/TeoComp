def q0(cadena, indice):
    if len(cadena) == 0:
        print("Cadena Invalida")
    elif cadena[indice] == "a":
        q2(cadena, indice)
    elif cadena[indice] == "b":
        q1(cadena, indice)
    else:
        print("Cadena invalida")


def q1(cadena, indice):
    if indice < tam-1:
        print("Cadena Invalida")

    elif indice == tam-1:
        print("Cadena válida")


def q2(cadena,indice):
    #print(str(indice+1))
    if indice == tam-1:
        print("Cadena válida")
    elif indice < tam-1:
        indice = indice +1
        #print(cadena[indice] + " " + str(indice))
        if cadena[indice] == "b":
            #indice = indice + 1
            q3(cadena, indice)
        elif cadena[indice] == "a":
            #indice = indice + 1
            q4(cadena, indice)
        else:
            print("Cadena Invalida")


def q3 (cadena, indice):
    if indice == tam-1:
        print("Cadena Válida")
    elif indice < tam-1:
        if cadena[indice+1] == "b":
            indice = indice + 1
            q3(cadena, indice)
        else:
            print("cadena invalida")


def q4(cadena, indice):
    if indice == tam-1:
        print("Cadena Invalida")
    elif indice < tam -1:
        if cadena[indice+1] == "a":
            indice = indice +1
            q4(cadena, indice)
        elif cadena[indice +1] == "b":
            indice = indice +1
            q5(cadena, indice)
        else:
            print("Cadena invalida")


def q5(cadena, indice):
    if indice == tam-1:
        print("Cadena valida")
    elif indice < tam-1:
        if cadena[indice+1] == "b" or cadena [indice+1] == "a":
            print("Cadena invalida")
        else:
            print ("Cadena invalida")

    #if indice+1 < tam-1:





cadena = input("ingresa la cadena que quieras validar con la expresion regular: a(a*b|b*) | b: \n")

#print(cadena[1])
tam = len(cadena)
#print(str(tam))
ind = 0
q0(cadena, ind)
