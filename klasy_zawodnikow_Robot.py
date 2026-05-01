import random
from zawodnik import Zawodnik

class Robot(Zawodnik):
    def __init__(self):
        super().__init__()
        self.sila = random.randint(5, 19)
        self.inteligencja = random.randint(1, 7)
        self.zwinnosc = random.randint(2, 10)

    def nazwa(self):
        return "Robot"

    def specjalna(self, element, zawodnicy):
        if element.typ == "wodny":
            return {"zwinnosc": -2}
        if element.typ == "fizyczny":
            return {"inteligencja": +2}
        return {}

    def komentarz(self):
        return "analizuje trasę w 0.003 sekundy"