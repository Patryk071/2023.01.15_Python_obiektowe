class Audi:
    def __init__(self, barwa, info_wprowadzone):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info_wprowadzone
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.maxspeed = 250
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
            self.maxspeed = 90
            print("Tryb eco")
        elif self.tryb == "normal":
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False
            self.maxspeed = 250
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
    def tankowanie(self, ile_litrow):
       if self.ilosc_paliwa + ile_litrow > 70:
            print("Bak paliwa jest za maly.")
       elif ile_litrow < 5:
            print("Za mala ilosc do zatankowania")
       else:
            self.ilosc_paliwa += ile_litrow
            print(f'Zatankowano {ile_litrow} litrow paliwa. Obecnie auto ma w baku {self.ilosc_paliwa}l paliwa.')

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
moje_auto.tankowanie(20)
moje_auto.tankowanie(4)
