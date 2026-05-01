import random
from typing import List
from zawodnik import Zawodnik
from trasa import ElementTrasy


def algorytm(z: Zawodnik, element: ElementTrasy, T: float, zawodnicy: List[Zawodnik]):
    # nowa tura zawodnika
    z.nowa_tura()
    z.tury += 1
    z.tury_na_elemencie += 1

    # specjalne zdolności klas (Robot, Czarodziej, Wilkolak...)
    spec = z.specjalna(element, zawodnicy) or {}

    # 1) CHAOTYCZNY LOSOWY POSTĘP (może nawet trochę cofnąć)
    for dz in z.postep:
        los = random.randint(-5, 12)
        z.postep[dz] = max(0.0, z.postep[dz] + los * T)

    # 2) DUŻY SKOK w jednej umiejętności zależnej od zawodnika
    um = z.losuj_umiejetnosc()

    wartosc = getattr(z, um)
    if um == "zwinnosc":
        wartosc = z.aktualna_zwinnosc()

    # modyfikatory specjalne
    if "mult" in spec:
        wartosc *= spec["mult"]
    if um in spec:
        wartosc += spec[um]

    z.postep[um] += random.randint(10, 25) + wartosc * T

    # 3) MECHANIZM GWARANCJI PRZEJŚCIA TEGO KONKRETNEGO ELEMENTU
    # im dłużej stoi na tym elemencie, tym szybciej go kończy
    for dz in z.postep:
        wymagane = element.wymagania[dz]
        if wymagane == 0:
            continue

        brak = wymagane - z.postep[dz]
        if brak > 0:
            # narastająca presja czasu
            z.postep[dz] += brak * 0.12 * z.tury_na_elemencie * T

    # 4) SPRAWDZENIE CZY UKOŃCZYŁ ELEMENT
    if all(z.postep[d] >= element.wymagania[d] for d in z.postep):
        print(f" -> Z{z.id} ({z.nazwa()}) ukończył element: {element.nazwa}")

        z.trasa_index += 1
        z.postep = {"sila": 0.0, "inteligencja": 0.0, "zwinnosc": 0.0}
        z.tury_na_elemencie = 0