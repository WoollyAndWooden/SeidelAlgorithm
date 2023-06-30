# nie potrzebujemy inputu od uzytkownika, mozemy go miec hardcode'owanego
# z przykladami od prof. Żylińskiego i własnymi

# TODO zrobić funkcję podającą przykład seidlowi (można w pętli kilka przykładów)
# ewentualnie po prostu input od uzytkownika wybierajacy ktory przyklad

# potrzebujemy klasy na
# - funkcję celu
# - ograniczenia
# reszta wyjdzie w praniu
import copy
import numpy
# TEST A
# max y
#
# y = < 1           [0, 1, -1]
# x - y = < -1      [1, -1, 1]
# -x + y = < 0      [-1, 1, 0]
#
# :::: sprzeczny

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

# TEST MOJ WLASNY
constraints_wlasne = []


# TEST A
# SPRZECZNY
# constraints_a = [[0, 1, -1], [1, -1, 1], [-1, 1, 0]]

# TEST Y
# OPTIMUM = -2/3 i -2/3
ograniczenia_y = [[0, 1, -2], [-1, 1, 0], [1, 1, 0], [0, -1, -2], [-2, -1, -2], [2, 1, 2]]
# ograniczenia_y = [[-1, 1, 0], [1, 1, 0], [0, -1, -2], [-2, -1, -2], [2, 1, 2]]




# pomocnicza funkcja
def print_ograniczenia(ograniczenia):
    print("Aktualny status ograniczeń:")
    for o in ograniczenia:
        print(o)
    print()


def wyznacz_h_min(ograniczenia):
    # sprawdz czy mamy ograniczenie spelniajace w postaci (0, 1, C)
    for o in ograniczenia:
        if o[0] == 0 and o[1] == 1:
            return o

    # jeśli nie, znajdz pp z najwiekszym B
    o_posortowane = sorted(ograniczenia, key=lambda x: x[1], reverse=True)

    for o in o_posortowane:
        if abs(o[0]) == 1 and abs(o[1]) != 0:
            return o

    # jezeli zaden z powyzszych, poszukaj w postaci (0, -1, C)
    for o in ograniczenia:
        if o[0] == 0 and o[1] == -1:
            return o

def czy_sprzeczny(ograniczenia, h_min):
    # TODO zobacz kroki A.2 i A.4 bo nie pamietam czy trzeba bylo
    for o in ograniczenia:
        if numpy.array_equiv(o, h_min):
            continue

        # przypadek A.1
        if h_min[0] == 1 and o[0] == -1 and o[1] > -h_min[1]:
            return True
        # przypadek A.3
        if h_min[0] == -1 and o[0] == 1 and o[1] > -h_min[1]:
            return True

        # przypadek A.5
        if h_min[0] == 0 and o[0] == 0 and o[1] > -h_min[1]:
            return True
    return False

def wyznacz_h_startowe(ograniczenia, h_min):
    # B
    if h_min[1] <= 0:
        print("Przypadek nieograniczony")


    for o in ograniczenia:
        if numpy.array_equiv(o, h_min):
            continue
        # C.1
        if h_min[0] == 1 and o[0] == -1:
            if (o[1] >= 0 and h_min[1] >= o[1]) or (o[1] > -h_min[1] and o[1] < 0):
                return (h_min, o)
            if -h_min[1] == o[1]:
                return None
        # # C.2
        # if h_min[0] == -1 and o[0] == 1:
        #     if o[1] == h_min[1] or abs(o[1]) < abs(h_min[1]):
        #         return (h_min, o)
        #     if -h_min[1] == o[1]:
        #         return None
        #
        # # C.3
        # if not h_min[0] == 0 and abs(h_min[1]) == 1:
        #     return None
        # if not o[0] == 0 and o[1] == -1:
        #     o_temp.append(o)

    for o in ograniczenia:
        if numpy.array_equiv(o, h_min):
            continue
        # C.2
        if h_min[0] == -1 and o[0] == 1:
            if o[1] == h_min[1] or abs(o[1]) < abs(h_min[1]):
                return (h_min, o)
            if -h_min[1] == o[1]:
                return None

    o_temp = []
    for o in ograniczenia:
        if numpy.array_equiv(o, h_min):
            continue
        # C.3
        if not (h_min[0] == 0 and abs(h_min[1]) == 1):
            return None
        if not o[0] == 0 and o[1] == -1:
            o_temp.append(o)

    for o in o_temp:
        if o[0] != 0 or o[1] != 1:
            chj = 0
            # TODO c 3.1 3.2 3.3 ogarnij to ladnie
            # potem masz gotowa baze zeby rozwiazywac rownania liniowe





def unormowanie(ograniczenia):
    # TODO zamien potem c na o bo sie rozmyslilem i wole po polsku bo mam notatki po polsku
    for o in ograniczenia:
        # jeżeli A != 0, to dzielimy ograniczenie przez |A|
        if o[0] != 0:
            temp = abs(o[0])
            o[0] = o[0] / temp
            o[1] = o[1] / temp
            o[2] = o[2] / temp

        # jeżeli A == 0 i B != 0, to dzielimy ograniczenie przez |B|
        if o[0] == 0 and o[1] != 0:
            temp = abs(o[1])
            o[1] = o[1] / temp
            o[2] = o[2] / temp


def seidel(ograniczenia):
    # przetwarzanie wstepne
    # 1. zakladamy ze juz w takiej formie
    # 2. unormowanie
    unormowanie(ograniczenia)
    print("Unormowano")
    # 3. Wektory normalne - nie musimy nic robic, to są pozycje A, B z (A, B, C)
    # 4. Wyznaczamy h_min przez szukanie najmniejszego kąta wektor normalny vs oś Y
    h_min = wyznacz_h_min(ograniczenia)
    print(h_min)

    # 5.A sprawdz sprzecznosc
    if czy_sprzeczny(ograniczenia, h_min):
        print("Zaszla sprzecznosc, kończę...")
    else:
        print("Nie ma sprzecznosci")

    # 5.B



# tymczasowo tu wybieramy przyklad
# wybralem przyklad Y bo ma rozwiazanie konkretne i latwo sie operuje na duzych ilosciach rzeczy
ograniczenia = copy.deepcopy(ograniczenia_y)

print_ograniczenia(ograniczenia)

unormowanie(ograniczenia)
print_ograniczenia(ograniczenia)

seidel(ograniczenia)

# wektory do polplaszczyzny to po prostu [A, B] z (A, B, C)
