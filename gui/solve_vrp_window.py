# gui/solve_vrp_window.py

import tkinter as tk
from models.client import Client
from models.vehicle import Vehicle
from models.warehouse import Warehouse
from optimization.vrp_solver import solve_vrp
from gui.utils import show_map

class SolveVRPWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Solve VRP")

        self.solve_button = tk.Button(self.top, text="Solve VRP", command=self.solve_vrp)
        self.solve_button.pack(pady=10)

        self.result_label = tk.Label(self.top, text="")
        self.result_label.pack(pady=10)

    def solve_vrp(self):
        # Assuming clients, vehicles, and warehouse are loaded
        clients = [
            Client(id=1, name='Abraham', address='Los Olivos', demand=10, location=(-77.0485, -12.0156)),
            Client(id=2, name='Mateo', address='San Juan de Lurigancho', demand=15, location=(-76.9831, -12.0264)),
            Client(id=3, name='Julio', address='Chosica', demand=20, location=(-76.6987, -11.9372)),
            Client(id=4, name='Ramón', address='Lurín', demand=25, location=(-76.8497, -12.1615)),
            Client(id=5, name='Yulissa', address='Chancay', demand=30, location=(-77.2710, -11.5622))
        ]

        vehicles = [
            Vehicle(id=1, capacity=100),
            Vehicle(id=2, capacity=100),
            Vehicle(id=3, capacity=100),
            Vehicle(id=4, capacity=100),
            Vehicle(id=5, capacity=100)
        ]

        warehouse = Warehouse(id=1, name='Main Warehouse', location=(-77.0428, -12.0464), storage_capacity=1000)

        vehicle_routes = solve_vrp(clients, vehicles, warehouse)
        
        # Show results on a map
        show_map(vehicle_routes, warehouse)
        self.result_label.config(text="VRP Solved and displayed on the map")
