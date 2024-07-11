import tkinter as tk
from gui.load_data_window import LoadDataWindow
from gui.solve_vrp_window import SolveVRPWindow
from gui.solve_cvrp_window import SolveCVRPWindow
from gui.solve_vrpb_window import SolveVRPBWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador de Problemas de Rutas de Vehículos")

        self.load_data_button = tk.Button(root, text="Cargar Datos", command=self.open_load_data_window)
        self.load_data_button.pack(pady=10)

        self.solve_vrp_button = tk.Button(root, text="Resolver VRP", command=self.open_solve_vrp_window)
        self.solve_vrp_button.pack(pady=10)

        self.solve_cvrp_button = tk.Button(root, text="Resolver CVRP", command=self.open_solve_cvrp_window)
        self.solve_cvrp_button.pack(pady=10)

        self.solve_vrpb_button = tk.Button(root, text="Resolver VRPB", command=self.open_solve_vrpb_window)
        self.solve_vrpb_button.pack(pady=10)

    def open_load_data_window(self):
        LoadDataWindow(self.root)

    def open_solve_vrp_window(self):
        SolveVRPWindow(self.root)

    def open_solve_cvrp_window(self):
        SolveCVRPWindow(self.root)

    def open_solve_vrpb_window(self):
        SolveVRPBWindow(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()
