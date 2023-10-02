import heapq

# Define the map of Romania as a graph
romania_map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101},
}

def dijkstra(graph, start, goal):
    # Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    vertices = [(0, start)]

    while vertices:
        current_distance, current_vertex = heapq.heappop(vertices)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(vertices, (distance, neighbor))

    # Build the shortest path
    path = []
    while goal:
        path.insert(0, goal)
        goal = predecessors[goal]

    return path

# Find the shortest path from 'Arad' to 'Bucharest'
start_city = 'Arad'
goal_city = 'Bucharest'
shortest_path = dijkstra(romania_map, start_city, goal_city)

# Print the shortest path
print(f"Shortest path from {start_city} to {goal_city}: {shortest_path}")
