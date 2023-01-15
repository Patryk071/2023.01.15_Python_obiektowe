import os
import time

#mozna zrobic "import os" albo "from os omport *"

#"import os"
#gdy mamy "import os" trzeba pisać np. "print(os.getcwd())"

#"from os omport *"
#gdy mamy "from os omport *" wsytarczy pisać np. "print(getcwd())"

print(os.getcwd())
os.chdir("C:\\Users\\patry\\Desktop\\2022 Pyton programowanie - studia podyplomowe\\006. Zjazd nr 003, gr. 2 (14-15.01.2023)\\2023.01.15_Python_obiektowe")
print(os.getcwd())

os.mkdir('Nowy_folder')
time.sleep(3)
os.rename("Nowy_folder", "Nowszy_folder")
time.sleep(3)
os.rmdir("Nowszy_folder")

#os.system - lepiej nie uzywac za czesto, bo moga byc
#problemy, gdy bedzie nowa dystrybucja
#systemu operacyjnego i zmiana w komendach lub
#skladni
os.system('cmd /c "dir /s new.txt >> results.txt"')
