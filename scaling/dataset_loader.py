import random

def generate_large_dataset(num_nodes, num_edges):
    graph_data = {}
    for i in range(num_nodes):
        graph_data[i] = []
        for _ in range(random.randint(1, num_edges)):
            neighbor = random.randint(0, num_nodes - 1)
            cost = random.uniform(1, 10)
            graph_data[i].append((neighbor, cost))
    return graph_data
