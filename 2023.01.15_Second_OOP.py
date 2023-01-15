class Audi:
    def __init__(self):
        self.kolor = "czerwony"
        self.ilosc_paliwa = 10
        self.kondycja = 4

moje_auto = Audi()
print(moje_auto.ilosc_paliwa)
print(moje_auto.kondycja)
moje_auto.kondycja +=1
print(moje_auto.kondycja)

auto_sasiada = Audi()
print(auto_sasiada.kondycja)