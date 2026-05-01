class ElementTrasy:
    def __init__(self, nazwa, sila, inteligencja, zwinnosc, typ="normalny"):
        self.nazwa = nazwa
        self.wymagania = {
            "sila": sila,
            "inteligencja": inteligencja,
            "zwinnosc": zwinnosc,
        }
        self.typ = typ


ELEMENTY = [
    ElementTrasy("Droga", 0, 0, 100),
    ElementTrasy("Lesna droga", 50, 0, 150),
    ElementTrasy("Zadanie matematyczne", 0, 100, 0),
    ElementTrasy("Zadanie fizyczne", 0, 150, 0, "fizyczny"),
    ElementTrasy("Rzeka", 100, 0, 150, "wodny"),
    ElementTrasy("Strumien", 50, 0, 100, "wodny"),
    ElementTrasy("Podnoszenie ciezarow", 200, 0, 0, "fizyczny"),
    ElementTrasy("Piaskowa dolina", 50, 50, 50),
    ElementTrasy("Blazen", 200, 200, 200),
    ElementTrasy("Lodowa sciezka", 80, 20, 120, "wodny"),
    ElementTrasy("Labirynt", 30, 140, 60),
]