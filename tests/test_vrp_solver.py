# tests/test_vrp_solver.py

# tests/test_vrp_solver.py

import unittest
from models.client import Client
from models.vehicle import Vehicle
from models.warehouse import Warehouse
from optimization.vrp_solver import resolver_vrp

class TestVRPSolver(unittest.TestCase):
    def setUp(self):
        # Configuración de datos de prueba
        self.clients = [
            Client(id=1, name='Abraham', address='Los Olivos', demand=10, location=(-77.0485, -12.0156)),
            Client(id=2, name='Mateo', address='San Juan de Lurigancho', demand=15, location=(-76.9831, -12.0264)),
            Client(id=3, name='Julio', address='Chosica', demand=20, location=(-76.6987, -11.9372)),
            Client(id=4, name='Ramón', address='Lurín', demand=25, location=(-76.8497, -12.1615)),
            Client(id=5, name='Yulissa', address='Chancay', demand=30, location=(-77.2710, -11.5622))
        ]
        self.vehicles = [
            Vehicle(id=1, capacity=100),
            Vehicle(id=2, capacity=100),
            Vehicle(id=3, capacity=100),
            Vehicle(id=4, capacity=100),
            Vehicle(id=5, capacity=100)
        ]
        self.warehouse = Warehouse(id=1, name='Main Warehouse', location=(-77.0428, -12.0464), storage_capacity=1000)

    def test_vrp_solution(self):
        # Prueba para verificar la solución VRP
        rutas_vehiculos = resolver_vrp(self.clients, self.vehicles, self.warehouse)
        self.assertIsInstance(rutas_vehiculos, list)
        self.assertTrue(all(isinstance(vehiculo, Vehicle) for vehiculo in rutas_vehiculos))
        total_demand = sum(cliente.demand for vehiculo in rutas_vehiculos for cliente in vehiculo.route)
        self.assertEqual(total_demand, sum(cliente.demand for cliente in self.clients))

if __name__ == '__main__':
    unittest.main()
