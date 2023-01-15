x = "Mama Tata Pies Kot"
y = x.split()
print(y)

z1 = "Mama.Tata.Pies.Kot"
z2 = z1.split(".")
print(z2)

with open("C:\\Users\\patry\\Desktop\\2022 Pyton programowanie - studia podyplomowe\\006. Zjazd nr 003, gr. 2 (14-15.01.2023)\\2023.01.15_Python_obiektowe\\rozliczenie.csv", "r") as plik_csv:
    content = plik_csv.readlines()
print(content)
print(content[4])

for i in range(len(content)):
    print(content[i])
    content[i] = content[i].split(";")
    print(content[i])

print(content)
print(content[5])
print(content[5][2])

#ZADANIE Obliczyć średnią wypłatę
total = 0
for i in range(1, len(content)):  #dajemy od 1, bo w pierwszym wierszu (wiersz 0) jest nazwa kolumny, a nie wartosc wypłaty
    total += int(content[i][1])  # zamieniamy stringi na integer, aby móc sumować

average = total / (len(content)-1)   #ilosc linii jest 37, ale pracownikow 36, stąd odejmujemy 1 w mianowniku
print(round(average))


#ZADANIE Obliczenie liczby osób na macierzyńskim
total = 0
for i in range(1, len(content)):
    print(content[i][4])
    content[i][4] = content[i][4].replace("\n","")
    if content[i][4] == "t" and content[i][3] == "k":
        total += 1

print(total)
print(content[7])