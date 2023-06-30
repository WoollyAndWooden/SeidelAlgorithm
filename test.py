
import numpy

from Seidel.Seidel import Seidel

arr = numpy.zeros([3, 3])

arr2 = [[0, 1], 2]
print(arr2[0][1])

print(Seidel(3, 3, [3, 3, 3], [3, 3, 3], [3, 3, 3]).solve())