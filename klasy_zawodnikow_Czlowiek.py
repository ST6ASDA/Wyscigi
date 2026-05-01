import random
from zawodnik import Zawodnik


class Czlowiek(Zawodnik):
    def __init__(self):
        super().__init__()
        self.sila = random.randint(2, 10)
        self.inteligencja = random.randint(3, 12)
        self.zwinnosc = random.randint(1, 11)

    def nazwa(self):
        return "Czlowiek"

    def losuj_umiejetnosc(self):
        return min(self.postep, key=self.postep.get)

    def komentarz(self):
        return "marudzi, że buty uwierają"