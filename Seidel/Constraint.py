

class Constraint:
    def __init__(self, x, y, b):
        self.x = x
        self.y = y
        self.b = b
        self.sideX = self.getSide(x)
        self.sideY = self.getSide(y)


    def getSide(self, side):
        if side < 0:
            return -1
        elif side == 0:
            return 0
        else:
            return 1

    def FX(self, x):
        return x * (-1 * self.x / self.y) +self.b / self.y

    def FY(self, y):
        return -1 * y * self.y / self.x + self.b / self.x

    def contains(self, x: float, y: float):
        return x * self.x + y * self.y <= self.b

    def intersection(self, checkCon):
        l1 = self
        l2 = checkCon
        if type(checkCon) != type(self):
            raise ValueError("checkCon is not Constraint type")

        if l2.x == 0 or l2.y == 0:
            temp = l1
            l1 = l2
            l2 = temp

        if l1.x == l2.x and l1.y == l2.y:
            if l1.b == -1 * l2.b:
                return [[0, l1.FX(0)], 2]
            else:
                return [[0, l1.FX(0)], 0]

        else:
            if l1.x == (-1 * l2.x) and l1.y == (-1 * l2.y):
                if l1.b == (-1 * l2.b):
                    return [[0, l1.FX(0)], 2]
                else:
                    if l1.x < 0:
                        temp = l1
                        l1 = l2
                        l2 = temp
                    else:
                        return [[0, 0], 0]

        if l1.x == 0:
            resultY = l1.b / l1.y

            if l2.y == 0:
                resultX = l2.b / l2.x
            else:
                resultX = l2.FY(resultY)

            return [[resultX, resultY], 1]

        if l1.y == 0:
            resultX = l1.b / l1.y

            if l2.y == 0:
                resultY = l2.b / l2.y
            else:
                resultY = l2.FX(resultX)

            return [[resultX, resultY], 1]

        resultX = (l1.y * l2.b - l2.y * l1.b) / (l2.x * l1.y - l1.x * l2.y)
        resultY = l1.FX(resultX)

        return [[resultX, resultY], 1]


