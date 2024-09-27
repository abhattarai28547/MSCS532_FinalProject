import heapq
from collections import defaultdict
import math

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u, v, cost):
        self.adj_list[u].append((v, cost))
    
    def heuristic(self, node, goal):
        # Example heuristic (Euclidean distance)
        return math.sqrt((goal[0] - node[0])**2 + (goal[1] - node[1])**2)

    def a_star(self, start, goal):
        open_set = [(0, start)]  # Priority queue
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}
        came_from = {}
        
        while open_set:
            current_f, current_node = heapq.heappop(open_set)
            
            if current_node == goal:
                return self.reconstruct_path(came_from, current_node)
            
            for neighbor, cost in self.adj_list[current_node]:
                tentative_g_score = g_score[current_node] + cost
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return None
    
    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        return path[::-1]

# Example usage:
g = Graph()
g.add_edge('Supplier1', 'Warehouse1', 10)
g.add_edge('Supplier1', 'Warehouse2', 20)
g.add_edge('Warehouse1', 'Customer1', 15)
g.add_edge('Warehouse2', 'Customer2', 30)

# Get shortest paths from Supplier1
shortest_paths = g.dijkstra('Supplier1')
print(shortest_paths)