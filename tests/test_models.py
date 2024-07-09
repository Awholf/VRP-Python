# tests/test_models.py

import unittest
from models.client import Client
from models.vehicle import Vehicle
from models.warehouse import Warehouse

class TestModels(unittest.TestCase):
    def test_client_creation(self):
        client = Client(id=1, name='Abraham', address='Los Olivos', demand=10, location=(-77.0485, -12.0156))
        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, 'Abraham')
        self.assertEqual(client.address, 'Los Olivos')
        self.assertEqual(client.demand, 10)
        self.assertEqual(client.location, (-77.0485, -12.0156))

    def test_vehicle_creation(self):
        vehicle = Vehicle(id=1, capacity=100)
        self.assertEqual(vehicle.id, 1)
        self.assertEqual(vehicle.capacity, 100)
        self.assertEqual(vehicle.route, [])

    def test_warehouse_creation(self):
        warehouse = Warehouse(id=1, name='Main Warehouse', location=(-77.0428, -12.0464), storage_capacity=1000)
        self.assertEqual(warehouse.id, 1)
        self.assertEqual(warehouse.name, 'Main Warehouse')
        self.assertEqual(warehouse.location, (-77.0428, -12.0464))
        self.assertEqual(warehouse.storage_capacity, 1000)
        self.assertEqual(warehouse.inventory, 0)

    def test_vehicle_add_stop(self):
        vehicle = Vehicle(id=1, capacity=100)
        client = Client(id=1, name='Abraham', address='Los Olivos', demand=10, location=(-77.0485, -12.0156))
        vehicle.add_stop(client)
        self.assertIn(client, vehicle.route)
        self.assertEqual(vehicle.current_load(), 10)

    def test_warehouse_inventory_management(self):
        warehouse = Warehouse(id=1, name='Main Warehouse', location=(-77.0428, -12.0464), storage_capacity=1000)
        warehouse.add_inventory(500)
        self.assertEqual(warehouse.inventory, 500)
        warehouse.remove_inventory(200)
        self.assertEqual(warehouse.inventory, 300)
        with self.assertRaises(ValueError):
            warehouse.remove_inventory(400)

if __name__ == '__main__':
    unittest.main()
