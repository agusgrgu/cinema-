import re
from functools import reduce
import json
import os

def crear_sala(filas, columnas):
    sala = [["L" for j in range(columnas)] for i in range(filas)]
    return sala

def imprimir_sala(sala):
    for fila in sala:
        for butaca in fila:
            print(butaca, end=" ")
        print()

def verificar_butaca(sala, fila, columna):
    return fila >= 0 and fila < len(sala) and columna >= 0 and columna < len(sala[0]) and sala[fila][columna] == "L"

def ocupar_butaca(sala, fila, columna):
    if verificar_butaca(sala, fila, columna):
        sala[fila][columna] = "O"
        print("Reserva exitosa: La butaca ha sido ocupada.")
        return True 
    else:
        print("Error!: La butaca noo existe o ya esta ocupada.")
        return False

def contar_butacas(sala):
    libres = reduce(lambda a, b: a + b, map(lambda f: f.count("L"), sala))
    ocupadas = reduce(lambda a, b: a + b, map(lambda f: f.count("O"), sala))
    return libres, ocupadas


"""
------------------------------------- Termina modulo salas.py ---------------------------------------------------------------
"""


# Modulo cartelera
# Modulo cartelera
peliculas= {"titanic": 650, "star wars II": 420, "avengers": 135}
horarios_peliculas = {"titanic": ["14:00", "18:00", "22:00"], "star wars II": ["15:00", "19:00", "21:00"], "avengers": ["16:00", "20:00", "23:00"]}

def agrega_pelicula(cantidad):
    for i in range(cantidad):

        nombre = input("Ingrese el nombre de la película: ")

        if nombre in peliculas:
            print("La película ya se encuentra en cartelera.")
            continue

        # INGRESO DEL PRECIO
        while True:
            try:
                precio = int(input("Ingrese el precio de la entrada: "))

                if precio <= 0:
                    print("Error: El precio debe ser mayor que cero.")
                else:
                    break

            except ValueError:
                print("Error: Debe ingresar un número entero para el precio.")

        # INGRESO DE LOS HORARIOS
        while True:
            horarios = input(
                "Ingrese los horarios separados por comas "
                "(ejemplo: 14:00,18:00,22:00): "
            ).split(",")

            patron = r"(?:[01][0-9]|2[0-3]):[0-5][0-9]"

            if all(re.fullmatch(patron, horario.strip()) for horario in horarios):
                horarios = [horario.strip() for horario in horarios]
                break
            else:
                print("Error: Los horarios ingresados no tienen el formato correcto.")

        # AGREGAR PELICULA
        peliculas[nombre] = precio
        horarios_peliculas[nombre] = horarios

        print("Película agregada exitosamente.")

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
            if precioact <= 0:
                print("Error: El precio debe ser mayor que cero.")
                while precioact <= 0:
                    precioact= verificar_entero ()
                    if precioact <= 0:
                        print("Error: El precio debe ser mayor que cero.")
            peliculas[pelicula] = precioact
        elif modificar == "nombre":
            nombreact= input("ingrese el nombre de la pelicula")
            peliculas[nombreact] = peliculas.pop(pelicula)
        elif modificar == "horario":
            print("de que pelicula desea modificar los horarios?")
            horarios = input("Ingrese los nuevos horarios separados por comas (ejemplo: 14:00,18:00,22:00): ").split(",")
            patron = r"(?:[01][0-9]|2[0-3]):[0-5][0-9]"
            if all(re.fullmatch(patron, horario) for horario in horarios):
                horarios_peliculas[pelicula] = horarios
            else:
                print("Error: Los horarios ingresados no tienen el formato correcto.")
        else:
            print("invalido")


def pelicula_fuera(pelicula):
    #elimina la pelicula de la cartelera
    if pelicula in peliculas:
        del peliculas[pelicula]
        del horarios_peliculas[pelicula]
        print("Película eliminada exitosamente.")
    else:
        print("La película no se encuentra en la cartelera.")



"""
------------------------------------- ↑↑↑ Termina modulo cartelera.py ↑↑↑ -----------------------------------------------------------
"""

def menu_principal():
    """
    Muestra el menú principal y devuelve la opción seleccionada.
    """
    print("""
    Bienvenido al sistema de gestión de cine.
    Seleccione una opción:
    1 - Crear usuario
    2 - Salir
    """)
    opcion = verificar_entero()
    while opcion < 1 or opcion > 2:
        print("Opción inválida. Intente nuevamente.")
        opcion = verificar_entero()
    return opcion

