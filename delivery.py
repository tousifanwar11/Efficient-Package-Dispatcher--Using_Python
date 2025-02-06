
from distance import d
from HashTable import HashTable
from truck import Truck


def next_delivery(truck, packages, distances):
    min_distance = float('inf')
    next_package = None
    for package in packages.table:
        for pkg in package:
            if pkg['status'] == 'at the hub':
                distance = distances.get_distance(truck.current_location, pkg['address'])
                if distance < min_distance:
                    min_distance = distance
                    next_package = pkg
    return next_package

def main_delivery_loop(packages, distances, trucks):
    all_delivered = False
    while not all_delivered:
        all_delivered = True
        for truck in trucks:
            if truck.has_capacity():
                package = next_delivery(truck, packages, distances)
                if package:
                    truck.load(package)
                    package['status'] = 'en route'
                    all_delivered = False
            truck.move_to_next_delivery(package, distances)
            truck.deliver('10:00 AM')  # Example time; should be calculated

# Initialize components
packages = HashTable()
distances = distance({('hub', '123 Main St'): 5})  # Example distance
trucks = [Truck() for _ in range(3)]

# Load packages example
packages.insert({'id': 1, 'address': '123 Main St', 'status': 'at the hub'})

# Start delivery system
main_delivery_loop(packages, distances, trucks)
