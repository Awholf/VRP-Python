# models/vehicle.py

class Vehicle:
    def __init__(self, id, capacity):
        """
        Inicializa un nuevo vehículo.

        :param id: Identificador único del vehículo.
        :param capacity: Capacidad máxima del vehículo.
        """
        self.id = id
        self.capacity = capacity
        self.route = []

    def add_stop(self, client):
        """
        Añade una parada a la ruta del vehículo.

        :param client: Cliente a añadir a la ruta.
        """
        self.route.append(client)

    def current_load(self):
        """
        Calcula la carga actual del vehículo basada en las demandas de los clientes en la ruta.

        :return: La carga actual del vehículo.
        """
        return sum(client.demand for client in self.route)

    def __repr__(self):
        return f"Vehicle(id={self.id}, capacity={self.capacity}, current_load={self.current_load()}, route={self.route})"
