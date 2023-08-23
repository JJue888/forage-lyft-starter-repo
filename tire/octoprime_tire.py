from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array
        self.sum = 0

    def needs_service(self):
        for i in range(0, len(self.wear_array)):
            self.sum = self.sum + self.wear_array[i]
        return self.sum >= 3
