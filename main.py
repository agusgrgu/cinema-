import re
import random
import salas

"""
=====================================================================
  VALIDACIONES (expresiones regulares)
=====================================================================
"""

def es_usuario_valido(usuario):
    """Solo letras y numeros, sin espacios."""
    return re.match(r'^[a-zA-Z0-9]+$', usuario) is not None

def es_telefono_valido(telefono):
    """Formato 00-0000-0000."""
    return re.match(r'^[0-9]{2}-[0-9]{4}-[0-9]{4}$', telefono) is not None

def es_horario_valido(horario):
    """Formato HH:MM (00:00 a 23:59)."""
    return re.match(r'^([01][0-9]|2[0-3]):[0-5][0-9]$', horario) is not None

def es_contraseña_valida(contraseña):
    """
    Minimo 4 caracteres y solo letras o numeros.
    filter deja los caracteres alfanumericos: si queda la misma cantidad, es valida.
    """
    alfanumericos = tuple(filter(lambda c: c.isalnum(), contraseña))
    return len(contraseña) >= 4 and len(alfanumericos) == len(contraseña)

"""
=====================================================================
  ENTRADA DE DATOS
=====================================================================
"""

def verificar_entero(mensaje="Ingrese su opcion: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def pedir_opcion(minimo, maximo, mensaje="Ingrese su opcion: "):
    """
    Pide un entero dentro del rango [minimo, maximo].
    """
    opcion = verificar_entero(mensaje)
    while opcion < minimo or opcion > maximo:
        print("Opción inválida. Intente nuevamente.")
        opcion = verificar_entero(mensaje)
    return opcion


def pedir_texto(mensaje):
    """
    Pide un texto obligatorio (no vacio).
    """
    texto = input(mensaje).strip()
    while texto == "":
        print("Error: el dato es obligatorio.")
        texto = input(mensaje).strip()
    return texto


def pedir_usuario_nuevo(lista_usuarios):
    """
    Pide un nombre de usuario que cumpla con es_usuario_valido y que no este en uso.
    """
    while True:
        usuario = pedir_texto("Ingrese su nombre de usuario: ")
        if not es_usuario_valido(usuario):
            print("Error: El nombre de usuario solo puede contener letras y números.")
        elif usuario == "admin":
            print("Error: ese nombre está reservado.")
        elif usuario in lista_usuarios:
            print("\nNombre de usuario no disponible. Intente nuevamente.")
        else:
            return usuario


def pedir_contraseña_nueva(mensaje):
    """
    Pide una contraseña que cumpla es_contraseña_valida.
    """
    contraseña = input(mensaje)
    while not es_contraseña_valida(contraseña):
        print("Error: mínimo 4 caracteres, solo letras y números.")
        contraseña = input(mensaje)
    return contraseña


def pedir_telefono_nuevo(lista_telefonos):
    """
    Pide un telefono con es_telefono_valido y que no este registrado.
    """
    while True:
        telefono = input("Ingrese su teléfono (formato 00-0000-0000): ").strip()
        if not es_telefono_valido(telefono):
            print("Error: El teléfono debe tener el formato 00-0000-0000.")
        elif telefono in lista_telefonos:
            print("El número de teléfono ya está registrado.")
        else:
            return telefono


def pedir_horario(numero, horarios_cargados):
    """
    Pide un horario que cumpla con es_horario_valido y no este repetido.
    """
    while True:
        horario = input(f"Horario {numero}: ").strip()
        if not es_horario_valido(horario):
            print("Error: el horario debe tener el formato 00:00 (ej: 14:30).")
        elif horario in horarios_cargados:
            print("Error: ese horario ya fue ingresado.")
        else:
            return horario
 
 
def pedir_horarios():
    """
    Pregunta cuantos horarios habra y luego pide esa cantidad de horarios.
    Devuelve la lista de horarios ordenada.
    """
    cantidad = pedir_opcion(1, 10, "\n¿Cuántos horarios tendrá la película? (1-10): ")
    horarios = []
    for i in range(cantidad):
        horarios.append(pedir_horario(i + 1, horarios))
    return sorted(horarios)

"""
=====================================================================
  MENUS
=====================================================================
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
    return pedir_opcion(1, 3)


def imprimir_funciones_admin():
    """
    Imprime las funciones disponibles para el administrador y devuelve la elegida.

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
    return pedir_opcion(1, 5)


def imprimir_funciones_usuario():
    """
    Imprime las funciones disponibles para el usuario y devuelve la elegida.
    """
    print("""
    Funciones disponibles:
    1 - Mostar cartelera
    2 - Comprar entradas
    3 - Consultar reservas
    4 - Salir
    """)
    return pedir_opcion(1, 4)


def funcion_gestionar_cartelera():
    """
    Menu de gestion de cartelera. Se accede desde el menú de administrador.
    """
    print("""
    1 - Agregar pelicula 
    2 - Quitar pelicula
    3 - Volver
    """)
    return pedir_opcion(1, 3)

"""
=====================================================================
  FUNCIONES AUXILIARES
=====================================================================
"""
def crear_id(lista_id):
    """
    Crea un ID de 4 digitos unico para agregar a una lista paralela
    """
    nuevo_id = random.randint(1000, 9999)
    while nuevo_id in lista_id:
        nuevo_id = random.randint(1000, 9999)
    return nuevo_id


def imprimir_lista_enumerada(lista):
    """
    Imprime una lista enumerada.
    """
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i]}")


