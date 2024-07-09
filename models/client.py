# models/client.py

class Client:
    def __init__(self, id, name, address, demand, location):
        """
        Inicializa un nuevo cliente.

        :param id: Identificador único del cliente.
        :param name: Nombre del cliente.
        :param address: Dirección del cliente.
        :param demand: Demanda del cliente.
        :param location: Ubicación del cliente como una tupla (x, y).
        """
        self.id = id
        self.name = name
        self.address = address
        self.demand = demand
        self.location = location

    def get_location(self):
        """
        Obtiene la ubicación del cliente.

        :return: Una tupla (x, y) que representa la ubicación del cliente.
        """
        return self.location

    def __repr__(self):
        return f"Client(id={self.id}, name={self.name}, address={self.address}, demand={self.demand}, location={self.location})"
