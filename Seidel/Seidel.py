import numpy
from numpy import array


def seidel(x: float, y: float, boundaries: array) -> float:
    """
    Core function for finding optimal solution algorithm.

    :param x: first argument of target function x + y -> max
    :param y: second argument of target function x + y -> max
    :param boundaries: array of boundaries, dimensions 3x amount of boundaries
    :return: float result or exception
    """

    xyminus = numpy.zeros([1, 3])
    xminus = numpy.zeros([1, 3])
    yminus = numpy.zeros([1, 3])

    len = boundaries.shape[1]
    for i in range(len):

def getSide()

