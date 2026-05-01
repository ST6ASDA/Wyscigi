import random
from zawodnik import Zawodnik

class Elf(Zawodnik):
    def __init__(self):
        super().__init__()
        self.sila = random.randint(3, 9)
        self.inteligencja = random.randint(8, 15)
        self.zwinnosc = random.randint(6, 14)

    def nazwa(self):
        return "Elf"

    def komentarz(self):
        return "biegnie z gracją modela z reklamy"