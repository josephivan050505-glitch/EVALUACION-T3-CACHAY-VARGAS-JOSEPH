# Evaluacion T3 - Analisis de Algoritmos y Estrategias de Programacion
# Problema 1: Laberinto del Raton con Backtracking y Vidas

import time

# Representacion del laberinto 9x9 original
# 'I' es el inicio (esquina inferior izquierda)
# 'F' es el fin (esquina superior izquierda)
# 0 son paredes (celdas grises en el grafico)
# 1 son celdas normales
# -1 resta 1 vida
# -2 resta 2 vidas
laberinto = [
    ['F',  1,  1,  1,  0,  1,  1,  1,  1],
    [-2,   0,  0, -1,  0,  1,  0,  1,  0],
    [ 1,   1,  0,  1,  1,  1,  0,  1,  0],
    [ 0,   1,  0, -1,  0,  0,  0, -1,  0],
    [ 1,   1,  1,  1,  1,  1,  1,  1,  0],
    [-1,   0,  0,  0,  0,  0,  0,  1,  1],
    [ 1,   1,  1,  1, -1,  1,  1,  1,  0],
    [ 1,   0,  0,  1,  0,  1,  0,  1,  0],
    ['I',  1, -1,  1,  1,  1,  0,  1,  1]
]

# Direcciones en el orden solicitado: abajo, derecha, arriba, izquierda
DIRECCIONES = [
    (1, 0, "Abajo"),
    (0, 1, "Derecha"),
    (-1, 0, "Arriba"),
    (0, -1, "Izquierda")
]

# Variables globales para el seguimiento
paso_nro = 0
camino_solucion = []
visitados = set()

def mostrar_laberinto(matriz):
    # Imprime el laberinto de forma legible
    for fila in matriz:
        print("  ".join(f"{str(celda):>2}" for celda in fila))
    print()

def resolver_backtracking(f, c, vidas):
    global paso_nro
    
    # Validar limites del laberinto
    if f < 0 or f >= 9 or c < 0 or c >= 9:
        return False
        
    # Validar si es una pared (0)
    if laberinto[f][c] == 0:
        return False
        
    # Validar si ya fue visitado en el camino actual
    if (f, c) in visitados:
        return False
        
    # Calcular el costo de vidas al pisar la celda
    valor_celda = laberinto[f][c]
    costo = 0
    if valor_celda == -1:
        costo = 1
    elif valor_celda == -2:
        costo = 2
        
    vidas_restantes = vidas - costo
    
    paso_nro += 1
    print(f"Paso {paso_nro}: Entrando a ({f}, {c}) con valor {valor_celda} | Vidas restantes: {vidas_restantes}")
    
    # Si las vidas llegan a cero o menos, el camino es inviable
    if vidas_restantes <= 0:
        print(f"  -> [Inviable] El raton perdio todas sus vidas en ({f}, {c}). Retrocediendo...")
        return False
        
    # Registrar la celda como visitada y agregar al camino
    visitados.add((f, c))
    camino_solucion.append((f, c))
    
    # Si llegamos a la meta (F)
    if f == 0 and c == 0:
        print(f"\nExito! Se logro llegar a la salida (F) en la posicion ({f}, {c}) con {vidas_restantes} vidas.")
        return True
        
    # Intentar avanzar en las direcciones indicadas: abajo, derecha, arriba, izquierda
    for df, dc, dir_nombre in DIRECCIONES:
        sig_f = f + df
        sig_c = c + dc
        
        # Mostrar intento de movimiento
        print(f"  -> Intentando mover hacia {dir_nombre} desde ({f}, {c}) a ({sig_f}, {sig_c})")
        
        if resolver_backtracking(sig_f, sig_c, vidas_restantes):
            return True
            
    # Backtracking: si ninguna direccion fue viable, deshacer cambios
    print(f"  -> [Retroceso] No hay movimientos viables desde ({f}, {c}). Volviendo al paso anterior...")
    visitados.remove((f, c))
    camino_solucion.pop()
    return False

def main():
    print("================ LABERINTO ORIGINAL ================")
    mostrar_laberinto(laberinto)
    print("====================================================\n")
    
    print("Iniciando la busqueda del camino...")
    # El raton inicia en (8, 0) con 3 vidas
    exito = resolver_backtracking(8, 0, 3)
    
    print("\n===================== RESULTADO =====================")
    if exito:
        print("RESULTADO: El raton logro salir del laberinto!")
        print(f"Camino tomado: {camino_solucion}\n")
        
        # Crear la matriz solucion marcando el camino con 'X'
        matriz_solucion = [fila[:] for fila in laberinto]
        for f, c in camino_solucion:
            if matriz_solucion[f][c] not in ['I', 'F']:
                matriz_solucion[f][c] = 'X'
                
        print("Matriz que indica el camino para salir:")
        mostrar_laberinto(matriz_solucion)
    else:
        print("RESULTADO: No fue posible salir del laberinto de forma viable.")
    print("=====================================================")

if __name__ == "__main__":
    main()
