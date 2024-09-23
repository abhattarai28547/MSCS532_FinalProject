class Graph:
    def __init__(self):
        self.adj_list = {}

    # Method to add an edge between two nodes (locations) with the associated cost (e.g., distance, time)
    def add_edge(self, u, v, cost):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append((v, cost))

    # Placeholder for Dijkstra's Algorithm to find the shortest path
    def dijkstra(self, start_node):
        import heapq
        # Priority queue for selecting the next closest node
        queue = [(0, start_node)]
        distances = {node: float('inf') for node in self.adj_list}
        distances[start_node] = 0
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.adj_list[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        
        return distances  # Returns the shortest distances to all other nodes

# Example usage:
g = Graph()
g.add_edge('Supplier1', 'Warehouse1', 10)
g.add_edge('Supplier1', 'Warehouse2', 20)
g.add_edge('Warehouse1', 'Customer1', 15)
g.add_edge('Warehouse2', 'Customer2', 30)

# Get shortest paths from Supplier1
shortest_paths = g.dijkstra('Supplier1')
print(shortest_paths)