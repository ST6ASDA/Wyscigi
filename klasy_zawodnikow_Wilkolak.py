import random
from zawodnik import Zawodnik

class Wilkolak(Zawodnik):
    def __init__(self):
        super().__init__()
        self.sila = random.randint(8, 18)
        self.inteligencja = random.randint(1, 5)
        self.zwinnosc = random.randint(8, 18)

    def nazwa(self):
        return "Wilkolak"

    def specjalna(self, element, zawodnicy):
        if len(zawodnicy) > 1 and random.random() < 0.2:
            ofiara = random.choice([z for z in zawodnicy if z is not self])
            ofiara.debuff_zwinnosc += 3
            ofiara.debuff_tury = 4
            print(f"Wilkolak {self.id} gryzie zawodnika {ofiara.id}!")
        return {}

    def komentarz(self):
        return "patrzy komu tu skoczyć do gardła"