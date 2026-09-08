import re
from functools import reduce

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
peliculas= ["titanic", "star wars II", "avengers" ]
entradaprecio= [650, 420, 135]
def agrega_pelicula(cantidad):
    #agrega la pelicula y su precio
    for i in range(cantidad):
        nombre = input("Ingrese el nombre de la película: ")
        precio= input("¿cuanto costara cada entrada?")
        entradaprecio.append(precio)
        peliculas.append(nombre)
    print("Películas agregadas exitosamente.")
    return peliculas, entradaprecio

def mostrar_cartelera():
    #muestra las entradas y sus precios junto con las entradas disponibles
    for i in range(len(peliculas)):
        print ("Película: ", peliculas[i], "Precio de entrada: ", entradaprecio[i])

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


def pelicula_fuera(pelicula):
    #elimina la pelicula de la cartelera
    if pelicula in peliculas:
        entradaprecio.pop(peliculas.index(pelicula))
        peliculas.remove(pelicula)
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
    2 - Cambiar precio de entradas
    3 - Crear sala de cine
    4 - ventas
    5 - salir
    """)
    eleccion = verificar_entero()
    while eleccion < 1 or eleccion > 5:
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

nombres_peliculas = [
    "avengers",
    "star wars II",
    "titanic"
]

horarios_peliculas = [
    ["14:00", "18:00", "22:00"],
    ["15:00", "19:00", "21:00"],
    ["16:00", "20:00", "23:00"]
]


# LISTAS DE RESERVAS

clientes_reservas = []
peliculas_reservas = []
horarios_reservas = []
cantidades_reservas = []
asientos_reservas = []


def elegir_pelicula():

    print("===== PELICULAS DISPONIBLES =====")

    i = 0

    while i < len(nombres_peliculas):
        print(i + 1, nombres_peliculas[i])
        i = i + 1

    opcion = int(input("Elegí una pelicula: "))
    print("su costo sera", entradaprecio[opcion-1])
    while opcion < 1 or opcion > len(nombres_peliculas):
        print("Opcion invalida")
        opcion = int(input("Elegí una pelicula: "))

    pelicula = nombres_peliculas[opcion - 1]

    print("Película elegida:", pelicula)
    print("Horarios disponibles:")

    i = 0

    while i < len(horarios_peliculas[opcion - 1]):
        print(i + 1, horarios_peliculas[opcion - 1][i])
        i = i + 1

    horario_opcion = int(input("Elegí un horario: "))

    while horario_opcion < 1 or horario_opcion > len(horarios_peliculas[opcion - 1]):
        print("Horario invalido")
        horario_opcion = int(input("Elegí un horario: "))

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

    print("===== REALIZAR RESERVA =====")

    cliente = input("Ingresá el nombre del cliente: ")

    pelicula, horario = elegir_pelicula()

    cantidad = int(input("Cuantas entradas querés reservar: "))

    while cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
        cantidad = int(input("Cuantas entradas querés reservar: "))

    asientos = []

    i = 0

    while i < cantidad:
        imprimir_sala(sala)
        fila2= int(input("Ingresá la fila"))
        columna2 = int(input("Ingresá la columna"))
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
    numeros_telefonicos = []
    
    funciones_principal = menu_principal()
    while funciones_principal != 2:
        if funciones_principal == 1:
            usuario = input("Ingrese su nombre de usuario: ")
            usuario_valido = re.match(r'^[a-zA-Z0-9]+$', usuario)
            if not usuario_valido:
                while not usuario_valido:
                    print("Error: El nombre de usuario solo puede contener letras y números.")
                    usuario = input("Ingrese su nombre de usuario: ")
                    usuario_valido = re.match(r'^[a-zA-Z0-9]+$', usuario)
                
            contraseña = input("Cree una contraseña: ")
            numero_telefonico = input("Ingrese su número de teléfono y nombre completo para ser comunicado en caso de que se necesite ")
            patron_telefono = "[0-9]{2}-[0-9]{4}-[0-9]{4}"
            numero= re.findall(patron_telefono, numero_telefonico)
            numeros_telefonicos.append(numero_telefonico)

            if usuario == "admin" and contraseña == contraseña_admin:
                """
                ---------------------------- ↓↓↓ EMPIEZA BLOQUE DE FUNCIONES DE ADMIN ↓↓↓ ----------------------------------------------------
                """
                while contraseña_admin == "admin":
                    contraseña_admin = input("Cree una contraseña para administradores: ")
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
                          nombre=input("que pelicula desea eliminar?")
                          pelicula_fuera(nombre)
                      else:
                          print("Opción inválida. Intente nuevamente.")

                  elif funciones_admin == 2:
                      # CAMBIAR PRECIO DE ENTRADAS
                      print("cambiar precio de entrada")
                      print(f"Precio actual {precio_entrada}")
                      precio_entrada = verificar_entero()
                      print(f"Se actualizo el precio a {precio_entrada}")

                  elif funciones_admin == 3:
                      # CREAR SALA DE CINE
                      print("crear sala de cine")
                      filas= input("Ingrese la cantidad de filas: ")
                      columnas= input("Ingrese la cantidad de columnas: ")
                      crear_sala(filas, columnas)

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