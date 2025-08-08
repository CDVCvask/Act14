def Menu():
    print("Copa piston")
    print("1.Agregar participantes")
    print("2.Mostrar participantes ordenados por nombre")
    print("3.Mostrar participantes ordenados por edad")
    print("4.Salir")
allow = False
allow1 = False
participants = {}
count = 0
while allow == False:
    Menu()
    opt = int(input("Ingrese la opción que desee: "))
    print(" ")
    match opt:
        case 1:
            check
            num = int(input("Cuantos participantes desea ingresar: "))
            if num <= 0:
                print("La cantidad ingresada no es valida")
            else:
                for i in range(num):
                    code = f"D{count}"
                    name = input("Ingrese el nombre completo del participante: ")
                    if name == "":
                        print("No puede dejar este espacio vacio")
                    else:
                        category = input("Ingrese el categoria del participante: ")
                        check = category.lower()
                        if check == "juvenil" or check == "adulto" or check == "master":
                            participants[name] = num
                        else:
                            print("La categoría no es valida solo se aceptan: Juvenil, Adulto y Master")
                    count = count + 1
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
