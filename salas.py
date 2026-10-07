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