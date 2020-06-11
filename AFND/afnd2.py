def q0(cadena, indice):
    #print(str(indice))
    if len(cadena) == 0:
        print("Cadena Vailda")
    elif cadena[indice] == "a":
        #indice = indice + 1
        q1(cadena, indice)
    elif cadena[indice] == "b":
        print("Cadena invalida")
    else:
        print("Cadena invalida")


def q1(cadena, indice):
#    print(str(indice))
    if indice == tam-1:
        print("Cadena invalida")
    elif indice < tam -1:
        if cadena[indice+1] == "b":
            indice = indice +1
            q2(cadena, indice)
        else:
            print("Cadena Invalida")


def q2(cadena, indice):
    #sprint(str(indice))
    if indice == tam-1:
        print("Cadena Valida")
    elif indice < tam - 1:
        if cadena[indice+1] == "a":
            indice = indice +1
            q3(cadena,indice)
        else:
            print("Cadena invalida")


def q3(cadena, indice):
#    print(str(indice))
    if indice == tam-1:
        print("Cadena Valida")
    elif indice < tam-1:
        if cadena[indice+1] == "a":
            indice = indice +1
            q1(cadena, indice)
        elif cadena[indice+1] == "b":
            indice = indice + 1
            q2(cadena,indice)
        else:
            print("Cadena Invalida")



cadena = input("ingresa la cadena que quieras validar con la expresion regular: (ab|aba)*: \n")

#print(cadena[1])
tam = len(cadena)
#print(str(tam))
ind = 0
q0(cadena, ind)