def imprimir_funciones_admin():
    """
    Imprime las funciones disponibles para el administrador.

    Se accede escribiendo "admin" como nombre de usuario.
    """
    print("""
    Funciones disponibles:
    1 - Gestionar cartelera
    2 - cambiar caracteristicas de las peliculas
    3 - Crear sala de cine
    4 - ventas
    5 - Comprobar informacion clientes
    6 - Salir
    """)
    eleccion = verificar_entero()
    while eleccion < 1 or eleccion > 6:
        print("Opción inválida. Intente nuevamente.")
        eleccion = verificar_entero()
    return eleccion

def imprimir_funciones_usuario():
    """
    Imprime las funciones disponibles para el usuario. Permitiendo al usuario ver la cartelera y comprar entradas.

    Al escribir "admin" abre el menu para administradores.
    """
    print("""
    Funciones disponibles:
    1 - Mostar cartelera
    2 - Comprar entradas
    3 - Consultar reservas
    4 - Salir
    """)
    eleccion = verificar_entero()
    while eleccion < 1 or eleccion > 4:
        print("Opción inválida. Intente nuevamente.")
        eleccion = verificar_entero()
    return eleccion

def verificar_entero():
    """
    Verifica que el valor ingresado sea un número entero.
    """
    entrada = input("Ingrese su opcion: ")

    while not entrada.isdigit():
        print("Error: Debe ingresar un número entero.")
        entrada = input("Ingrese su opcion: ")

    return int(entrada)

"""
-------------------------------------- ↓↓↓ EMPIEZA entradas y reservas ↓↓↓ ----------------------------------------------------------------------
"""
# LISTAS DE PELICULAS

nombres_peliculas = list(peliculas.keys())
entradaprecio = list(peliculas.values())

horarios_peliculas = list(horarios_peliculas.values())

# LISTAS DE RESERVAS

clientes_reservas = []
peliculas_reservas = []
horarios_reservas = []
cantidades_reservas = []
asientos_reservas = []


def elegir_pelicula():
    nombres_peliculas = list(peliculas.keys())
    entradaprecio = list(peliculas.values())

    horarios_peliculas = list(horarios_peliculas.values())
    print("===== PELICULAS DISPONIBLES =====")

    i = 0

    while i < len(nombres_peliculas):
        print(i + 1, nombres_peliculas[i])
        i = i + 1

    opcion = verificar_entero()
    while opcion < 1 or opcion > len(nombres_peliculas) or opcion == "":
        print("Opcion invalida")
        opcion = verificar_entero()

    pelicula = nombres_peliculas[opcion - 1]
    print("su costo sera", entradaprecio[opcion-1])

    print("Película elegida:", pelicula)
    print("Horarios disponibles:")

    i = 0

    while i < len(horarios_peliculas[opcion - 1]):
        print(i + 1, horarios_peliculas[opcion - 1][i])
        i = i + 1

    horario_opcion = verificar_entero()

    while horario_opcion < 1 or horario_opcion > len(horarios_peliculas[opcion - 1]) or horario_opcion =="":
        print("Horario invalido")
        horario_opcion = verificar_entero()

    horario = horarios_peliculas[opcion - 1][horario_opcion - 1]

    return pelicula, horario


def guardar_reserva(cliente, pelicula, horario, cantidad, asientos):
    
    clientes_reservas.append(cliente)
    peliculas_reservas.append(pelicula)
    horarios_reservas.append(horario)
    cantidades_reservas.append(cantidad)
    asientos_reservas.append(asientos)

    print("Reserva guardada correctamente")


def realizar_reserva():
    nombres_peliculas = list(peliculas.keys())
    entradaprecio = list(peliculas.values())

    horarios_peliculas = list(horarios_peliculas.values())
    print("===== REALIZAR RESERVA =====")

    cliente = input("Ingresá el nombre del cliente: ")

    pelicula, horario = elegir_pelicula()
    print("Ingrese la cantidad de entradas que desea reservar:")
    cantidad = verificar_entero()

    while cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
        cantidad = verificar_entero()

    asientos = []

    i = 0

    while i < cantidad:
        imprimir_sala(sala)
        print("ingrese la fila ")
        fila2= verificar_entero()
        print("ingrese la columna ")
        columna2 = verificar_entero()
        fila2= fila2-1
        columna2= columna2 - 1
        ocupar_butaca(sala, fila2, columna2)
        i = i + 1

    guardar_reserva(cliente, pelicula, horario, cantidad, asientos)

    print("===== RESERVA =====")
    print("Cliente:", cliente)
    print("Película:", pelicula)
    print("Horario:", horario)
    print("Cantidad de entradas:", cantidad)


