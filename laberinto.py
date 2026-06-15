# Problema 1 - Evaluacion T3
import time

# Matriz del laberinto 9x9
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

# Movimientos en orden: abajo, derecha, arriba, izquierda
DIRECCIONES = [
    (1, 0, "Abajo"),
    (0, 1, "Derecha"),
    (-1, 0, "Arriba"),
    (0, -1, "Izquierda")
]

# Variables globales
paso_nro = 0
camino_solucion = []
visitados = set()

def mostrar_laberinto(matriz):
    # Imprimir laberinto
    for fila in matriz:
        print("  ".join(f"{str(celda):>2}" for celda in fila))
    print()

def resolver_backtracking(f, c, vidas):
    global paso_nro
    
    # Limites de la matriz
    if f < 0 or f >= 9 or c < 0 or c >= 9:
        return False
        
    # Si es pared
    if laberinto[f][c] == 0:
        return False
        
    # Si ya fue visitado
    if (f, c) in visitados:
        return False
        
    # Costo de vidas
    valor_celda = laberinto[f][c]
    costo = 0
    if valor_celda == -1:
        costo = 1
    elif valor_celda == -2:
        costo = 2
        
    vidas_restantes = vidas - costo
    
    paso_nro += 1
    print(f"Paso {paso_nro}: Entrando a ({f}, {c}) con valor {valor_celda} | Vidas: {vidas_restantes}")
    
    # Si se queda sin vidas
    if vidas_restantes <= 0:
        print(f"  -> [Inviable] El raton se quedo sin vidas en ({f}, {c}). Retrocediendo...")
        return False
        
    # Guardar en camino y visitados
    visitados.add((f, c))
    camino_solucion.append((f, c))
    
    # Llegada a la meta
    if f == 0 and c == 0:
        print(f"\nExito! Se llego a la salida (F) en ({f}, {c}) con {vidas_restantes} vidas.")
        return True
        
    # Buscar en las 4 direcciones
    for df, dc, dir_nombre in DIRECCIONES:
        sig_f = f + df
        sig_c = c + dc
        
        # Imprimir intento
        print(f"  -> Intentando mover a {dir_nombre} desde ({f}, {c}) a ({sig_f}, {sig_c})")
        
        if resolver_backtracking(sig_f, sig_c, vidas_restantes):
            return True
            
    # Deshacer camino si no sirve
    print(f"  -> [Retroceso] No hay movimientos viables desde ({f}, {c}). Retrocediendo...")
    visitados.remove((f, c))
    camino_solucion.pop()
    return False

def main():
    print("================ LABERINTO ORIGINAL ================")
    mostrar_laberinto(laberinto)
    print("====================================================\n")
    
    print("Iniciando la busqueda del camino...")
    # Inicia en 8 0 con 3 vidas
    exito = resolver_backtracking(8, 0, 3)
    
    print("\n===================== RESULTADO =====================")
    if exito:
        print("RESULTADO: El raton logro salir del laberinto!")
        print(f"Camino tomado: {camino_solucion}\n")
        
        # Marcar camino con X
        matriz_solucion = [fila[:] for fila in laberinto]
        for f, c in camino_solucion:
            if matriz_solucion[f][c] not in ['I', 'F']:
                matriz_solucion[f][c] = 'X'
                
        print("Matriz que indica el camino para salir:")
        mostrar_laberinto(matriz_solucion)
    else:
        print("RESULTADO: No fue posible salir del laberinto.")
    print("=====================================================")

if __name__ == "__main__":
    main()