def consultar_tamaño_sala(lista_salas, lista_id_sala):
    """
    Consulta el tamaño de la sala de cine y su ID.
    ID de la sala: 1111
    Sala 1: 3 filas x 3 columnas
    """
    for i in range(len(lista_salas)):
        print(f"ID de la sala: {lista_id_sala[i]}")
        print(f"Sala {i+1}: {len(lista_salas[i])} filas x {len(lista_salas[i][0])} columnas")
        print("-" * 30)

def salas_libres(lista_sala_asignada, lista_id_sala):
    """
    Devuelve TRUE si hay salas sin pelicula asignada, FALSE si todas estan ocupadas.
    ESTA FUNCION USA CONJUNTOS
    """
    return set(lista_id_sala) - set(lista_sala_asignada) != set()

"""
=====================================================================
  USUARIOS Y SESION
=====================================================================
"""
def verificar_usuario_registrado(usuario, contraseña, lista_usuarios, lista_contraseñas):
    """
    Verifica si el usuario se encuentra registrado devolviendo TRUE o FALSE
    """
    return usuario in lista_usuarios and lista_contraseñas[lista_usuarios.index(usuario)] == contraseña


def registrar_usuario(lista_usuarios, lista_id_usuarios, lista_contraseñas, lista_telefonos):
    """
    Crea un usuario, contraseña y telefono (validados). Devuelve el usuario.
    """
    usuario = pedir_usuario_nuevo(lista_usuarios)
    contraseña = pedir_contraseña_nueva("Cree una contraseña (mínimo 4, letras y números): ")
    telefono = pedir_telefono_nuevo(lista_telefonos)

    lista_usuarios.append(usuario)
    lista_id_usuarios.append(crear_id(lista_id_usuarios))
    lista_contraseñas.append(contraseña)
    lista_telefonos.append(telefono)
    print("\nUsuario registrado correctamente.")
    return usuario


def iniciar_sesion(lista_usuarios, lista_contraseñas, contraseña_admin):
    """
    Pide las credenciales. Devuelve (usuario, contraseña_admin):
    usuario es el nombre si son correctas ("admin" para el administrador) o None si no.
    En el primer ingreso del admin se le pide crear su contraseña.
    """
    usuario = input("Ingrese su nombre de usuario: ").strip()

    if usuario == "admin" and contraseña_admin is None:
        print("Primer ingreso de administrador.")
        contraseña_admin = pedir_contraseña_nueva("Cree una contraseña para administradores: ")
        return "admin", contraseña_admin

    contraseña = input("Ingrese su contraseña: ")
    if usuario == "admin":
        if contraseña == contraseña_admin:
            return "admin", contraseña_admin
        return None, contraseña_admin

    if verificar_usuario_registrado(usuario, contraseña, lista_usuarios, lista_contraseñas):
        return usuario, contraseña_admin
    return None, contraseña_admin

"""
=====================================================================
  CARTELERA
=====================================================================
"""

