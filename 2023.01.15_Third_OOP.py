class Pracownik:
#imie, nazwisko, rok urodzenia, stopien, liczba_dni_urlopu
    def __init__(self, imie_pracownika, nazwisko_pracownika, rok_urodzenia_pracownika):
        self.imie = imie_pracownika
        self.nazwisko = nazwisko_pracownika
        self.rok_urodzenia = rok_urodzenia_pracownika
        self.stopien = 1
        self.liczba_dni_urlopu = 26
    def __str__(self):
        info = f'To jest {self.imie}, urodzony w {self.rok_urodzenia}. Ma dostepnych {liczba_dni_urlopu} dni urlopu.'
        return info
    def urlop(self, liczba_dni):
        if self.liczba_dni_urlopu < liczba_dni:
            print("Nie mozna. Zadana ilosc urlopu jest wieksza niz dostepna ilosc dni wolnych.")
        else:
            self.liczba_dni_urlopu -= liczba_dni


p1 = Pracownik("Kamil", "Musial", 88)
p2 = Pracownik("Andrzej", "Dragan", 78)
p3 = Pracownik("Maria", "Peszek", 75)

print(p1.nazwisko)
print(p3.rok_urodzenia)
p2.rok_urodzenia = 74
print(p2.rok_urodzenia)

