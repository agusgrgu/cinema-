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
        precio = verificar_entero()
        peliculas[nombre] = precio
    print("Películas agregadas exitosamente.")

def mostrar_cartelera():
    #muestra las entradas y sus precios junto con las entradas disponibles
    for nombre, precio in peliculas.items():
        print("Película: ",  nombre, "Precio de entrada: ", precio)
        print("")

def modifica_la_pelicula(pelicula):
    #modifica nombre y precio de la pelicula
    if pelicula in peliculas:
        modificar = input("que desea modificar? nombre o precio")
        while modificar != "precio" and modificar != "nombre":
            print("opcion invalida")
            modificar = input("que desea modificar? nombre o precio")
        if modificar == "precio":
            print ("ingrese el precio de la pelicula")
            precioact= verificar_entero ()
            peliculas[pelicula] = precioact
        elif modificar == "nombre":
            nombreact= input("ingrese el nombre de la pelicula")
            peliculas[nombreact] = peliculas.pop(pelicula)
        else:
            print("invalido")


def pelicula_fuera(pelicula):
    #elimina la pelicula de la cartelera
    if pelicula in peliculas:
        del peliculas[pelicula]
        print("Película eliminada exitosamente.")
    else:
        print("La película no se encuentra en la cartelera.")


pelicula_fuera("titanic")
print (peliculas)