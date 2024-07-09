# models/warehouse.py

class Warehouse:
    def __init__(self, id, name, location, storage_capacity):
        """
        Inicializa un nuevo almacén.

        :param id: Identificador único del almacén.
        :param name: Nombre del almacén.
        :param location: Ubicación del almacén como una tupla (x, y).
        :param storage_capacity: Capacidad de almacenamiento del almacén.
        """
        self.id = id
        self.name = name
        self.location = location
        self.storage_capacity = storage_capacity
        self.inventory = 0

    def add_inventory(self, amount):
        """
        Añade inventario al almacén.

        :param amount: Cantidad de inventario a añadir.
        """
        self.inventory += amount

    def remove_inventory(self, amount):
        """
        Elimina inventario del almacén.

        :param amount: Cantidad de inventario a eliminar.
        """
        if amount <= self.inventory:
            self.inventory -= amount
        else:
            raise ValueError("Not enough inventory to remove")

    def get_location(self):
        """
        Obtiene la ubicación del almacén.

        :return: Una tupla (x, y) que representa la ubicación del almacén.
        """
        return self.location

    def __repr__(self):
        return f"Warehouse(id={self.id}, name={self.name}, location={self.location}, storage_capacity={self.storage_capacity}, inventory={self.inventory})"
