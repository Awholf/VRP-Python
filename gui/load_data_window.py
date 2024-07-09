# gui/load_data_window.py

import tkinter as tk
from tkinter import filedialog
from data.load_data import load_clients, load_vehicles, load_warehouse

class LoadDataWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Cargar Datos")

        self.client_data_button = tk.Button(self.top, text="Cargar Datos de Clientes", command=self.load_clients_data)
        self.client_data_button.pack(pady=10)

        self.vehicle_data_button = tk.Button(self.top, text="Cargar Datos de Vehículos", command=self.load_vehicles_data)
        self.vehicle_data_button.pack(pady=10)

        self.warehouse_data_button = tk.Button(self.top, text="Cargar Datos del Almacén", command=self.load_warehouse_data)
        self.warehouse_data_button.pack(pady=10)

        self.reload_button = tk.Button(self.top, text="Recargar Datos", command=self.reload_data)
        self.reload_button.pack(pady=10)

        self.clients = []
        self.vehicles = []
        self.warehouse = None

    def load_clients_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.clients = load_clients(file_path)
            tk.Label(self.top, text=f"Cargados {len(self.clients)} clientes").pack()

    def load_vehicles_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.vehicles = load_vehicles(file_path)
            tk.Label(self.top, text=f"Cargados {len(self.vehicles)} vehículos").pack()

    def load_warehouse_data(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.warehouse = load_warehouse(file_path)
            tk.Label(self.top, text="Datos del almacén cargados").pack()

    def reload_data(self):
        # Lógica para recargar datos
        self.clients = []
        self.vehicles = []
        self.warehouse = None
        tk.Label(self.top, text="Datos recargados").pack()
