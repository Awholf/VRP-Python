# optimization/vrp_solver.py
import numpy as np
from models.vehicle import Vehicle
from models.client import Client
from models.warehouse import Warehouse
from optimization.utils import calculate_distance

def solve_vrp(clients, vehicles, warehouse):
    """
    Solves the vehicle routing problem using the Clarke and Wright Savings algorithm.

    :param Clients: List of Client objects.
    :param vehicles: List of Vehicle objects.
    :param warehouse: Warehouse object.
    :return: List of optimized routes for each vehicle.
    """
    # Create distance matrix
    locations = [warehouse.get_location()] + [client.get_location() for client in clients]
    distance_matrix = np.zeros((len(locations), len(locations)))
    
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:
                distance_matrix[i][j] = calculate_distance(locations[i], locations[j])
    
    # Initialize routes, each client in a separate route
    routes = [[i] for i in range(1, len(clients) + 1)]
    savings = []

    # Calculate savings
    for i in range(1, len(clients) + 1):
        for j in range(i + 1, len(clients) + 1):
            saving = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((saving, i, j))

    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    # Apply Clarke and Wright algorithm
    for saving, i, j in savings:
        route_i = None
        route_j = None
        for route in routes:
            if i in route:
                route_i = route
            if j in route:
                route_j = route
        if route_i and route_j and route_i != route_j:
            if route_i[0] == i or route_i[-1] == i:
                if route_j[0] == j or route_j[-1] == j:
                    new_route = route_i + route_j if route_i[-1] == i and route_j[0] == j else route_j + route_i
                    if len(new_route) <= vehicles[0].capacity:
                        routes.remove(route_i)
                        routes.remove(route_j)
                        routes.append(new_route)

    # Assign routes to vehicles
    vehicle_routes = []
    for route in routes:
        vehicle = vehicles.pop(0)
        vehicle.route = [clients[i - 1] for i in route]
        vehicle_routes.append(vehicle)
        if not vehicles:
            break

    return vehicle_routes