def elegir_sala_libre(lista_salas, lista_id_sala, lista_sala_asignada):
    """
    Muestra las salas y devuelve el ID de una sala sin pelicula asignada.
    """
    consultar_tamaño_sala(lista_salas, lista_id_sala)
    opcion = pedir_opcion(1, len(lista_id_sala), "Ingrese el número de sala: ")
    while lista_id_sala[opcion - 1] in lista_sala_asignada:
        print("\nLa sala ya tiene asignada una pelicula.")
        consultar_tamaño_sala(lista_salas, lista_id_sala)
        opcion = pedir_opcion(1, len(lista_id_sala), "Ingrese el número de sala: ")
    return lista_id_sala[opcion - 1]


def agrega_pelicula(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios):
    """
    Agrega una pelicula a la cartelera.
    Y le asigna una sala de cine.

    Esta función se puede acceder desde el menú de administrador.
    """
    nombre_pelicula = pedir_texto("\nIngrese el nombre de la pelicula a agregar: ")
    if nombre_pelicula in lista_peliculas:
        print("Esa pelicula ya esta en la cartelera.")
        return
    sala_asignada = elegir_sala_libre(lista_salas, lista_id_sala, lista_sala_asignada)
    horarios = pedir_horarios()
    lista_peliculas.append(nombre_pelicula)
    lista_sala_asignada.append(sala_asignada)
    lista_horarios.append(horarios)
    print(f"\nPelicula '{nombre_pelicula}' agregada en la sala {sala_asignada}.")


def quitar_pelicula(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, mapa_reservas, lista_horarios):
    """
    Quita una pelicula de la cartelera, libera su sala y cancela sus reservas.
    """
    imprimir_lista_enumerada(lista_peliculas)
    pelicula_a_eliminar = input("Ingrese el nombre de la pelicula a quitar: ").strip()
    if pelicula_a_eliminar not in lista_peliculas:
        print("La pelicula no se encuentra en la cartelera.")
        return

    posicion = lista_peliculas.index(pelicula_a_eliminar)
    id_sala = lista_sala_asignada.pop(posicion)
    lista_horarios.pop(posicion)
    lista_peliculas.pop(posicion)

    # Las reservas de la pelicula se cancelan y la sala vuelve a quedar libre
    for clave in list(filter(lambda r: r[0] == id_sala, mapa_reservas)):
        del mapa_reservas[clave]
    print(f"\nPelicula '{pelicula_a_eliminar}' eliminada de la cartelera.")


def gestionar_cartelera(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios ,mapa_reservas):
    """
    Gestiona la cartelera del cine.

    Esta función se puede acceder desde el menú de administrador.
    """
    gestion = funcion_gestionar_cartelera()
    while gestion != 3:
        if gestion == 1 and salas_libres(lista_sala_asignada , lista_id_sala):
            agrega_pelicula(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios)
        elif gestion == 2 and len(lista_peliculas) != 0:
            quitar_pelicula(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, mapa_reservas, lista_horarios)
        else:
            if gestion == 1:
                print("\nTodas las salas estan ocupadas.")
            else:
                print("\nNo hay peliculas en la cartelera.")
        gestion = funcion_gestionar_cartelera()


def mostrar_cartelera(lista_peliculas, lista_sala_asignada, lista_horarios, precio_entrada):
    """
    Muestra las peliculas con su sala y el precio de entrada.
    """
    print(f"\nPrecio de entrada: ${precio_entrada}")
    for i in range(len(lista_peliculas)):
        print("Película: ", lista_peliculas[i], "--- Sala ID --", lista_sala_asignada[i], "--- Horarios --", ", ".join(lista_horarios[i]))

"""
=====================================================================
  FUNCIONES DE ADMIN
=====================================================================
"""

def cambiar_precio(precio_entrada):
    """
    Cambia el precio de entrada (compartido por todas las peliculas). Devuelve el nuevo precio.
    """
    print(f"Precio actual {precio_entrada}")
    nuevo_precio = verificar_entero("Ingrese el nuevo precio: ")
    while nuevo_precio <= 0:
        print("Error: el precio debe ser mayor a 0.")
        nuevo_precio = verificar_entero("Ingrese el nuevo precio: ")
    print(f"Se actualizo el precio a {nuevo_precio}")
    return nuevo_precio


