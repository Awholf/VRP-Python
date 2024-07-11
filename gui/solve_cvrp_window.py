import tkinter as tk
from data.load_data import load_clients, load_vehicles, load_warehouse
from optimization.cvrp_solver import solve_cvrp
from gui.utils import show_map

class SolveCVRPWindow:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("Resolver CVRP")

        self.solve_button = tk.Button(self.top, text="Resolver CVRP", command=self.solve_cvrp)
        self.solve_button.pack(pady=10)

        self.result_label = tk.Label(self.top, text="")
        self.result_label.pack(pady=10)

    def solve_cvrp(self):
        clients = load_clients('data/cvrp_clients.csv')
        vehicles = load_vehicles('data/cvrp_vehicles.csv')
        warehouse = load_warehouse('data/cvrp_warehouse.csv')

        vehicle_routes = solve_cvrp(clients, vehicles, warehouse)
        
        # Mostrar los resultados en un mapa y guardar en un archivo HTML específico para CVRP
        show_map(vehicle_routes, warehouse, filename='optimized_cvrp_route.html')
        self.result_label.config(text="CVRP Resuelto y mostrado en el mapa")
