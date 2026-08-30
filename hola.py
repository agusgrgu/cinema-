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

def modifica_la_pelicula(pelicula):
    #modifica nombre y precio de la pelicula
    if pelicula in peliculas:
        modifica=input("que desea modificar? nombre o precio")
        if modifica == "precio":
            precioact = input("ingrese el precio de la pelicula")
            entradaprecio[[peliculas.index(pelicula)]] =precioact
        elif modifica == "nombre":
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
        
print("bienveidos al sistema de gestion de peliculas: ")
print("1. agregar pelicula")
print("2. mostrar cartelera")
print("3. modificar pelicula")
print("4. eliminar pelicula")
print("5. salir")
print("ingrese la opcion que desea realizar: ")
a = int(input())
if a == 1:
    agrega = int(input("ingrese la cantidad de peliculas que desea agregar: "))
    agrega_pelicula(agrega)
    print("peliculas agregadas: ", agrega)
elif a == 2:
    peliculas = int(input("ingrese la cantidad de entradas disponibles para la pelicula: "))
    mostrar_cartelera(peliculas)
    print("cartelera mostrada correctamente.")
    print("peliculas disponibles: ", peliculas)
elif a == 3:
    modificar = input("ingrese la pelicula que desea  modificar: ")
    modifica_la_pelicula(modificar)
elif a == 4:
    pelicula = input("ingrese la pelicula que desea eliminar: ")
    pelicula_fuera(pelicula)
elif a == 5:
    print("---saliendo del sistema de gestion de peliculas---")
    