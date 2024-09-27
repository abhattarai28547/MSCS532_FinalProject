import heapq

class FibonacciHeapNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0
    
    def insert(self, value, priority):
        node = FibonacciHeapNode(value, priority)
        if self.min_node is None:
            self.min_node = node
        else:
            # Merge node with the root list
            if priority < self.min_node.priority:
                self.min_node = node
        self.total_nodes += 1
    
    def extract_min(self):
        # Implement min extraction
        pass
