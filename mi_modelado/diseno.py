# diseno.py
import math

def calcular_pendientes(matriz, distancia_horizontal=10):
    """
    Calcula pendientes entre puntos adyacentes (N-S y E-O)
    Retorna una lista con todas las pendientes calculadas (%)
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    pendientes = []

    for i in range(filas):
        for j in range(columnas):
            # Pendiente hacia el Este
            if j < columnas - 1:
                delta_z = matriz[i][j+1] - matriz[i][j]
                pendiente = (delta_z / distancia_horizontal) * 100
                pendientes.append(pendiente)
            # Pendiente hacia el Sur
            if i < filas - 1:
                delta_z = matriz[i+1][j] - matriz[i][j]
                pendiente = (delta_z / distancia_horizontal) * 100
                pendientes.append(pendiente)
    
    return pendientes

def estadisticas_pendientes(pendientes):
    """
    Calcula pendiente máxima, mínima y promedio
    """
    if not pendientes:
        return 0, 0, 0
    max_p = round(max(pendientes), 2)
    min_p = round(min(pendientes), 2)
    prom_p = round(sum(pendientes)/len(pendientes), 2)
    return max_p, min_p, prom_p