import tkinter as tk
from tkinter import ttk
from data.load_data import load_clients, load_vehicles, load_warehouse
from optimization.vrpb_solver import solve_vrpb
from gui.utils import show_map
from tkinter import ttk, filedialog 
class SolveVRPBWindow:
    def __init__(self, root):
        self.top = tk.Toplevel(root)
        self.top.title("Resolver VRPB")

        self.clients_file_label = ttk.Label(self.top, text="Seleccionar archivo de Clientes")
        self.clients_file_label.pack(pady=5)
        self.clients_file_button = ttk.Button(self.top, text="Seleccionar Archivo", command=self.load_clients_file)
        self.clients_file_button.pack(pady=5)
        self.clients_file_path = ttk.Label(self.top, text="")
        self.clients_file_path.pack(pady=5)

        self.vehicles_file_label = ttk.Label(self.top, text="Seleccionar archivo de Vehículos")
        self.vehicles_file_label.pack(pady=5)
        self.vehicles_file_button = ttk.Button(self.top, text="Seleccionar Archivo", command=self.load_vehicles_file)
        self.vehicles_file_button.pack(pady=5)
        self.vehicles_file_path = ttk.Label(self.top, text="")
        self.vehicles_file_path.pack(pady=5)

        self.warehouse_file_label = ttk.Label(self.top, text="Seleccionar archivo de Almacén")
        self.warehouse_file_label.pack(pady=5)
        self.warehouse_file_button = ttk.Button(self.top, text="Seleccionar Archivo", command=self.load_warehouse_file)
        self.warehouse_file_button.pack(pady=5)
        self.warehouse_file_path = ttk.Label(self.top, text="")
        self.warehouse_file_path.pack(pady=5)

        self.solve_button = ttk.Button(self.top, text="Resolver VRPB", command=self.solve_vrpb)
        self.solve_button.pack(pady=10)

        self.result_label = ttk.Label(self.top, text="")
        self.result_label.pack(pady=10)

    def load_clients_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.clients_file_path.config(text=file_path)
            self.clients = load_clients(file_path)

    def load_vehicles_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.vehicles_file_path.config(text=file_path)
            self.vehicles = load_vehicles(file_path)

    def load_warehouse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.warehouse_file_path.config(text=file_path)
            self.warehouse = load_warehouse(file_path)

    def solve_vrpb(self):
        vehicle_routes = solve_vrpb(self.clients, self.vehicles, self.warehouse)
        show_map(vehicle_routes, self.warehouse, filename='optimized_vrpb_route.html')
        self.result_label.config(text="VRPB Resuelto y mostrado en el mapa")
