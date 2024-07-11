import folium
from folium.plugins import MarkerCluster

def show_map(vehicle_routes, warehouse, filename='optimized_route.html'):
    """
    Shows a map with the vehicle routes and saves it to an HTML file.

    :param vehicle_routes: List of vehicles with their routes.
    :param warehouse: Warehouse object with the location of the warehouse.
    :param filename: The name of the HTML file to save the map.
    """
    # Create map centered on the warehouse
    map_ = folium.Map(location=warehouse.get_location(), zoom_start=12)
    
    # Add warehouse marker
    folium.Marker(location=warehouse.get_location(), popup='Warehouse', icon=folium.Icon(color='green')).add_to(map_)

    # Define a list of colors for the subroutes
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
    
    # Add routes and client markers
    for idx, vehicle in enumerate(vehicle_routes):
        color = colors[idx % len(colors)]  # Cycle through colors if more routes than colors
        route = [warehouse.get_location()] + [client.get_location() for client in vehicle.route] + [warehouse.get_location()]
        folium.PolyLine(route, color=color, weight=2.5, opacity=1).add_to(map_)
        
        for client in vehicle.route:
            folium.Marker(location=client.get_location(), popup=f'Client {client.id}', icon=folium.Icon(color='red')).add_to(map_)
    
    # Save the map to an HTML file
    map_.save(filename)
    print(f"Map saved as '{filename}'")
