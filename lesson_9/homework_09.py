class Rhomb:
    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("side_a must be greater than 0")

        if name == "corner_a":
            if not (0 < value < 180):
                raise ValueError("corner_a must be between 0 and 180")

            self.__dict__[name] = value
            self.__dict__["corner_b"] = 180 - value
            return

        self.__dict__[name] = value
