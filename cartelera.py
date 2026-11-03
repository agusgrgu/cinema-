import re
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
horarios_peliculas = {"titanic": ["14:00", "18:00", "22:00"], "star wars II": ["15:00", "19:00", "21:00"], "avengers": ["16:00", "20:00", "23:00"]}
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
        modificar = input("que desea modificar? nombre, precio o horario")
        while modificar != "precio" and modificar != "nombre" and modificar != "horario":
            print("opcion invalida")
            modificar = input("que desea modificar? nombre, precio o horario")
        if modificar == "precio":
            print ("ingrese el precio de la pelicula")
            precioact= verificar_entero ()
            peliculas[pelicula] = precioact
        elif modificar == "nombre":
            nombreact= input("ingrese el nombre de la pelicula")
            peliculas[nombreact] = peliculas.pop(pelicula)
        elif modificar == "horario":
            print("de que pelicula desea modificar los horarios?")
            horarios = input("Ingrese los nuevos horarios separados por comas (ejemplo: 14:00,18:00,22:00): ").split(",")
            patron= "[0-2]{1}[0-4]{1}:[0-6]{1}[0-9]{1}"
            if all(re.match(patron, horario) for horario in horarios):
                horarios_peliculas[pelicula] = horarios
            else:
                print("Error: Los horarios ingresados no tienen el formato correcto.")
        else:
            print("invalido")
    print(horarios_peliculas)


def pelicula_fuera(pelicula):
    #elimina la pelicula de la cartelera
    if pelicula in peliculas:
        del peliculas[pelicula]
        print("Película eliminada exitosamente.")
    else:
        print("La película no se encuentra en la cartelera.")


modifica_la_pelicula("titanic")