import random
from abc import ABC, abstractmethod
from typing import Dict, List


class Zawodnik(ABC):
    id_counter = 1

    def __init__(self):
        self.id = Zawodnik.id_counter
        Zawodnik.id_counter += 1

        self.sila = 0
        self.inteligencja = 0
        self.zwinnosc = 0

        self.trasa_index = 0
        self.postep: Dict[str, float] = {"sila": 0.0, "inteligencja": 0.0, "zwinnosc": 0.0}
        self.ukonczyl = False
        self.miejsce = None
        self.tury = 0
        self.tury_na_elemencie = 0

        self.debuff_zwinnosc = 0
        self.debuff_tury = 0

    @abstractmethod
    def nazwa(self) -> str:
        pass

    def aktualna_zwinnosc(self) -> int:
        return max(0, self.zwinnosc - self.debuff_zwinnosc)

    def nowa_tura(self):
        if self.debuff_tury > 0:
            self.debuff_tury -= 1
            if self.debuff_tury == 0:
                self.debuff_zwinnosc = 0

    def losuj_umiejetnosc(self) -> str:
        return random.choice(["sila", "inteligencja", "zwinnosc"])

    def specjalna(self, element, zawodnicy: List["Zawodnik"]):
        return {}

    def komentarz(self) -> str:
        return "idzie przed siebie bez większego planu"