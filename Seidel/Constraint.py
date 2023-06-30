class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Constraint:
    def __init__(self, x, y, b):
        self.x = x
        self.y = y
        self.b = b