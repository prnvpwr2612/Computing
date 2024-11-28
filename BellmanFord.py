class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    def __init__(self, vertices, edges):
        self.V = vertices
        self.E = edges
        self.edge = []

    def add_edge(self, source, destination, weight):
        if source >= self.V or destination >= self.V:
            print(f"Error: vertex out of range. Valid range is 0 to {self.V-1}.")
            return
        self.edge.append(Edge(source, destination, weight))


def bellman_ford(graph, source):
    V = graph.V
    E = len(graph.edge)
    distance = [float('inf')] * V
    distance[source] = 0

    # Relax edges V-1 times
    for _ in range(V - 1):
        for edge in graph.edge:
            u = edge.source
            v = edge.destination
            weight = edge.weight
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    # Check for negative weight cycles
    for edge in graph.edge:
        u = edge.source
        v = edge.destination
        weight = edge.weight
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Graph contains negative weight cycle")
            return

    print("Vertex Distance from Source")
    for i in range(V):
        print(f"{i}\t\t{distance[i]}")


# Input section
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

graph = Graph(V, E)

print("Enter source, destination, and weight for each edge:")
for _ in range(E):
    source, destination, weight = map(int, input().split())
    graph.add_edge(source, destination, weight)

source = int(input("Enter source vertex: "))
if source < 0 or source >= V:
    print(f"Invalid source vertex. Valid range is 0 to {V-1}.")
else:
    bellman_ford(graph, source)