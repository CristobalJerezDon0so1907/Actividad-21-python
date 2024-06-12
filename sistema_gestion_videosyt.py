import miactividad as m


while True:
    m.limpiar()
    print("Sistema De Gestion Videos Favoritos")
    print("═══════════════════════════════════")
    print("1.-) Guardar Video")
    print("2.-) Modificar Video")
    print("3.-) Eliminar Video")
    print("4.-) Listar Video")
    print("0.-) Salir")

    opcion = int(input("Seleccione : "))

    if opcion==0:
        break
    elif opcion==1:
        print("Guardar Video")
        videos = input("Ingrese nombre de video : ").title()
        nombre = input("Ingrese nombre : ").title()
        autor = input("Ingrese el nombre del autor : ").title()[0]
        duracion = int(input("Ingrese la duracion del video"))
        m.guardar(videos,nombre,autor,duracion)
    elif opcion==2:
        print("Modificar Video")
        indice = int(input("Ingrese el numero de video que quiera modificar ")) -1
        nombre = input("Ingrese nuevo nombre del video : ")
        autor = input("Ingrese nuevo autor del video : ")
        duracion = int(input("Ingrese la nueva duracion del video (en segundos) : "))
        m.modificar_video(videos,indice,nombre,autor,duracion)
    
    elif opcion==3:
        print("Eliminar Video")
        indice = int(input("Ingrese el numero de video a eliminar: "))-1
        m.eliminar(videos,indice,nombre,autor,duracion)
    elif opcion==4:
        print("Listar Video")
        m.listar
    else:
        print("opcion no valida")


