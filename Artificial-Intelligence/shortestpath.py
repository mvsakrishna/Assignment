import networkx as nx
import matplotlib.pyplot as plt

# Create a graph representing the map of Romania
G = nx.Graph()

# Define the cities and their connections
cities = {
    'Arad': {'Zerind', 'Sibiu', 'Timisoara'},
    'Zerind': {'Arad', 'Oradea'},
    'Oradea': {'Zerind', 'Sibiu'},
    'Timisoara': {'Arad', 'Lugoj'},
    'Lugoj': {'Timisoara', 'Mehadia'},
    'Mehadia': {'Lugoj', 'Drobeta'},
    'Drobeta': {'Mehadia', 'Craiova'},
    'Craiova': {'Drobeta', 'Rimnicu Vilcea', 'Pitesti'},
    'Rimnicu Vilcea': {'Craiova', 'Pitesti', 'Sibiu'},
    'Sibiu': {'Arad', 'Oradea', 'Rimnicu Vilcea', 'Fagaras'},
    'Fagaras': {'Sibiu', 'Bucharest'},
    'Pitesti': {'Craiova', 'Rimnicu Vilcea', 'Bucharest'},
    'Bucharest': {'Fagaras', 'Pitesti', 'Giurgiu', 'Urzieeni'},
    'Giurgiu': {'Bucharest'},
    'Urzieeni': {'Bucharest', 'Hirsova', 'Vaslui'},
    'Hirsova': {'Urzieeni', 'Eforie'},
    'Eforie': {'Hirsova'},
    'Vaslui': {'Urzieeni', 'Insi'},
    'Insi': {'Vaslui', 'Neamt'},
    'Neamt': {'Insi'},
}

# Add nodes (cities) and edges (connections) to the graph
for city, connections in cities.items():
    G.add_node(city)
    for connection in connections:
        G.add_edge(city, connection)

# Use Dijkstra's algorithm to find the shortest path from 'Arad' to 'Bucharest'
shortest_path = nx.shortest_path(G, source='Arad', target='Bucharest')

# Print the shortest path
print("Shortest Path from Arad to Bucharest:", shortest_path)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='purple', font_size=10, font_color='black')
nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='red', node_size=3000)
nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)],
                       edge_color='red', width=3)

plt.title("Map of Romania")
plt.show()