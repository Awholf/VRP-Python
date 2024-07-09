# data/load_data.py

import pandas as pd
from models.client import Client
from models.vehicle import Vehicle
from models.warehouse import Warehouse

def load_clients(file_path):
    """
    Carga los datos de los clientes desde un archivo CSV.

    :param file_path: Ruta del archivo CSV.
    :return: Lista de objetos Client.
    """
    clients_df = pd.read_csv(file_path)
    clients = []
    for _, row in clients_df.iterrows():
        client = Client(
            id=row['id'],
            name=row['name'],
            address=row['address'],
            demand=row['demand'],
            location=(row['location_x'], row['location_y'])
        )
        clients.append(client)
    return clients

def load_vehicles(file_path):
    """
    Carga los datos de los vehículos desde un archivo CSV.

    :param file_path: Ruta del archivo CSV.
    :return: Lista de objetos Vehicle.
    """
    vehicles_df = pd.read_csv(file_path)
    vehicles = []
    for _, row in vehicles_df.iterrows():
        vehicle = Vehicle(
            id=row['id'],
            capacity=row['capacity']
        )
        vehicles.append(vehicle)
    return vehicles

def load_warehouse(file_path):
    """
    Carga los datos del almacén desde un archivo CSV.

    :param file_path: Ruta del archivo CSV.
    :return: Objeto Warehouse.
    """
    warehouse_df = pd.read_csv(file_path)
    row = warehouse_df.iloc[0]
    warehouse = Warehouse(
        id=row['id'],
        name=row['name'],
        location=(row['location_x'], row['location_y']),
        storage_capacity=row['storage_capacity']
    )
    return warehouse
