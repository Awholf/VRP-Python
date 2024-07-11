import numpy as np
from models.vehicle import Vehicle
from models.client import Client
from models.warehouse import Warehouse
from optimization.utils import calculate_distance

def solve_vrpb(clients, vehicles, warehouse):
    """
    Solves the vehicle routing problem with backhauls using a modified Clarke and Wright Savings algorithm.

    :param clients: List of Client objects.
    :param vehicles: List of Vehicle objects.
    :param warehouse: Warehouse object.
    :return: List of optimized routes for each vehicle.
    """
    locations = [warehouse.get_location()] + [client.get_location() for client in clients]
    distance_matrix = np.zeros((len(locations), len(locations)))
    
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:
                distance_matrix[i][j] = calculate_distance(locations[i], locations[j])
    
    delivery_clients = [client for client in clients if client.type == 'delivery']
    pickup_clients = [client for client in clients if client.type == 'pickup']

    routes = [[i] for i in range(1, len(delivery_clients) + 1)]
    savings = []

    for i in range(1, len(delivery_clients) + 1):
        for j in range(i + 1, len(delivery_clients) + 1):
            saving = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((saving, i, j))

    savings.sort(reverse=True, key=lambda x: x[0])

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
                    total_demand = sum(delivery_clients[k - 1].demand for k in new_route)
                    if total_demand <= vehicles[0].capacity:
                        routes.remove(route_i)
                        routes.remove(route_j)
                        routes.append(new_route)

    vehicle_routes = []
    for route in routes:
        vehicle = vehicles.pop(0)
        vehicle.route = [delivery_clients[i - 1] for i in route]
        vehicle_routes.append(vehicle)
        if not vehicles:
            break

    for vehicle in vehicle_routes:
        for client in pickup_clients:
            if vehicle.add_client(client):
                pickup_clients.remove(client)

    return vehicle_routes