def crear_sala_cine(lista_salas, lista_id_sala):
    """
    Crea una sala nueva con la cantidad de filas y columnas indicada.
    """
    print("\nIngrese la cantidad de filas.")
    filas = pedir_opcion(1, 20, "Filas (1-20): ")
    print("\nIngrese la cantidad de columnas.")
    columnas = pedir_opcion(1, 20, "Columnas (1-20): ")
    nueva_sala = salas.crear_sala(filas, columnas)
    lista_salas.append(nueva_sala)
    lista_id_sala.append(crear_id(lista_id_sala))

    print("\nCantidad actual de salas:", len(lista_salas))
    print()
    consultar_tamaño_sala(lista_salas, lista_id_sala)
    salas.imprimir_sala(nueva_sala)

def dividir_seguro(numerador, denominador):
    """
    Divide dos numeros. Si el denominador es 0 devuelve 0.0 en lugar de fallar
    """
    try:
        return numerador / denominador
    except ZeroDivisionError:
        return 0.0
 
 
def entradas_de_sala(mapa_reservas, id_sala):
    """
    Cantidad de entradas vendidas para una sala (todos sus horarios).
    """
    return len(list(filter(lambda clave: clave[0] == id_sala, mapa_reservas)))
 
 
def capacidad_pelicula(lista_salas, lista_id_sala, id_sala, horarios):
    """
    Cantidad total de butacas que se pueden vender para una pelicula:
    filas x columnas de su sala x cantidad de horarios.
    Si la sala no existe devuelve 0 y avisa.
    """
    try:
        sala = lista_salas[lista_id_sala.index(id_sala)]
    except ValueError:
        print(f"Aviso: no se encontro la sala {id_sala}.")
        return 0
    return len(sala) * len(sala[0]) * len(horarios)
 
 
def pelicula_mas_vendida(lista_peliculas, ventas):
    """
    Devuelve el nombre de la pelicula con mas entradas vendidas.
    Si no hay peliculas en cartelera, max() lanza ValueError y se devuelve None.
    """
    try:
        mejor_venta, nombre = max(zip(ventas, lista_peliculas))
    except ValueError:
        return None
    return nombre if mejor_venta > 0 else None
 
 
def mostrar_estadisticas(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios, mapa_reservas, precio_entrada):
    """
    Muestra estadisticas de ventas y ocupacion a partir de mapa_reservas.
    """
    total_entradas = len(mapa_reservas)
    clientes = set(mapa_reservas.values())          # usuarios de las personas que compraron
    ventas = list(map(lambda id_sala: entradas_de_sala(mapa_reservas, id_sala), lista_sala_asignada))
 
    print("\n===== MODULO DE ESTADISTICAS =====")
    if total_entradas == 0:
        print("Todavia no hay ventas registradas.")
    print(f"Entradas vendidas: {total_entradas}")
    print(f"Recaudacion (a precio actual ${precio_entrada}): ${total_entradas * precio_entrada}")
    print(f"Clientes distintos: {len(clientes)}")
    print(f"Promedio de entradas por cliente: {dividir_seguro(total_entradas, len(clientes)):.2f}")
 
    print("\nOcupacion por pelicula:")
    peliculas_con_ventas = set()
    for i in range(len(lista_peliculas)):
        capacidad = capacidad_pelicula(lista_salas, lista_id_sala, lista_sala_asignada[i], lista_horarios[i])
        porcentaje = dividir_seguro(ventas[i], capacidad) * 100
        print(f"- {lista_peliculas[i]}: {ventas[i]} entradas de {capacidad} butacas ({porcentaje:.1f}%)")
        if ventas[i] > 0:
            peliculas_con_ventas.add(lista_peliculas[i])
 
    mas_vendida = pelicula_mas_vendida(lista_peliculas, ventas)
    if mas_vendida is None:
        print("\nNo hay una pelicula mas vendida todavia.")
    else:
        print(f"\nPelicula mas vendida: {mas_vendida}")
    sin_ventas = set(lista_peliculas) - peliculas_con_ventas
    if len(sin_ventas) > 0 and total_entradas > 0:
        print("Peliculas sin ventas:", ", ".join(sorted(sin_ventas)))


