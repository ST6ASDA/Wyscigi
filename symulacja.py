import random
from klasy_zawodnikow import *
from trasa import ELEMENTY
from algorytm import algorytm
from wyswietlanie import pokaz_pozycje


DIFFICULTY_MAP = {"latwy": 1.75, "normalny": 1.0, "trudny": 0.6}
KLASY = [Czlowiek, Robot, Czarodziej, Wilkolak, Elf, Ork]


def start():
    n = int(input("Ilu zawodników: "))
    k = int(input("Długość trasy: "))
    diff = input("Trudność: ").lower()

    T = DIFFICULTY_MAP[diff]
    trasa = ELEMENTY[:k]
    zawodnicy = [random.choice(KLASY)() for _ in range(n)]

    miejsce = 1
    tura = 1

    while not all(z.ukonczyl for z in zawodnicy):
        print(f"\n=========== TURA {tura} ===========")

        for z in zawodnicy:
            if z.ukonczyl:
                continue

            algorytm(z, trasa[z.trasa_index], T, zawodnicy)

            if z.trasa_index >= len(trasa):
                z.ukonczyl = True
                z.miejsce = miejsce
                miejsce += 1
                print(f"🏁 Z{z.id} ({z.nazwa()}) dociera na metę!")

        pokaz_pozycje(zawodnicy, trasa)
        tura += 1
        input("ENTER -> dalej")