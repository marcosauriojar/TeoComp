def q0(cadena, indice):
    if cadena[indice] == "a":
        q2(cracter[indice], indice)
    elif cadena[indice] == "b":
        q1(cadena[indice], indice)
    else:
        print("Cadena invalida")


def q1(cadena, indice):
    if indice < tam-1:
        print("Cadena Invalida")

    elif indice == tam-1:
        print("Cadena válida")


def q2(cadena,indice):
    if indice == tam-1:
        print("Cadena válida")
    elif indice < tam-1:
        if cadena[indice+1] == "b":
            indice = indice + 1
            q3(cadena, indice)
        elif cadena[indice+1] == "a":
            indice = indice + 1
            q4(cadena, indice)
        else:
            print("Cadena Invalida")
    #if indice+1 < tam-1:





cadena = input("ingresa la cadena que quieras validar con la expresion regular: a(a*b|b*) | b: \n")
tam = len(cadena)


q0(cadena, 0)
