import numpy

def print_ograniczenia(ograniczenia):
    print("Aktualny status ograniczeń:")
    for o in ograniczenia:
        print(o)
    print()

def y_przeciecia(linia1, linia2):
    a1 = linia1[0]
    a2 = linia2[0]
    b1 = linia1[1]
    b2 = linia2[1]
    c1 = linia1[2]
    c2 = linia2[2]
    print(f"Linia1: {linia1}")
    print(f"Linia2: {linia2}")
    y = (a2 * c1 - a1 * c2)/(-a2 * b1 + a1*b2)
    print(f"y przeciecia: {y}")
    return y


def wyznacz_h_min(ograniczenia):
    # sprawdz czy mamy ograniczenie w postaci (0, 1, C)
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
    for o in ograniczenia:
        if numpy.array_equiv(o, h_min):
            continue

        # przypadek A.1
        if h_min[0] == 1 and o[0] == -1 and o[1] == -h_min[1] and o[2] > -h_min[2]:
            print("Sprzeczność A1")
            return True
        # przypadek A.3
        if h_min[0] == -1 and o[0] == 1 and o[1] == -h_min[1] and o[2] > -h_min[2]:
            print("Sprzeczność A3")
            return True

        # przypadek A.5
        if h_min[0] == 0 and o[0] == 0 and o[1] == -h_min[1] and o[2] > -h_min[2]:
            print("Sprzeczność A5")
            return True

    return False


def wyznacz_h_startowe(ograniczenia, h_min):
    # B
    if h_min[1] <= 0:
        print(" 5b:  Przypadek nieograniczony, obszar nieograniczony")
        return None

    # C.1
    for o in ograniczenia:
        if numpy.array_equiv(o, h_min):
            continue

        if h_min[0] == 1 and o[0] == -1:
            if (0 <= o[1] <= h_min[1]) or (-h_min[1] < o[1] < 0):
                print("C.1: Zwracamy H1 i H2")
                return h_min, o  # zwracamy jako H1, H2 = (H_min, H_j) gdzie o = H_j
            if -h_min[1] == o[1]:
                print("C.1 -> Przypadek nieograniczony")
                return None

    # C.2
    for o in ograniczenia:
        if numpy.array_equiv(o, h_min):
            continue

        if h_min[0] == -1 and o[0] == 1:
            if o[1] == h_min[1] or abs(o[1]) < abs(h_min[1]):
                print("C.2 -> Zwracamy H1 i H2")
                return h_min, o  # zwracamy jako H1, H2 = (H_min, H_j) gdzie o = H_j
            if -h_min[1] == o[1]:
                print("C.2 -> Przypadek nieograniczony niesprzeczny")
                return None

    o_temp = []
    # C.3 tworzymy nową liste ograniczen Hj, nie zawierającą Hi = (0, -1, Ci)

    print("C.3 Na tym etapie dostajemy ograniczenia:")
    print_ograniczenia(ograniczenia)
    print("C.3")

    print("Wyrzucamy takie Hi: (0, -1, Ci)")
    for o in ograniczenia:
        # if numpy.array_equiv(o, h_min):
        #     continue
        if not (h_min[0] == 0 and h_min[1] == 1):  # Czy H_min = (0, 1, Cmin)
            raise Exception("H_min nieprzewidzianej postaci")
        # C.3.1 Wyrzucamy Hi = (0, -1, Ci)

        if o[0] != 0 or o[1] != -1:
            print(f"C.3.1 Dodajemy do nowych bez Hi: {o}")
            o_temp.append(o)

    print("C.3.1 lista z wyrzuconymi Hi:")
    print_ograniczenia(o_temp)

    # C.3.2 Czy wszystkie pozostale Hj są w postaci (0, 1, Cj)
    # sortujemy po Cj malejąco
    o_temp = sorted(o_temp, key=lambda x: x[2], reverse=True)
    print("Posortowane wedlug najwieksze Cj")
    print_ograniczenia(o_temp)

    odpowiednia_postac = True

    for o in o_temp:
        # czy kazde sa w odpowiedniej postaci
        if o[0] != 0 or o[1] != 1:
            odpowiednia_postac = False
            break
    print("Czy wszystkie sa w odpowiedniej postaci Hj = (0, 1, Cj)?")
    if odpowiednia_postac:
        print("Tak, w odpowiedniej postaci -> C.3.2!")
        # C.3.2
        o_cj_min = o_temp[0]
        print(f"C.3.2 Z najwiekszym Cj: {o_cj_min}")
        print(f"C.3.2 Nieskonczenie wiele rozwiazan na prostej y = {-o_cj_min[2]}")
        return None

    print("W nieodpowiedniej postaci -> idziemy do C.3.3")
    print("C.3.3 Szukamy H_max: Hj = (0, 1, Cj) z Cj = MAX")
    h_max = []
    for o in o_temp:
        if o[0] == 0 and o[1] == 1:
            h_max = o
            break

    o_bez_hk = []
    for o in o_temp:
        if numpy.array_equiv(o, h_max):
            continue
        if not (o[0] == 0 and o[1] == 1):
            o_bez_hk.append(o)
    o_bez_hk
    print("C.3.3 Lista ograniczeń z wyrzuconymi Hk = (0, 1, Ck) innymi niz Hmax")
    print(f"C.3.3 Hmax = {h_max}")
    print_ograniczenia(o_bez_hk)

    # mamy teraz H_Max poziome, sprawdzamy je z reszta H
    h_with_xl = []
    h_with_xp = []
    for o in o_bez_hk:
        if o[0] == -1:
            xl = (-o[1] * -h_max[2] - o[2]) / o[0]
            h_with_xl.append([o, xl])
        if o[0] == 1:
            xp = (-o[1] * -h_max[2] - o[2]) / o[0]
            h_with_xp.append([o, xp])
    print(f"Ograniczenia ze swoim xl wzgledem Hmax = {h_with_xl}")
    print(f"Ograniczenia ze swoim xp wzgledem Hmax = {h_with_xp}")

    h_with_xl = sorted(h_with_xl, key=lambda x: x[1], reverse=True)
    h_with_xp = sorted(h_with_xp, key=lambda x: x[1])
    # if not = jezeli pusta
    # jezeli nie ma xp, a sa xl
    if not h_with_xp and h_with_xl:
        print(f"Rozwiązanie jest na prostej y = {-h_max[2]} z opt = ({h_with_xl[0][1]}, {-h_max[2]})")
        return None
    if h_with_xp and not h_with_xl:
        print(f"Rozwiązanie jest na prostej y = {-h_max[2]} z opt = ({h_with_xp[0][1]}, {-h_max[2]})")
        return None

    if h_with_xl[0][1] < h_with_xp[0][1]:
        print(f"Nieskonczenie wiele rozwiązań na odcinku, ({h_with_xl[0][1]}, {-h_max[2]}) - ({h_with_xp[0][1]}, {-h_max[2]})")
    elif h_with_xl[0][1] == h_with_xp[0][1]:
        print(f"Uniknalne rozwiązanie, xl = {h_with_xl[0][1]}, opt = {-h_max[2]}")
    else:
        if h_with_xl[0][0][0] == h_with_xp[0][0][1] and h_with_xl[0][0][1] == h_with_xp[0][0][0]:
            print("C 3.3+  Sprzeczność - proste nie przecinają się")
            return None
        y = y_przeciecia(h_with_xl[0][0], h_with_xp[0][0])
        if y > -h_max[2]:
            print("C3.3 Sprzeczność - punkt przecięcia powyżej H_max")
            return None
        else:
            print("C.3.3: Zwracamy H1 i H2")
            return h_with_xl[0][1], h_with_xp[0][1]


