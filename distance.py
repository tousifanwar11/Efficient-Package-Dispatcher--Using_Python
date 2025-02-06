class DistanceTable:
    def __init__(self, distances):
        self.distances = distances

    def get_distance(self, location1, location2):
        return self.distances.get((location1, location2), float('inf'))