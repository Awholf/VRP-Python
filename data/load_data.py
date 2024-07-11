import pandas as pd
from models.client import Client
from models.vehicle import Vehicle
from models.warehouse import Warehouse

def load_clients(file_path):
    clients_df = pd.read_csv(file_path)
    clients = []
    type_exists = 'type' in clients_df.columns  # Verificar si el campo 'type' existe en el CSV

    for _, row in clients_df.iterrows():
        client = Client(
            id=row['id'],
            name=row['name'],
            address=row['address'],
            demand=row['demand'],
            type=row['type'] if type_exists else 'delivery',  # Usar 'delivery' si 'type' no está en el CSV
            location=(row['location_y'], row['location_x'])
        )
        clients.append(client)
    return clients

def load_vehicles(file_path):
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
    warehouse_df = pd.read_csv(file_path)
    row = warehouse_df.iloc[0]
    warehouse = Warehouse(
        id=row['id'],
        name=row['name'],
        location=(row['location_y'], row['location_x']),
        storage_capacity=row['storage_capacity']
    )
    return warehouse