def unormowanie(ograniczenia):
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
    print_ograniczenia(ograniczenia)
    # przetwarzanie wstepne
    # 1. zakladamy ze juz w takiej formie
    # 2. unormowanie
    unormowanie(ograniczenia)
    print("Unormowano")
    print_ograniczenia(ograniczenia)
    # 3. Wektory normalne - nie musimy nic robic, to są pozycje A, B z (A, B, C)
    # 4. Wyznaczamy h_min przez szukanie najmniejszego kąta wektor normalny vs oś Y
    h_min = wyznacz_h_min(ograniczenia)
    print("H min:")
    print(h_min)

    # 5 A sprawdz sprzecznosc
    if czy_sprzeczny(ograniczenia, h_min):
        print("Zaszla sprzecznosc, kończę...")
    else:
        print("Nie ma sprzecznosci")

    # 5.B, 5.C
    h1, h2 = wyznacz_h_startowe(ograniczenia, h_min)
    if h1 is not None:
        print(f"H1: {h1}, H2: {h2}")


ograniczenia_a = [[0, 1, -1], [1, -1, 1], [-1, 1, 0]]  # spodziewany: sprzeczny | wyszlo: sprzeczny
ograniczenia_b = [[0, 1, -1], [1, -1, 1], [-2, 1, 0], [1, 1, 0]]  # spodziewany: sprzeczny | wyszlo: niedokończone
ograniczenia_c = [[1, -1, 0], [0, -1, 1], [-1, -1, 1], [2, -1, 0]]  # spodziewany: nieograniczony opt inft | wyszlo: nieograniczony
ograniczenia_d = [[0, 1, -2], [-1, 1, -2], [0, -1, 0], [-1, -1, -2]]  # spodziewany: nieograniczony z opt w np (0, 2) | wyszlo dobrze
ograniczenia_e = [[0, 1, -2], [-1, 1, -4], [0, -1, 0], [1, -1, 0]] # OPT na odcinku, jego końce to (-2,2)-(2,2) | wyszlo dobrze
ograniczenie_f = [[0, 1, -2], [-1, 1, 0], [1, 1, 0], [0, -1, -2], [-2, -1, -2], [2, 1, 2]]

# ograniczenia_y = [[-1, 1, 0], [1, 1, 0], [0, -1, -2], [-2, -1, -2], [2, 1, 2]]

seidel(ograniczenie_f)
# wysokosc_przeciecia([1, -1, 3], [-2, -1, 6])

# wektory do polplaszczyzny to po prostu [A, B] z (A, B, C)
