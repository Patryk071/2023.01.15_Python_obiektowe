class Audi:
    def __init__(self, barwa, info_wprowadzone):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info_wprowadzone
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
    def __str__(self):
        napis = (f"Audi ma kolor {self.kolor} i jest w kondycji {self.kondycja}")
        return napis
    def zasieg(self):
            zasieg = self.ilosc_paliwa / self.spalanie_na_100 * 100
            return round(zasieg, 2)
    def ustaw_tryb(self, tryb):
        self.tryb = tryb
        if self.tryb == "eco":
            self.spalanie_na_100 = 10
            self.tryb_ekonomiczny = True
            print("Tryb eco")
        elif self.tryb == "normal":
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False
            print("Tryb normal")
        else:
            print("Tryb nierozpoznany, brak zmian")
    def wlacz_eco(self):
        self.spalanie_na_100 = 10
        self.tryb_ekonomiczny = True
        print("Tryb eco wlaczony")
    def wlacz_normal(self):
        self.spalanie_na_100 = 14
        self.tryb_ekonomiczny = False
        print("Tryb normal wlaczony")
    def zatankuj(self, paliwo_litry):
        self.ilosc_paliwa += paliwo_litry
        print(f'Zatankowano {paliwo_litry} litrow paliwa. Obecnie auto ma w baku {self.ilosc_paliwa}l paliwa.')

moje_auto = Audi("czerwomy", 4)
print(moje_auto.ilosc_paliwa)
print(moje_auto.kondycja)
moje_auto.kondycja +=1
print(moje_auto.kondycja)

auto_sasiada = Audi("zielony", 5)
print(auto_sasiada.kondycja)
print(moje_auto)
print(moje_auto.zasieg())

moje_auto.ustaw_tryb("eco")
print(moje_auto.zasieg())

moje_auto.ustaw_tryb("normal")
print(moje_auto.zasieg())

print(moje_auto.ilosc_paliwa)
moje_auto.zatankuj(20)
moje_auto.zatankuj(5)
