import heapq

class ShipmentQueue:
    def __init__(self):
        self.queue = []

    # Method to add a shipment with a priority
    def add_shipment(self, priority, shipment):
        heapq.heappush(self.queue, (priority, shipment))

    # Method to retrieve the next shipment with the highest priority (lowest priority value)
    def get_next_shipment(self):
        return heapq.heappop(self.queue)

# Example usage:
shipment_queue = ShipmentQueue()
shipment_queue.add_shipment(1, 'UrgentShipment')
shipment_queue.add_shipment(5, 'RegularShipment')
shipment_queue.add_shipment(2, 'PriorityShipment')

# Get the next shipment based on priority
next_shipment = shipment_queue.get_next_shipment()
print(next_shipment)