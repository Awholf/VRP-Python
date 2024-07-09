# optimization/utils.py
import math

def calculate_distance(point1, point2):
    """
    Calcula la distancia euclidiana entre dos puntos.
    :param point1: (tuple) Coordenadas del primer punto (x, y).
    :param point2: (tuple) Coordenadas del segundo punto (x, y).
    :return: (float) Distancia entre los dos puntos.
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_route_cost(route, distance_matrix):
    """
    Calcula el costo total de una ruta dada una matriz de distancias.
    :param route: (list) Lista de índices que representan la ruta.
    :param distance_matrix: (list of lists) Matriz de distancias entre todos los puntos.
    :return: (float) Costo total de la ruta.
    """
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i]][route[i + 1]]
    cost += distance_matrix[route[-1]][route[0]]  # Regresar al almacén
    return cost
