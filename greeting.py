#Alusta programmi
#Küsi kasutajalt: "Mis on sinu perekonna nimi?"
#Salvesta vastus muutujasse family_name
#Küsi kasutajalt: "Mis on sinu sugu? (m/n)"
#Salvesta vastus muutujasse gender.
#Kui kasutaja valib "m", väljasta "Tere, härra (family_name)"
#Kui kasutaja valib "n", väljasta "Tere, proua (family_name)"
#Muidu, kui sisestatakse midagi muud, väljasta "Tere tulemast, (family_name)"
#Lõpeta programm

family_name = input("Mis on sinu perekonna nimi?")
gender = input("Mis on sinu sugu? (m/n)")
if gender == "m":
    print("Tere, härra", family_name + "!")
elif gender == "n":
    print("Tere, proua", family_name + "!")
else:
    print("Tere tulemast,", family_name + "!")
