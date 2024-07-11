import tkinter as tk
from data.load_data import load_clients, load_vehicles, load_warehouse
from optimization.vrpb_solver import solve_vrpb
from gui.utils import show_map

class SolveVRPBWindow:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("Resolver VRPB")

        self.solve_button = tk.Button(self.top, text="Resolver VRPB", command=self.solve_vrpb)
        self.solve_button.pack(pady=10)

        self.result_label = tk.Label(self.top, text="")
        self.result_label.pack(pady=10)

    def solve_vrpb(self):
        clients = load_clients('data/vrpb_data/vrpb_clients.csv')
        vehicles = load_vehicles('data/vrpb_data/vrpb_vehicles.csv')
        warehouse = load_warehouse('data/vrpb_data/vrpb_warehouse.csv')

        vehicle_routes = solve_vrpb(clients, vehicles, warehouse)
        
        # Mostrar los resultados en un mapa y guardar en un archivo HTML específico para VRPB
        show_map(vehicle_routes, warehouse, filename='optimized_vrpb_route.html')
        self.result_label.config(text="VRPB Resuelto y mostrado en el mapa")
