import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from gui.load_data_window import LoadDataWindow
from gui.solve_vrp_window import SolveVRPWindow
from gui.solve_cvrp_window import SolveCVRPWindow
from gui.solve_vrpb_window import SolveVRPBWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Solucionador de Problemas de Rutas de Vehículos")

        # Crear un estilo para la GUI
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        style.configure("TLabel", padding=6, background="#f0f0f0")
        style.configure("TNotebook", padding=6)
        style.configure("TNotebook.Tab", padding=6)

        # Crear el notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill='both')

        # Crear los frames para cada pestaña
        self.frame_load_data = ttk.Frame(self.notebook)
        self.frame_vrp = ttk.Frame(self.notebook)
        self.frame_cvrp = ttk.Frame(self.notebook)
        self.frame_vrpb = ttk.Frame(self.notebook)

        self.frame_load_data.pack(fill="both", expand=True)
        self.frame_vrp.pack(fill="both", expand=True)
        self.frame_cvrp.pack(fill="both", expand=True)
        self.frame_vrpb.pack(fill="both", expand=True)

        # Añadir frames al notebook
        self.notebook.add(self.frame_load_data, text="Cargar Datos")
        self.notebook.add(self.frame_vrp, text="Resolver VRP")
        self.notebook.add(self.frame_cvrp, text="Resolver CVRP")
        self.notebook.add(self.frame_vrpb, text="Resolver VRPB")

        # Cargar Datos
        self.load_data_label = ttk.Label(self.frame_load_data, text="Cargar Datos desde archivos CSV")
        self.load_data_label.pack(pady=10)
        self.load_data_button = ttk.Button(self.frame_load_data, text="Cargar Datos", command=self.open_load_data_window)
        self.load_data_button.pack(pady=10)

        # Añadir la imagen debajo del botón de cargar datos
        self.background_image = Image.open("data/logo.jpg")
        self.background_image = self.background_image.resize((400, 280), Image.ANTIALIAS)  # Redimensionar la imagen
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.image_label = ttk.Label(self.frame_load_data, image=self.background_photo)
        self.image_label.pack(pady=10)

        # Resolver VRP
        self.solve_vrp_label = ttk.Label(self.frame_vrp, text="Resolver el Problema de Rutas de Vehículos (VRP)")
        self.solve_vrp_label.pack(pady=10)
        self.solve_vrp_button = ttk.Button(self.frame_vrp, text="Resolver VRP", command=self.open_solve_vrp_window)
        self.solve_vrp_button.pack(pady=10)

        # Resolver CVRP
        self.solve_cvrp_label = ttk.Label(self.frame_cvrp, text="Resolver el Problema de Rutas de Vehículos con Capacidad (CVRP)")
        self.solve_cvrp_label.pack(pady=10)
        self.solve_cvrp_button = ttk.Button(self.frame_cvrp, text="Resolver CVRP", command=self.open_solve_cvrp_window)
        self.solve_cvrp_button.pack(pady=10)

        # Resolver VRPB
        self.solve_vrpb_label = ttk.Label(self.frame_vrpb, text="Resolver el Problema de Rutas de Vehículos con Recolecciones (VRPB)")
        self.solve_vrpb_label.pack(pady=10)
        self.solve_vrpb_button = ttk.Button(self.frame_vrpb, text="Resolver VRPB", command=self.open_solve_vrpb_window)
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
