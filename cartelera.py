<<<<<<< HEAD
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
=======
<<<<<<<< HEAD:hola.py
========
peliculas= []
entradaprecio= []
>>>>>>> e0d6e83654c188cdac3105e0c938ec84d5d23646
def agrega_pelicula(cantidad):
    #agrega la pelicula y su precio
    for i in range(cantidad):
        nombre = input("Ingrese el nombre de la película: ")
<<<<<<< HEAD
        print("¿cuanto costara cada entrada?")
        precio = verificar_entero()
        peliculas[nombre] = precio
    print("Películas agregadas exitosamente.")

def mostrar_cartelera():
    #muestra las entradas y sus precios junto con las entradas disponibles
    for nombre, precio in peliculas.items():
        print("Película: ",  nombre, "Precio de entrada: ", precio)
        print("")
=======
        precio= input("¿cuanto costara cada entrada?")
        entradaprecio.append(precio)
        peliculas.append(nombre)
    print("Películas agregadas exitosamente.")
    return peliculas, entradaprecio

def mostrar_cartelera(cantentrada):
    #muestra las entradas y sus precios junto con las entradas disponibles
    for i in range(len(peliculas)):
        print ("Película: ", peliculas[i], "Precio de entrada: ", entradaprecio[i], "Entradas disponibles: ", cantentrada)
>>>>>>> e0d6e83654c188cdac3105e0c938ec84d5d23646

def modifica_la_pelicula(pelicula):
    #modifica nombre y precio de la pelicula
    if pelicula in peliculas:
        modificar = input("que desea modificar? nombre o precio")
<<<<<<< HEAD
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
=======
        if modificar == "precio":
            precioact = input("ingrese el precio de la pelicula")
            entradaprecio[[peliculas.index(pelicula)]] =precioact
        elif modifica == "nombre":
            nombreact = input("ingrese el nombre de la pelicula")
            peliculas[[peliculas.index(pelicula)]] =nombreact
>>>>>>> e0d6e83654c188cdac3105e0c938ec84d5d23646
        else:
            print("invalido")


def pelicula_fuera(pelicula):
    #elimina la pelicula de la cartelera
    if pelicula in peliculas:
<<<<<<< HEAD
        del peliculas[pelicula]
        print("Película eliminada exitosamente.")
    else:
        print("La película no se encuentra en la cartelera.")


pelicula_fuera("titanic")
print (peliculas)
=======
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
    
>>>>>>>> e0d6e83654c188cdac3105e0c938ec84d5d23646:cartelera.py
>>>>>>> e0d6e83654c188cdac3105e0c938ec84d5d23646
