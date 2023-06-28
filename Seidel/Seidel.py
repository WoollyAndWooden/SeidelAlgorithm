import numpy
from numpy import array

from Seidel.Constraint import Constraint


class Seidel:
    """Main class for Seidel Algorithm."""

    def __init__(self, x: float, y: float, Hx: array, Hy: array, Hb: array):
        Hx = numpy.array(Hx)
        Hy = numpy.array(Hy)
        Hb = numpy.array(Hb)
        self.x = x
        self.y = y
        self.status = 0

        self.f = lambda xp, yp: xp * self.x + yp * self.y

        self.applied = []
        self.applied.append(Constraint(-1, 0, 0))
        self.applied.append(Constraint(0, -1, 0))
        self.solution = []
        self.result = None


        if Hx.shape[0] != Hy.shape[0] or Hx.shape[0] != Hb.shape[0]:
            raise ValueError("Constraints arrays length do not match")

        constraintsNo = Hx.shape[0]
        self.constraints = []

        for i in range(constraintsNo):
            self.constraints.append(Constraint(Hx[i], Hy[i], Hb[i]))

        for i in self.constraints:
            if i.sideX == 1 and i.sideY == 1:
                xyminus = i
                break
            elif i.sideX == 1:
                if yminus == None:
                    xminus = i
                else:
                    if yminus.intersection(i)[1] != 0:
                        xminus = i
                        break

            elif i.sideY == 1:

                if xminus == None:
                    yminus = i
                else:
                    if xminus.intersection(i)[1] != 0:
                        yminus = i
                        break

        possibleSolutions = []
        if xyminus != None:
            self.applied.append(xyminus)
            possibleSolutions.append(xyminus.intersection(self.applied[0])[0])
            possibleSolutions.append(xyminus.intersection(self.applied[1])[0])

            self.constraints.remove(xyminus)
        else:
            if xminus == None or yminus == None:
                if xminus == None:
                    for i in self.constraints:
                        if i.x == 1:
                            self.status = 2
                            break
                elif yminus == None:
                    for i in self.constraints:
                        if i.y == 1:
                            self.status = 2
                            break
                else:
                    self.status = 3

            else:
                self.applied.append(xminus)
                self.applied.append(yminus)

                possibleSolutions.append(xminus.intersection(self.applied[0])[0])
                possibleSolutions.append(xminus.intersection(self.applied[1])[0])

                intersection = yminus.intersection(xminus)

                if intersection[1] == 1:
                    possibleSolutions.append(intersection[0])

        if possibleSolutions:
            legalSolutions = []
            for i in possibleSolutions:
                if self.isPointLegal(i[0], i[1]):
                    legalSolutions.append(i)

            if not legalSolutions:
                self.status = 3
            else:
                self.solution = legalSolutions[0]
                for i in legalSolutions:
                    if self.f(i[0], i[1]) > self.f(self.solution[0], self.solution[1]):
                        self.solution = i


    def solve(self):
        while self.constraints and self.status == 0:
            constraint = self.constraints.pop()
            self.applyConstraint(constraint)

        if self.constraints and self.status == 0:
            self.status = 1

        self.getResult()

    def isPointLegal(self, x, y):
        return x >= 0 and y >= 0

    def applyConstraint(self, constraint: Constraint):
        if constraint.contains(self.solution[0], self.solution[1]):
            self.applied.append(constraint)

        intersections = []

        for i in self.applied:
            result = constraint.intersection(i)[0]
            if result[1] == 0:
                self.status = 2
                break

            for j in self.applied:
                if not j.contains(result[0], result[1]):
                    break

            intersections.append(result[0])

        if not intersections:
            self.status = 2

        else:
            self.solution = intersections[0]

            for i in intersections:
                if self.f(i[0], i[1]) > self.f(self.solution[0], self.solution[1]):
                    self.solution = i

            self.applied.append(constraint)

    def getResult(self):
        if self.status == 1:
            self.result = self.f(self.solution[0], self.solution[1])
        elif self.status == 2:
            raise ValueError("Unsolvable task")
        elif self.status == 3:
            raise ValueError("Infinite amount of results")











