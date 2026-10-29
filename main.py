import random
import salas
from functools import reduce

# Modulo cartelera
def agrega_pelicula(lista_salas, lista_id_sala, lista_sala_asignada):
    """
    Agrega una pelicula a la cartelera.
    Y le asigna una sala de cine.

    Esta función se puede acceder desde el menú de administrador.
    """
    nombre_pelicula = input("\nIngrese el nombre de la pelicula a agregar: ")
    consultar_tamaño_sala(lista_salas, lista_id_sala)
    asignar_sala = verificar_entero()
    while asignar_sala <= 0 or asignar_sala > len(lista_salas):
        print("Error. Fuera de rango.")
        asignar_sala = verificar_entero()
    while lista_id_sala[asignar_sala-1] in lista_sala_asignada or asignar_sala > len(lista_id_sala):
        if lista_id_sala[asignar_sala-1] in lista_sala_asignada:
          print("\nLa sala ya tiene asignada una pelicula.")
          consultar_tamaño_sala(lista_salas, lista_id_sala)
          asignar_sala = verificar_entero()
        if asignar_sala > len(lista_id_sala):
          print("\nLa sala no existe.")
          consultar_tamaño_sala(lista_salas, lista_id_sala)
          asignar_sala = verificar_entero()
    
    asignar_sala = lista_id_sala[asignar_sala-1]
    return nombre_pelicula , asignar_sala

def mostrar_cartelera(lista_peliculas, lista_sala_asignada):
    #muestra las entradas y sus precios junto con las entradas disponibles
    for i in range(len(lista_peliculas)):
        print ("Película: ", lista_peliculas[i] , "--- Sala ID --", lista_sala_asignada[i])


"""
------------------------------------- ↑↑↑ Termina modulo cartelera.py ↑↑↑ -----------------------------------------------------------
"""

def menu_principal():
    """
    Muestra el menú principal y devuelve la opción seleccionada.
    """
    print("""
    Bienvenido a ButacaPro!
    
    Seleccione una opción:
    1 - Crear usuario
    2 - Iniciar sesion
    3 - Salir
    """)
    opcion = verificar_entero()
    while opcion < 1 or opcion > 3:
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
    Consulta el tamaño de la sala de cine y su ID.
    ID de la sala: 1111
    1. Sala 1: 3 filas x 3 columnas
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

def registrar_usuario(lista_usuario):
    """
    Crea un usuario y contraseña
    """
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Cree una contraseña: ")
    while usuario in lista_usuario:
        print("\nNombre de usuario no disponible. Intente nuevamente.")
        usuario = input("Ingrese su nombre de usuario: ")
    return usuario , contraseña

def verificar_usuario_registrado(usuario , contraseña, lista_usuarios , lista_contraseña):
    """
    Verifica si el se encuentra registrado devolviendo TRUE o FALSE
    """
    if usuario in lista_usuarios:
        if lista_contraseña[lista_usuarios.index(usuario)] == contraseña:
            return True
        else:
            return False

def guardar_reserva(canti_entradas, lista_salas, sala_por_contar, usuario, elijo_pelicula):
    """
    Guarda las posiciones y la ID de la sala de la reserva en una lista.
    """
    reservas = []
    while canti_entradas != 0:
        salas.imprimir_sala(lista_salas[sala_por_contar])
        print("\nIngrese la fila: ")
        fila = verificar_entero()
        print("\nIngrese la columna: ")
        columna = verificar_entero()
        seleccion_de_asiento = salas.ocupar_butaca(lista_salas[sala_por_contar],fila,columna)
        while seleccion_de_asiento == False:
            salas.imprimir_sala(lista_salas[sala_por_contar])
            print("\nIngrese la fila: ")
            fila = verificar_entero()
            print("\nIngrese la columna: ")
            columna = verificar_entero()
            seleccion_de_asiento = salas.ocupar_butaca(lista_salas[sala_por_contar],fila,columna)

        posicion_reserva = (elijo_pelicula, fila, columna)
        reserva_usuario = (posicion_reserva, usuario)
        reservas.append(reserva_usuario)
        print("Se ocupo el asiento", "fila:",fila,"columna:",columna)
        canti_entradas -= 1
    return reservas
        
                            
    
"""
-------------------------------------- ↓↓↓ EMPIEZA EL PROGRAMA PRINCIPAL ↓↓↓ ----------------------------------------------------------------------
"""


