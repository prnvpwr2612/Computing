import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, predecessors

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

start_node = 'A'
distances, predecessors = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(f"To {node}: {distance}")

print("\nShortest paths:")
for node in graph:
    if node != start_node:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = predecessors[current]
        path.reverse()
        print(f"{start_node} to {node}: {' -> '.join(path)}")