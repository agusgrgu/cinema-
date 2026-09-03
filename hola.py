import main
peliculas = []
entradaprecio = []

def agrega_pelicula(lista_salas, lista_id_sala, lista_sala_asignada):
    """
    Agrega una pelicula a la cartelera.
    Y le asigna una sala de cine.

    Esta función se puede acceder desde el menú de administrador.
    """
    nombre_pelicula = input("\nIngrese el nombre de la pelicula a agregar: ")
    main.consultar_tamaño_sala(lista_salas, lista_id_sala)
    asignar_sala = main.verificar_entero()    
    while lista_id_sala[asignar_sala-1] in lista_sala_asignada or asignar_sala > len(lista_id_sala):
        if lista_id_sala[asignar_sala-1] in lista_sala_asignada:
          print("\nLa sala ya tiene asignada una pelicula.")
          main.consultar_tamaño_sala(lista_salas, lista_id_sala)
          asignar_sala = main.verificar_entero()
        if asignar_sala > len(lista_id_sala):
          print("\nLa sala no existe.")
          main.consultar_tamaño_sala(lista_salas, lista_id_sala)
          asignar_sala = main.verificar_entero()
    
    asignar_sala = lista_id_sala[asignar_sala-1]
    return nombre_pelicula , asignar_sala

def mostrar_cartelera(cantentrada):
    #muestra las entradas y sus precios junto con las entradas disponibles
    for i in range(len(peliculas)):
        print ("Película: ", peliculas[i], "Precio de entrada: ", entradaprecio[i], "Entradas disponibles: ", cantentrada)

def modifica_la_pelicula(pelicula):
    #modifica nombre y precio de la pelicula
    if pelicula in peliculas:
        modificar = input("que desea modificar? nombre o precio")
        if modificar == "precio":
            precioact = input("ingrese el precio de la pelicula")
            entradaprecio[[peliculas.index(pelicula)]] =precioact
        elif modificar == "nombre":
            nombreact = input("ingrese el nombre de la pelicula")
            peliculas[[peliculas.index(pelicula)]] =nombreact
        else:
            print("invalido")
