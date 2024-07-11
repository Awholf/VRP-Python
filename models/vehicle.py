class Vehicle:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.route = []
        self.current_load = 0

    def add_client(self, client):
        """
        Adds a client to the vehicle's route if it doesn't exceed the vehicle's capacity.

        :param client: Client object to be added.
        :return: True if the client was added, False otherwise.
        """
        if self.current_load + client.demand <= self.capacity:
            self.route.append(client)
            self.current_load += client.demand
            return True
        return False

    def get_location(self):
        return self.location
