
def verificar_entero():
    """
    Verifica que el valor ingresado sea un número entero.
    """
    entrada = input("Ingrese su opcion: ")

    while not entrada.isdigit():
        print("Error: Debe ingresar un número entero.")
        entrada = input("Ingrese su opcion: ")

    return int(entrada)
# Modulo cartelera
peliculas= {"titanic": 650, "star wars II": 420, "avengers": 135}
def agrega_pelicula(cantidad):
    #agrega la pelicula y su precio
    for i in range(cantidad):
        nombre = input("Ingrese el nombre de la película: ")
        print("¿cuanto costara cada entrada?")
        while True:
            try:
                precio = int(input("Ingrese el precio de la entrada: "))
                if precio > 0:
                    break
                print("Error: El precio debe ser mayor que cero.")
            except ValueError:
                print("Error: Debe ingresar un número entero para el precio.")
        if nombre in peliculas:
            print("la pelicula ya se encuentra en cartelera")
        else:
            peliculas[nombre] = precio
    print("Películas agregadas exitosamente.")
    #verificada

def mostrar_cartelera():
    #muestra las entradas y sus precios junto con las entradas disponibles
    for nombre, precio in peliculas.items():
        print("Película: ",  nombre, "Precio de entrada: ", precio)
        print("")
def modificar_pelicula(pelicula):
    #modifica precio o nombre de la pelicula
    if pelicula in peliculas:

        opcioninv= True
        while opcioninv == True:
            print("¿Qué desea modificar?")
            print("1. Nombre de la película")
            print("2. Precio de la entrada")
            opcion = verificar_entero()
            if opcion == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
                peliculas[nuevo_nombre] = peliculas.pop(pelicula)
                print("Nombre de la película modificado exitosamente.")
                opcioninv= False
            elif opcion == 2:
                print("Ingrese el nuevo precio de la entrada: ")
                print("¿cuanto costara cada entrada?")
                while True:
                    try:
                        nuevo_precio = int(input("Ingrese el precio de la entrada: "))
                        if nuevo_precio > 0:
                              break
                        print("Error: El precio debe ser mayor que cero.")
                    except ValueError:
                        print("Error: Debe ingresar un número entero para el precio.")
                peliculas[pelicula] = nuevo_precio
                print("Precio de la entrada modificado exitosamente.")
                opcioninv= False
            else:
                print("Opción inválida, inice de nuevo e ingrse 1 o 2.")
                opcioninv= True
        
    else:
        print("La película no se encuentra en la cartelera.")
        
def eliminar_pelicula(pelicula):
    if pelicula in peliculas:
        del peliculas[pelicula]
        print("Película eliminada exitosamente.")
    else:
        print("La película no se encuentra en la cartelera.")
print(peliculas.values())