def main():

    precio_entrada = 10000
    lista_peliculas = ["Pocoyo"]
    lista_salas = [[["L", "L", "L"], ["L", "L", "L"], ["L", "L", "L"]]]
    lista_usuarios = []
    lista_id_usuarios = []
    lista_contraseñas = []
    lista_sala_asignada = [1111]
    lista_id_sala = [1111]

    mapa_reservas = {}

    contraseña_admin = "admin"
    usuario = "admin"
    contraseña = ""
    verifico_registrado = True


    funciones_principal = menu_principal()
    while funciones_principal != 3:
        if funciones_principal == 1 or funciones_principal == 2:
            
            if funciones_principal == 1:
                usuario , contraseña = registrar_usuario(lista_usuarios)
                lista_usuarios.append(usuario)
                lista_id_usuarios.append(crear_id(lista_id_usuarios))
                lista_contraseñas.append(contraseña)
            elif funciones_principal == 2 and len(lista_usuarios)>0:
                usuario = input("Ingrese su nombre de usuario: ")
                contraseña = input("Ingrese su contraseña: ")
                verifico_registrado = verificar_usuario_registrado(usuario, contraseña, lista_usuarios , lista_contraseñas)


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
                              nombre_pelicula , asignar_sala = agrega_pelicula(lista_salas, lista_id_sala, lista_sala_asignada)
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
                      creo_sala = salas.crear_sala(filas, columnas)
                      lista_salas.append(creo_sala)
                      lista_id_sala.append(crear_id(lista_id_sala))
                      
                      print("\nCantidad actual de salas:", len(lista_salas))
                      print()
                      consultar_tamaño_sala(lista_salas , lista_id_sala)
                      salas.imprimir_sala(creo_sala)

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
            elif usuario != "admin" and verifico_registrado == True: # Llegas si el usuario no es admin y ingresas correctamente tu usuario y contraseña.
                """
                ---------------------------- ↓↓↓ EMPIEZA BLOQUE DE FUNCIONES DE USUARIO ↓↓↓ ---------------------------------------------------
                """

                print("\nBienvenido!", usuario)
                funciones_usuario = imprimir_funciones_usuario()


                while funciones_usuario != 4:
                    if funciones_usuario == 1 and len(lista_peliculas)>0:
                        # MOSTRAR CARTELERA
                        print("Mostrar cartelera")
                        mostrar_cartelera(lista_peliculas , lista_sala_asignada)

                    elif funciones_usuario == 2 and len(lista_peliculas)>0:
                        # COMPRAR ENTRADAS
                        print("Comprar entradas")
                        imprimir_lista_enumerada(lista_peliculas)
                        print(f"Ingrese un numero 1-{len(lista_peliculas)}.")
                        elijo_pelicula = verificar_entero()
                        print("Verifico sala", elijo_pelicula)
                        while elijo_pelicula <= 0 or elijo_pelicula > len(lista_peliculas):
                            print("Error. Fuera de rango.")
                            elijo_pelicula = verificar_entero()
                        print("Precio por entrada $", precio_entrada)
                        print("Ingrese la cantidad de entradas a comprar:")
                        canti_entradas = verificar_entero()
                        elijo_pelicula = lista_sala_asignada[elijo_pelicula-1]
                        print("Verifico sala", elijo_pelicula)
                        sala_por_contar = lista_id_sala.index(elijo_pelicula)
                        print(sala_por_contar)
                        libres_por_contar , ocupadas_por_contar = salas.contar_butacas(lista_salas[sala_por_contar])
                        print(libres_por_contar)
                        while canti_entradas <= 0 or canti_entradas > libres_por_contar:
                            print("Error. Intente nuevamente.")
                            print("Ingrese la cantidad de entradas a comprar: ")
                            canti_entradas = verificar_entero()
                        
                        reservas = dict(guardar_reserva(canti_entradas, lista_salas, sala_por_contar, usuario, elijo_pelicula))
                        mapa_reservas.update(reservas)
                        

                        
                    elif funciones_usuario == 3:
                        # CONSULTAR RESERVAS
                        print(mapa_reservas)
                        print("Consultar reservas")

                        


                    else:
                        if funciones_usuario == 1:
                            print("\nNo hay peliculas en cartelera.")
                        else:
                            print("\nOpción inválida. Intente nuevamente.")
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