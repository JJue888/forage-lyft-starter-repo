from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        for i in range(0, len(self.wear_array)):
            if self.wear_array[i] >= 0.9:
                return True
            else:
                pass
        return False
