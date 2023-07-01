import re

import pytest

from Seidel.main import seidel, czy_sprzeczny


class TestSeidel:

    @pytest.fixture()
    def sprzecznosc(self):
        return "Zaszla sprzecznosc"

    def test_case_A(self, capsys, sprzecznosc):
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
        captured = str(capsys.readouterr().out)
        print(captured)
        assert re.search(sprzecznosc, captured)

    def test_case_B(self, capsys, sprzecznosc):
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
        captured = str(capsys.readouterr().out)
        assert re.search(sprzecznosc, captured)

    def test_case_Y(self, capsys):
        ograniczenia_y = [[0, 1, -2], [-1, 1, 0], [1, 1, 0], [0, -1, -2], [-2, -1, -2], [2, 1, 2]]
        seidel(ograniczenia_y)
        captured = str(capsys.readouterr().out)
        assert re.search("Unormowano", captured)

    def test_sprzecznosc(self):
        assert czy_sprzeczny([[-1, -1, 2], [1, 1, 0]], [1, 1, 0])  # tak, jest sprzeczny => true

    def test_sprzecznosc_kolejny(self):
        assert not czy_sprzeczny([[-1, -2, 2], [1, 1, 0]], [1, 1, 0])  # ten przyklad jest niesprzeczny => false

    # def test_nie_sprzecznosc(self):
    #     assert czy_sprzeczny([[-1, -1, 2], [1, 1, 0]], [-1, -1, 2])

    def test_sprzecznosc_main(self, capsys, sprzecznosc):
        seidel([[-1, -1, 2], [1, 1, 0]])
        captured = str(capsys.readouterr().out)
        assert re.search(sprzecznosc, captured)
