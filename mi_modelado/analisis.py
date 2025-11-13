# analisis.py
import random

def generar_matriz_elevaciones(filas=5, columnas=5, elev_min=100, elev_max=200):
    """
    Genera una matriz de elevaciones simulada (en metros).
    """
    matriz = []
    for _ in range(filas):
        fila = [round(random.uniform(elev_min, elev_max), 2) for _ in range(columnas)]
        matriz.append(fila)
    return matriz