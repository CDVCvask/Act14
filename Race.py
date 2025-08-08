def Menu():
    print("Copa piston")
    print("1.Agregar participantes")
    print("2.Mostrar participantes ordenados por nombre")
    print("3.Mostrar participantes ordenados por edad")
    print("4.Salir")
allow = False
allow1 = False
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    print(" ")
    match opt:
        case 1:
            num = int(input("Cuantos participantes desea ingresar: "))
        case 2:
            if allow1 == False:
                print("Aún no hay ningún dato")
            else:
                print("Show")
        case 3:
            if allow1 == False:
                print("Aún no hay ningún dato")
            else:
                print("Show")
        case 4:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")
