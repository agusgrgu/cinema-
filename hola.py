peliculas= []
entradaprecio= []
def agrega_pelicula(cantidad):
    #agrega la pelicula y su precio
    for i in range(cantidad):
        nombre = input("Ingrese el nombre de la película: ")
        precio= input("¿cuanto costara cada entrada?")
        entradaprecio.append(precio)
        peliculas.append(nombre)
    print("Películas agregadas exitosamente.")
    return peliculas, entradaprecio

def mostrar_cartelera(cantentrada):
    #muestra las entradas y sus precios junto con las entradas disponibles
    for i in range(len(peliculas)):
        print ("Película: ", peliculas[i], "Precio de entrada: ", entradaprecio[i], "Entradas disponibles: ", cantentrada)

def modifica_la pelicula(pelicula):
    #modifica nombre y precio de la pelicula
    if pelicula in peliculas:
        modifica=input("que desea modificar? nombre o precio")
        if modificar == "precio":
            precioact = input("ingrese el precio de la pelicula")
            entradaprecio[[peliculas.index(pelicula)]] =precioact
        elif modificar == "nombre":
            nombreact = input("ingrese el nombre de la pelicula")
            peliculas[[peliculas.index(pelicula)]] =nombreact
        else:
            print("invalido")


def pelicula_fuera(pelicula):
    #elimina la pelicula de la cartelera
    if pelicula in peliculas:
        peliculas.remove(pelicula)
        entradaprecio.pop(peliculas.index(pelicula))
        print("Película eliminada exitosamente.")
    else:
        print("La película no se encuentra en la cartelera.")