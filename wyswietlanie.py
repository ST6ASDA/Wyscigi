from collections import defaultdict


def pokaz_pozycje(zawodnicy, trasa):
    grupy = defaultdict(list)

    for z in zawodnicy:
        if z.ukonczyl:
            grupy["META"].append(z)
        else:
            nazwa = trasa[z.trasa_index].nazwa
            grupy[nazwa].append(z)

    print("\n--- GDZIE KTO JEST ---")
    for miejsce, lista in grupy.items():
        print(f"\n[{miejsce}]")
        for z in lista:
            print(f"  Z{z.id} ({z.nazwa()}) -> {z.komentarz()}")