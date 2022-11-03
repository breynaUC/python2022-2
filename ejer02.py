op = 1
texto = ""
cont = 0
cv = 0
while op!=5:
    print("=====MENU====")
    print("[1]. Ingresar Cadena.")
    print("[2]. # de espacios en blanco.")
    print("[3]. # de Vocales.")
    print("[4]. Dimensión de la cadena.")
    print("[5]. Salir")
    op = int(input("Opción [1-5]: "))
    if op == 1:
        texto = input("Ingresar frase: ")
    if op == 2:
        for cad in range(0, len(texto)):
            if texto[cad] == " ":
                cont+=1
        print("# de espacios en blanco: ",cont)
    if op == 3:
        for cad in range(0, len(texto)):
            if texto[cad] == "a" or texto[cad] == "e" or texto[cad] == "i" or texto[cad] == "o" or texto[cad] == "u":
                cv+=1
        print("# de vocales: ",cv)
    if op == 4:
        print("Longitud de la cadena: ",len(texto))