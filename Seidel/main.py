from typing import TYPE_CHECKING

from Seidel import Constraint
from Seidel.Constraint import Point

if TYPE_CHECKING:
    from typing import List



def main(constraints: "List", target: Point=Point(0, 1)) -> float:
    """
    Main function for solving Seidel algorithm

    :param target: target function to maximize. For the sake of the project, it equals to [0, 1]
    :param constraints: List of at least 2 Constraint type objects
    :return: Optimal solution of the problem
    """
    if len(constraints) < 2:
        raise Exception("less than 2 constraints were given")
    for i in constraints:
        if not isinstance(i, Constraint):
            raise Exception("Element is not of type Constraint")



    return 0