import random
from zawodnik import Zawodnik

class Ork(Zawodnik):
    def __init__(self):
        super().__init__()
        self.sila = random.randint(12, 20)
        self.inteligencja = random.randint(1, 6)
        self.zwinnosc = random.randint(3, 10)

    def nazwa(self):
        return "Ork"

    def komentarz(self):
        return "biegnie, bo ktoś powiedział że na mecie jest jedzenie"