# gui/utils.py

import folium
from folium.plugins import MarkerCluster

def show_map(vehicle_routes, warehouse):
    """
    Shows a map with the vehicle routes.

    :param vehicle_routes: List of vehicles with their routes.
    :param warehouse: Warehouse object with the location of the warehouse.
    """
    # Create map centered on the warehouse
    map_ = folium.Map(location=warehouse.get_location(), zoom_start=12)
    
    # Add warehouse marker
    folium.Marker(location=warehouse.get_location(), popup='Warehouse', icon=folium.Icon(color='green')).add_to(map_)

    # Add routes and client markers
    for vehicle in vehicle_routes:
        route = [warehouse.get_location()] + [client.get_location() for client in vehicle.route] + [warehouse.get_location()]
        folium.PolyLine(route, color='blue', weight=2.5, opacity=1).add_to(map_)
        
        for client in vehicle.route:
            folium.Marker(location=client.get_location(), popup=f'Client {client.id}', icon=folium.Icon(color='red')).add_to(map_)
    
    # Save the map to an HTML file
    map_.save('optimized_route.html')
    print("Map saved as 'optimized_route.html'")