def buscar_reservas_cliente():

    print("===== BUSCAR RESERVAS =====")

    cliente = input("Ingresá el nombre del cliente: ")

    encontrado = False

    i = 0

    while i < len(clientes_reservas):

        if clientes_reservas[i] == cliente:

            encontrado = True

            print("===== RESERVA =====")
            print("Cliente:", clientes_reservas[i])
            print("Película:", peliculas_reservas[i])
            print("Horario:", horarios_reservas[i])
            print("Cantidad de entradas:", cantidades_reservas[i])

        i = i + 1

    if encontrado == False:
        print("No se encontraron reservas")
def ventas():
    print("===== VENTAS =====")
    total_ventas = 0
    for i in range(len(cantidades_reservas)):
        pelicula = peliculas_reservas[i]
        cantidad = cantidades_reservas[i]
        precio = entradaprecio[nombres_peliculas.index(pelicula)]
        total_venta = cantidad * precio
        total_ventas += total_venta
        print(f"Cliente: {clientes_reservas[i]}, Película: {pelicula}, Cantidad de entradas: {cantidad}, Total venta: ${total_venta}")
    print(f"Total de ventas: ${total_ventas}")
"""
-------------------------------------- ↓↓↓ EMPIEZA EL PROGRAMA PRINCIPAL ↓↓↓ ----------------------------------------------------------------------
"""
sala=crear_sala(2, 3)

