import pytest

from Seidel.Seidel import Seidel


class TestSeidel:
    def testConstraintsNotEqual(self):
        with pytest.raises(ValueError, match="Constraints arrays length do not match"):
            Seidel(3, 3, [3, 3], [3, 3, 3], [3, 3])
