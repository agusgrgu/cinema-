import random
import salas
import estadisticas
import hola

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
    4 - Mostrar estadisticas
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

def funcion_gestionar_cartelera():
    """
    Gestiona la cartelera del cine.

    Esta función se puede acceder desde el menú de administrador.
    """
    print("""
    1 - Agregar pelicula 
    2 - Quitar pelicula
    3 - Volver
    """)
    eleccion = verificar_entero()
    while eleccion < 1 or eleccion > 3:
        print("Opción inválida. Intente nuevamente.")
        eleccion = verificar_entero()
    return eleccion

def consultar_tamaño_sala(lista_salas , lista_id_sala):
    """
    Consulta el tamaño de la sala de cine.
    """
    for i in range(len(lista_salas)):
        print(f"ID de la sala: {lista_id_sala[i]}")
        print(f"Sala {i+1}: {len(lista_salas[i])} filas x {len(lista_salas[i][0])} columnas")
        print("-"*30)

def imprimir_lista_enumerada(lista):
    """
    Imprime una lista enumerada.
    """
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i]}")

def crear_id(lista_id):
    """
    Crea un ID de 4 digitos unico para agregar a una lista paralela
    """
    id = random.randint(1000, 9999)
    while id in lista_id:
        id = random.randint(1000, 9999)
    return id

"""
-------------------------------------- ↓↓↓ EMPIEZA EL PROGRAMA PRINCIPAL ↓↓↓ ----------------------------------------------------------------------
"""


def main():

    precio_entrada = 0
    lista_peliculas = []
    lista_salas = []
    lista_usuarios = []
    lista_contraseñas = []
    lista_sala_asignada = []
    lista_id_sala = []
    contraseña_admin = "admin"


    funciones_principal = menu_principal()
    while funciones_principal != 2:
        if funciones_principal == 1:
            usuario = input("Ingrese su nombre de usuario: ")
            contraseña = input("Cree una contraseña: ")


            if usuario == "admin" and contraseña == contraseña_admin:
                """
                ---------------------------- ↓↓↓ EMPIEZA BLOQUE DE FUNCIONES DE ADMIN ↓↓↓ ----------------------------------------------------
                """
                while contraseña_admin == "admin":
                    contraseña_admin = input("Cree una contraseña para administradores: ")
                print("\nBienvenido al menu de administradores")
                funciones_admin = imprimir_funciones_admin()

                while funciones_admin != 5:

                  if funciones_admin == 1 and len(lista_salas) > 0:
                      # GESTIONAR CARTELERA --- QUITAR PELICULA FINALIZADO ---- AGREGAR PELICULA FINALIZADO
                      gestionar_cartelera = funcion_gestionar_cartelera() 
                      while gestionar_cartelera != 3:
                          if gestionar_cartelera == 1 and len(lista_sala_asignada) != len(lista_id_sala): # AGREGAR PELICULA SI Y SOLO SI HAY SALAS DISPONIBLES
                              print("Agregar pelicula")
                              nombre_pelicula , asignar_sala = hola.agrega_pelicula(lista_salas, lista_id_sala, lista_sala_asignada)
                              lista_peliculas.append(nombre_pelicula)
                              lista_sala_asignada.append(asignar_sala)

                              # Verificacion de listas
                              print("Lista de peliculas", lista_peliculas)
                              print("Lista de salas ocupadas",lista_sala_asignada)
                              print("Lista id sala", lista_id_sala)

                          elif gestionar_cartelera == 2 and len(lista_peliculas) != 0: # QUITAR PELICULA SI Y SOLO SI HAY PELICULAS OCUPANDO SALAS
                              print("Quitar pelicula")
                              imprimir_lista_enumerada(lista_peliculas)
                              pelicula_a_eliminar = input("Ingrese el nombre de la pelicula a quitar: ")
                              if pelicula_a_eliminar in lista_peliculas:
                                  lista_sala_asignada.remove(lista_sala_asignada[lista_peliculas.index(pelicula_a_eliminar)])
                                  lista_peliculas.remove(pelicula_a_eliminar)
                              else:
                                  print("La pelicula no se encuentra en la cartelera.")
                          else:
                              if len(lista_sala_asignada) == len(lista_id_sala):
                                  print("Todas las salas estan ocupadas.")
                              if len(lista_peliculas) == 0:
                                  print("No hay peliculas en la cartelera.")
                          gestionar_cartelera = funcion_gestionar_cartelera()

                  elif funciones_admin == 2:
                      # CAMBIAR PRECIO DE ENTRADAS --- ESTA FINALIZADA
                      print("Cambiar precio de entrada")
                      print(f"Precio actual {precio_entrada}")
                      precio_entrada = verificar_entero()
                      print(f"Se actualizo el precio a {precio_entrada}")

                  elif funciones_admin == 3:
                      # CREAR SALA DE CINE --- ESTA FINALIZADA
                      print("crear sala de cine")
                      print("\nIngrese la cantidad de filas.")
                      filas = verificar_entero()
                      print("\nIngrese la cantidad de columnas.")
                      columnas = verificar_entero()
                      lista_salas.append(salas.crear_sala(filas, columnas))
                      lista_id_sala.append(crear_id(lista_id_sala))
                      
                      print("\nCantidad de salas:", len(lista_salas))
                      for index, sala in enumerate(lista_salas):
                          print("-"*30)
                          print("Sala N°", index+1, "--- ID", lista_id_sala[index])
                          salas.imprimir_sala(sala)
                          print("-"*30)

                  elif funciones_admin == 4:
                      # MOSTRAR ESTADISTICAS --- WIP
                      print("Mostrar estadisticas")

                  else:
                      if len(lista_salas) == 0:
                          print("\nNo hay salas creadas.")
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

                    elif funciones_usuario == 2:
                        # COMPRAR ENTRADAS
                        print("Comprar entradas")

                    elif funciones_usuario == 3:
                        # CONSULTAR RESERVAS
                        print("Consultar reservas")

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