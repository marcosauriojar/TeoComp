def q0(cadena, indice):
    if cadena[indice] == "a":
        q2(cracter[indice], indice)
    elif cadena[indice] == "b":
        q1(cadena[indice], indice)
    else:
        print("Cadena invalida")


def q1(cadena, indice):
    if cadena[indice+1] != "\0":
        if(cadena[indice+1] == "b" or cadena[indice] == "a"):
            print("Cadena invalida")
        elif cadena[indice+1] == "\0":
            print("Cadena válida")



cadena = input("ingresa la cadena que quieras validar con la expresion regular: a(a*b|b*) | b: \n")
print(cadena)

q0(cadena, 0)