def sesion_admin(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios, mapa_reservas, precio_entrada):
    """
    Menu del administrador. Devuelve el precio de entrada (por si fue modificado).
    """
    print("\nBienvenido al menu de administradores")
    funciones_admin = imprimir_funciones_admin()
    while funciones_admin != 5:
        if funciones_admin == 1:
            gestionar_cartelera(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios, mapa_reservas)
        elif funciones_admin == 2:
            precio_entrada = cambiar_precio(precio_entrada)
        elif funciones_admin == 3:
            crear_sala_cine(lista_salas, lista_id_sala)
        else:
            mostrar_estadisticas(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios, mapa_reservas, precio_entrada)
        funciones_admin = imprimir_funciones_admin()
    return precio_entrada

"""
=====================================================================
  FUNCIONES DE USUARIO
=====================================================================
"""

def elegir_pelicula(lista_peliculas):
    """
    Muestra las peliculas y devuelve la posicion (desde 0) de la elegida.
    """
    imprimir_lista_enumerada(lista_peliculas)
    indice = pedir_opcion(1, len(lista_peliculas), f"Ingrese un numero 1-{len(lista_peliculas)}: ")
    return indice - 1

def elegir_horario(horarios):
    """
    Muestra los horarios de la pelicula y devuelve el elegido.
    """
    print("\nHorarios disponibles:")
    imprimir_lista_enumerada(horarios)
    opcion = pedir_opcion(1, len(horarios), f"Ingrese un horario 1-{len(horarios)}: ")
    return horarios[opcion - 1]
 
 
def armar_sala_horario(plantilla, id_sala, horario, mapa_reservas):
    """
    Devuelve la sala para una funcion (sala + horario): una sala nueva con
    las butacas ya reservadas para ese horario marcadas como ocupadas.
    """
    sala = salas.crear_sala(len(plantilla), len(plantilla[0]))
    reservas_funcion = filter(lambda clave: clave[0] == id_sala and clave[1] == horario, mapa_reservas)
    for _, _, fila, columna in reservas_funcion:
        sala[fila - 1][columna - 1] = "O"
    return sala

def pedir_butaca(sala):
    """
    Pide fila y columna (numeradas desde 1) hasta ocupar una butaca libre.
    Devuelve (fila, columna) tal como las ingreso el usuario.
    """
    while True:
        salas.imprimir_sala(sala)
        fila = verificar_entero("\nIngrese la fila (desde 1): ")
        columna = verificar_entero("Ingrese la columna (desde 1): ")
        if salas.ocupar_butaca(sala, fila - 1, columna - 1):
            return fila, columna


def guardar_reserva(canti_entradas, sala, usuario, id_sala, horario):
    """
    Pide las butacas y devuelve la lista de reservas [((id_sala, horario, fila, columna), usuario), ...]
    """
    reservas = []
    while canti_entradas != 0:
        fila, columna = pedir_butaca(sala)
        posicion_reserva = (id_sala, horario, fila, columna)
        reservas.append((posicion_reserva, usuario))
        print("Se ocupo el asiento", "fila:", fila, "columna:", columna)
        canti_entradas -= 1
    return reservas


def comprar_entradas(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada,
                     lista_horarios, precio_entrada, usuario, mapa_reservas):
    """
    Permite elegir pelicula, horario, cantidad y butacas. Guarda las reservas en mapa_reservas.
    """
    posicion = elegir_pelicula(lista_peliculas)
    id_sala = lista_sala_asignada[posicion]
    horario = elegir_horario(lista_horarios[posicion])
    plantilla = lista_salas[lista_id_sala.index(id_sala)]
    sala = armar_sala_horario(plantilla, id_sala, horario, mapa_reservas)
    libres, _ = salas.contar_butacas(sala)
    if libres == 0:
        print("\nLa funcion esta agotada.")
        return
 
    print(f"\nPrecio por entrada $ {precio_entrada} - Butacas libres: {libres}")
    cantidad = pedir_opcion(1, libres, f"Ingrese la cantidad de entradas a comprar (1-{libres}): ")
    reservas = dict(guardar_reserva(cantidad, sala, usuario, id_sala, horario))
    mapa_reservas.update(reservas)
    print(f"\nCompra exitosa. Total a pagar: $ {precio_entrada * cantidad}")


