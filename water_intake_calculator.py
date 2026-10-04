#Alusta programmi
#Salvesta muutujasse goal väärtus 2000
#Küsi kasutajal: "Mitu klaasi vett sa oled täna joonud?:"
#Salvesta vastus muutujasse glasses
#Arvuta kogus milliliitritesse
#Salvesta tulemus muutujasse water
#Arvuta, mitu protsenti päevanormist on täidetud
#Salvesta tulemus muutujasse percent
#Kuva päevanormi täitumise protsent
#Kui protsent on <50: "Joo rohkem vett, keha vajab seda!"
#Kui protsent <100: "Tubli, jätka samas vaimus!"
#Kui protsent ≥100: "Suurepärane, oled oma päevase eesmärgi täitnud!"
#Lõpeta programm


goal = 2000

glasses = int(input("Mitu klaasi vett sa oled täna joonud?:"))

water = glasses * 250

percent = (water/goal) * 100

print(f"{percent}%")

if percent <50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent <100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")