import pytest

from Seidel.main import seidel, czy_sprzeczny


class TestSeidel:
    def test_case_A(self, capsys):
        # TEST A
        # max y
        #
        # y = < 1           [0, 1, -1]
        # x - y = < -1      [1, -1, 1]
        # -x + y = < 0      [-1, 1, 0]
        #
        # :::: sprzeczny
        ograniczenia_a = [[0, 1, -1], [1, -1, 1], [-1, 1, 0]]
        seidel(ograniczenia_a)
        captured = capsys.readouterr()
        assert captured.out == "Zaszla sprzecznosc, kończę..."

    def test_case_B(self, capsys):
        # TEST B
        # max
        # y
        #
        # y = < 1           [0, 1, -1]
        # x - y = < -1      [1, -1, 1]
        # -2x + y = < 0     [-2, 1, 0]
        # x + y = < 0       [1, 1,  0]
        #
        # :::: sprzeczny

        ograniczenia_b = [[0, 1, -1], [1, -1, 1], [-2, 1, 0], [1, 1, 0]]
        seidel(ograniczenia_b)
        captured = capsys.readouterr()
        assert captured.out == "Zaszla sprzecznosc, kończę..."

    def test_case_Y(self, capsys):
        ograniczenia_y = [[0, 1, -2], [-1, 1, 0], [1, 1, 0], [0, -1, -2], [-2, -1, -2], [2, 1, 2]]
        seidel(ograniczenia_y)
        captured = capsys.readouterr()
        assert captured.out == "Unormowano"

    def test_sprzecznosc(self):
        assert czy_sprzeczny([[-1, -1, 2], [1, 1, 0]], [1, 1, 0]) == False