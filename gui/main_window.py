# gui/main_window.py

import tkinter as tk
from gui.load_data_window import LoadDataWindow
from gui.solve_vrp_window import SolveVRPWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador de Problemas de Rutas de Vehículos")

        self.load_data_button = tk.Button(root, text="Cargar Datos", command=self.open_load_data_window)
        self.load_data_button.pack(pady=10)

        self.solve_vrp_button = tk.Button(root, text="Resolver VRP", command=self.open_solve_vrp_window)
        self.solve_vrp_button.pack(pady=10)

    def open_load_data_window(self):
        LoadDataWindow(self.root)

    def open_solve_vrp_window(self):
        SolveVRPWindow(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()