def main():

    precio_entrada = 0
    lista_peliculas = []
    lista_salas = []
    lista_usuarios = []
    lista_contraseñas = []
    lista_id_usuario = []
    contraseña_admin = "admin"
    numeros_telefonicos = set()
    
    funciones_principal = menu_principal()
    while funciones_principal != 2:
        if funciones_principal == 1:
            usuario = input("Ingrese su nombre de usuario: ")
            usuario_valido = re.match(r'^[a-zA-Z0-9]+$', usuario)
            if usuario_valido:
                lista_usuarios.append(usuario)
            elif not usuario_valido:
                while not usuario_valido:
                    print("Error: El nombre de usuario solo puede contener letras y números.")
                    usuario = input("Ingrese su nombre de usuario: ")
                    usuario_valido = re.match(r'^[a-zA-Z0-9]+$', usuario)
                    if usuario_valido:
                        lista_usuarios.append(usuario)
            print(lista_usuarios)    
            contraseña = input("Cree una contraseña: ")
            lista_contraseñas.append(contraseña)
            numero_telefonico = input("Ingrese su número de teléfono para ser comunicado en caso de que se necesite ")
            patron_telefono = "[0-9]{2}-[0-9]{4}-[0-9]{4}"
            numero= re.findall(patron_telefono, numero_telefonico)
            if numero and numero_telefonico not in numeros_telefonicos:
                numeros_telefonicos.add(numero_telefonico)
                print("Número de teléfono válido y agregado a la lista.")
            elif numero_telefonico in numeros_telefonicos:
                print("Error: El número de teléfono ya ha sido ingresado previamente.")
                print("ingrese un número de teléfono diferente.")
                while not numero:
                                    print("Error: El número de teléfono no tiene el formato correcto. Debe ser XX-XXXX-XXXX.")
                                    numero_telefonico = input("Ingrese su número de teléfono para ser comunicado en caso de que se necesite ")
                                    numero = re.findall(patron_telefono, numero_telefonico)
                                    if numero and numero_telefonico not in numeros_telefonicos:
                                        numeros_telefonicos.add(numero_telefonico)
                                        print("Número de teléfono válido y agregado a la lista.")
            else:
                while not numero:
                    print("Error: El número de teléfono no tiene el formato correcto. Debe ser XX-XXXX-XXXX.")
                    numero_telefonico = input("Ingrese su número de teléfono para ser comunicado en caso de que se necesite ")
                    numero = re.findall(patron_telefono, numero_telefonico)
                    if numero and numero_telefonico not in numeros_telefonicos:
                        numeros_telefonicos.add(numero_telefonico)
                        print("Número de teléfono válido y agregado a la lista.")
            if usuario == "admin" and contraseña == contraseña_admin:
                """
                ---------------------------- ↓↓↓ EMPIEZA BLOQUE DE FUNCIONES DE ADMIN ↓↓↓ ----------------------------------------------------
                """
                try:
                    open("contraseña_admin.txt", "r")
                except FileNotFoundError:
                    contraseña_admin = input("Cree una contraseña para administradores: ")
                    contraseña_valida= filter(lambda x: x.isalnum(), contraseña_admin)
                    tuplecontra= tuple(contraseña_valida)
                    del contraseña_admin
                    del contraseña_valida
                    with open("contraseña_admin.txt", "w", encoding="utf-8") as archivo:
                        archivo.write("".join(tuplecontra))
                        print("su contraseña guardada es: ", "".join(tuplecontra))
                print("Ingrese la contraseña de administrador: ")
                contraseña_ingresada = input()
                if contraseña_ingresada != open("contraseña_admin.txt", "r").read():
                    print("Contraseña incorrecta. Acceso denegado.")
                    continue
                print("\nBienvenido al menu de administradores")
                funciones_admin = imprimir_funciones_admin()

                while funciones_admin != 5:

                  if funciones_admin == 1:
                      # GESTIONAR CARTELERA
                      print("1. Agregar pelicula")
                      print("2. Quitar pelicula")
                      
                      gestionar_cartelera = verificar_entero()

                      if gestionar_cartelera == 1:
                          print("Agregar pelicula")
                          cantidad = int(input("Ingrese la cantidad de películas a agregar: "))
                          agregopeli=agrega_pelicula(cantidad)
                      elif gestionar_cartelera == 2:
                          print("Quitar pelicula")
                          nombre = input("¿Qué pelicula desea eliminar? ")
                          if nombre == "":
                              print("Error al ingresar el nombre de la película.")
                          else:
                              pelicula_fuera(nombre)
                      else:
                          print("Opción inválida. Intente nuevamente.")

                  elif funciones_admin == 2:
                      # CAMBIAR pelicula
                      pelicula = input("Ingrese el nombre de la película que desea modificar: ")
                      if pelicula not in peliculas:
                          print("La película no se encuentra en la cartelera.")
                      modifica_la_pelicula(pelicula)
                      

                  elif funciones_admin == 3:
                      # CREAR SALA DE CINE
                      print("crear sala de cine")
                      filas= input("Ingrese la cantidad de filas: ")
                      columnas= input("Ingrese la cantidad de columnas: ")
                      crear_sala(filas, columnas)

                  elif funciones_admin == 4:
                      # VENTAS
                      ventas()
                  elif funciones_admin == 5:
                      #comprobando informacion de clientes
                      print(lista_usuarios, lista_contraseñas, lista_id_usuario, numeros_telefonicos)
                  elif funciones_admin == 6:
                      print("Saliendo del sistema...")
                      break
                  else:
                      print("Opción inválida. Intente nuevamente.")
                  funciones_admin = imprimir_funciones_admin()

                """
                ---------------------------- ↑↑↑ TERMINA BLOQUE DE FUNCIONES DE ADMIN ↑↑↑ ----------------------------------------------------
                """
            elif usuario != "admin": # Llegas aqui si ingresas cualquier usuario aparte de "admin"
                """
                ---------------------------- ↓↓↓ EMPIEZA BLOQUE DE FUNCIONES DE USUARIO ↓↓↓ ---------------------------------------------------
                """

                print("\nBienvenido!", usuario)
                funciones_usuario = imprimir_funciones_usuario()


                while funciones_usuario != 4:
                    if funciones_usuario == 1:
                        # MOSTRAR CARTELERA
                        print("Mostrar cartelera")
                        mostrarcarteleras = mostrar_cartelera()

                    elif funciones_usuario == 2:
                        # COMPRAR ENTRADAS
                        print("Comprar entradas")
                        realizar_reserva()

                    elif funciones_usuario == 3:
                        # CONSULTAR RESERVAS
                        print("Consultar reservas")
                        buscar_reservas_cliente()

                    else:
                        print("Opción inválida. Intente nuevamente.")
                    funciones_usuario = imprimir_funciones_usuario()
                """
                ----------------------------- ↑↑↑ TERMINA BLOQUE DE FUNCIONES DE USUARIO ↑↑↑ ---------------------------------------------------
                """
            else: # Llegas aqui si ingresas "admin" como usuario pero la contraseña de admin incorrecta.
                print("\nUSUARIO INVALIDO. INTENTE NUEVAMENTE.")

        else: # Llegas aqui si escribes un dato invalido en funcion principal.
            print("Opción inválida. Intente nuevamente.")
        funciones_principal = menu_principal()

    print("Saliendo del sistema...")

main()