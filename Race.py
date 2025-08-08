def Menu():
    print("Copa piston")
    print("1.Agregar participantes")
    print("2.Mostrar participantes ordenados por nombre")
    print("3.Mostrar participantes ordenados por edad")
    print("4.Salir")
def Q_S_Name(Dict):
    piv = " "
    lower = {}
    same = {}
    uppper = {}
    if len(Dict) <= 1:
        return Dict
    else:
        for key, value in Dict.items():
            piv = value['Nombre']
            break
        for key, value in Dict.items():
            if value['Nombre'] < piv:
                lower[key] = {'Nombre': value['Nombre'], 'Edad': value['Edad'],'Categoria': value['Categoria']}
            if value['Nombre'] == piv:
                same[key] = {'Nombre': value['Nombre'], 'Edad': value['Edad'], 'Categoria': value['Categoria']}
            if value['Nombre'] > piv:
                uppper[key] = {'Nombre': value['Nombre'], 'Edad': value['Edad'], 'Categoria': value['Categoria']}
        return {**Q_S_Name(lower), **same, **Q_S_Name(uppper)}
def Q_S_Age(Dict):
    piv = " "
    lower = {}
    same = {}
    uppper = {}
    if len(Dict) <= 1:
        return Dict
    else:
        for key, value in Dict.items():
            piv = value['Edad']
            break
        for key, value in Dict.items():
            if value['Edad'] < piv:
                lower[key] = {'Nombre:': value['Nombre'], 'Edad': value['Edad'], 'Categoria': value['Categoria']}
            if value['Edad'] == piv:
                same[key] = {'Nombre:': value['Nombre'], 'Edad': value['Edad'], 'Categoria': value['Categoria']}
            if value['Edad'] > piv:
                uppper[key] = {'Nombre:': value['Nombre'], 'Edad': value['Edad'], 'Categoria': value['Categoria']}
        return {**Q_S_Age(lower), **same, **Q_S_Age(uppper)}
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
            check = ""
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
                        age = int(input("Ingrese el edad del participante: "))
                        if age < 16:
                            print("Edad no valida")
                        else:
                            category = input("Ingrese el categoria del participante: ")
                            check = category.lower()
                            if check == "juvenil" or check == "adulto" or check == "master":
                                participants[code] = {'Nombre': name, 'Edad': age, 'Categoria': category.capitalize()}
                                allow1 = True
                            else:
                                print("La categoría no es valida solo se aceptan: Juvenil, Adulto y Master")
                    count = count + 1
        case 2:
            if allow1 == False:
                print("Aún no hay ningún dato")
            else:
                sorted = Q_S_Name(participants)
                for code,value in sorted.items():
                    print(f"Dorsal{code}, Nombre: {value['Nombre']}, Edad: {value['Edad']}, Categoria: {value['Categoria']}")
        case 3:
            if allow1 == False:
                print("Aún no hay ningún dato")
            else:
                sorted = Q_S_Age(participants)
        case 4:
            print("Gracias por utilizar el programa")
            break
        case _:
            print("La opción seleccionada no es valida")