def consultar_reservas(lista_peliculas, lista_sala_asignada, mapa_reservas, usuario):
    """
    Muestra solo las reservas del usuario (se filtran por usuario).
    """
    propias = sorted(filter(lambda r: r[1] == usuario, mapa_reservas.items()))
    if len(propias) == 0:
        print("\nNo tenes reservas.")
        return
    print(f"\nReservas de {usuario}:")
    for (id_sala, horario, fila, columna), _ in propias:
        pelicula = lista_peliculas[lista_sala_asignada.index(id_sala)]
        print(f"- {pelicula} | Sala ID {id_sala} | {horario} | Fila {fila}, Columna {columna}")


def sesion_usuario(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios, mapa_reservas, precio_entrada, usuario):
    """
    Menu del usuario registrado.
    """
    print("\nBienvenido!", usuario)
    funciones_usuario = imprimir_funciones_usuario()
    while funciones_usuario != 4:
        if funciones_usuario == 3:
            consultar_reservas(lista_peliculas, lista_sala_asignada, mapa_reservas, usuario)
        elif len(lista_peliculas) == 0:
            print("\nNo hay peliculas en cartelera.")
        elif funciones_usuario == 1:
            mostrar_cartelera(lista_peliculas, lista_sala_asignada, lista_horarios, precio_entrada)
        else:
            comprar_entradas(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada,
                             lista_horarios, precio_entrada, usuario, mapa_reservas)
        funciones_usuario = imprimir_funciones_usuario()


"""
-------------------------------------- ↓↓↓ EMPIEZA EL PROGRAMA PRINCIPAL ↓↓↓ ----------------------------------------------------------------------
"""


def main():
                                                    # ↓↓↓ Tipo de dato que ocupa ↓↓↓
    precio_entrada = 10000                          # int: precio de entrada (igual para todas las peliculas)
    lista_peliculas = ["Pocoyo"]                    # string: nombre de cada pelicula en cartelera, mismo orden que lista_sala_asignada
    lista_salas = [salas.crear_sala(3, 3)]          # matriz: "L" = libre, "O" = ocupada, mismo orden que lista_id_sala
    lista_id_sala = [1111]                          # int: id de la sala, mismo orden que lista_salas
    lista_horarios = [["10:00", "14:00", "18:00"]]  # string: horarios de cada pelicula, mismo orden que lista_peliculas
    lista_sala_asignada = [1111]                    # int: id de la sala asignada a cada pelicula, mismo orden que lista_peliculas
    lista_usuarios = ["pepe"]                       # string: nombre de cada usuario registrado, mismo orden que lista_id_usuarios
    lista_id_usuarios = [1111]                      # int: id unico de cada usuario registrado, mismo orden que lista_usuarios
    lista_contraseñas = ["1234"]                    # string: contraseña de cada usuario registrado, mismo orden que lista_usuarios
    lista_telefonos = ["12-1234-1234"]              # string: numero de telefono de cada usuario registrado, mismo orden que lista_usuarios

    mapa_reservas = {(1111, "10:00", 1, 1): "pepe"} # dict: {(id_sala, horario, fila, columna): usuario} para guardar las reservas de butacas
    contraseña_admin = None                         # string: contraseña del administrador, None si no se creo aun

    funciones_principal = menu_principal()
    while funciones_principal != 3:
        if funciones_principal == 1:
            usuario = registrar_usuario(lista_usuarios, lista_id_usuarios, lista_contraseñas, lista_telefonos)
        else:
            usuario, contraseña_admin = iniciar_sesion(lista_usuarios, lista_contraseñas, contraseña_admin)

        if usuario == "admin":
            precio_entrada = sesion_admin(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios, mapa_reservas, precio_entrada)
        elif usuario is not None:
            sesion_usuario(lista_peliculas, lista_salas, lista_id_sala, lista_sala_asignada, lista_horarios, mapa_reservas, precio_entrada, usuario)
        else:
            print("\nUSUARIO O CONTRASEÑA INCORRECTOS. INTENTE NUEVAMENTE.")
        funciones_principal = menu_principal()

    print("Saliendo del sistema...")

main()