import tkinter as tk
from data.load_data import load_clients, load_vehicles, load_warehouse
from optimization.vrp_solver import solve_vrp
from gui.utils import show_map

class SolveVRPWindow:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("Resolver VRP")

        self.solve_button = tk.Button(self.top, text="Resolver VRP", command=self.solve_vrp)
        self.solve_button.pack(pady=10)

        self.result_label = tk.Label(self.top, text="")
        self.result_label.pack(pady=10)

    def solve_vrp(self):
        clients = load_clients('data/vrp_data/clients.csv')
        vehicles = load_vehicles('data/vrp_data/vehicles.csv')
        warehouse = load_warehouse('data/vrp_data/warehouse.csv')

        vehicle_routes = solve_vrp(clients, vehicles, warehouse)
        
        # Mostrar los resultados en un mapa y guardar en un archivo HTML específico para VRP
        show_map(vehicle_routes, warehouse, filename='optimized_vrp_route.html')
        self.result_label.config(text="VRP Resuelto y mostrado en el mapa")
