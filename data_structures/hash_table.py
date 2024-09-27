class HashTable:
    def __init__(self, size=1000):
        self.table = [None] * size
        self.size = size
    
    def custom_hash(self, key):
        return hash(key) % self.size
    
    def add_item(self, key, value):
        index = self.custom_hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for item in self.table[index]:
                if item[0] == key:
                    item = (key, value)
                    return
            self.table[index].append((key, value))
    
    def get_item(self, key):
        index = self.custom_hash(key)
        if self.table[index] is None:
            return None
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None