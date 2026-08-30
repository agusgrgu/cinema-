def crear_sala(filas, columnas):
    """crea una matriz para representar la sala
    las butacas comienzan en forma de "L" (libre) y
    Devuelve la matriz creada"""
    sala = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("L")
        sala.append(fila)
    return sala
    
def imprimir_sala(sala):
    """recibe la matriz de la sala y la muestra en pantalla
    ordenada en filas y columnas"""
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            print(sala[i][j], end=" ")
        print()
        
def verificar_butaca(sala, fila, columna):
    """comprueba que la fila y columna ingresadas existan dentro
    de los limites de la sala y que la butaca este "L" (libre)
    devuelve True si está disponible o False si no existe o está ocupada"""
    if fila >= 0 and fila < len(sala) and columna >= 0 and columna < len(sala[0]):
        if sala[fila][columna] == "L":
            return True
        else:
            return False
    else:
        return False 

def ocupar_butaca(sala, fila, columna):
    """cambia el estado de una butaca a "O" (ocupada) si es que
    esta disponible se usa verificar_butaca() para validarlo
    devuelve True si se pudo reservar o False si falló."""
    if verificar_butaca(sala, fila, columna) == True:
        sala[fila][columna] = "O"
        print("Reserva exitosa: La butaca ha sido ocupada.")
        return True 
    else:
        print("Error!: La butaca no existe o ya esta ocupada.")
        return False

def contar_butacas(sala):
    """recorre toda la sala y cuenta cuántas butacas estan "L" (libres)
    y cuántas están "O" (ocupadas)
    devuelve ambos totales para poder calcular estadisticas"""
    libres = 0
    ocupadas = 0
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            if sala[i][j] == "L":
                libres = libres + 1
            elif sala[i][j] == "O":
                ocupadas = ocupadas + 1
    return libres, ocupadas
