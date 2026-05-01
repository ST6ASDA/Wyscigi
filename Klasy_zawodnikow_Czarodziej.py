import random
from zawodnik import Zawodnik

class Czarodziej(Zawodnik):
    def __init__(self):
        super().__init__()
        self.sila = random.randint(1, 7)
        self.inteligencja = random.randint(6, 21)
        self.zwinnosc = random.randint(2, 9)

    def nazwa(self):
        return "Czarodziej"

    def specjalna(self, element, zawodnicy):
        if element.nazwa == "Blazen":
            return {"mult": 1.75}
        return {}

    def komentarz(self):
        return "rzuca zaklęcie 'oby szybciej'"