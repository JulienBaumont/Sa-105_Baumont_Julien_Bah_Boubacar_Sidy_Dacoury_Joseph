import csv
from matplotlib import pyplot as plt
#Partie 1 : Consommation en France
table_fr = []
with open('conso_brute_France.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table_fr.append(row)
#on commence par étudier la consommation en France 
conso_france=[]
for i in range(1, len(table_fr)):
        conso_france.append(table_fr[i][2])
#print(conso_france)
#on passe de str a int pour les Twh
valeur=[]
for k in conso_france :
    valeur_float=float(k.replace(",", "."))
    valeur.append(int(valeur_float))
#print(valeur)

dates=[]
for j in range(1,len(table_fr)):
    dates.append(table_fr[j][0][:4])#on garde uniquement l'année pour aléger le graphique
#[:4] pour prendre tous les indices jusqu'à 4
#courbe de consomation en France
plt.bar(dates,valeur)
plt.title("Evolution de la consommation d'électricité en France ")
plt.ylabel('conso en Twh')
plt.xlabel('date')
plt.show()
#print(len(valeur))

total_france2014_2025=0
for i in range(230, 373):  #valeur de 2014 à 2025
    total_france2014_2025 = total_france2014_2025 + valeur[i]
print("La consomation totale de la france entre 2014 et 2025 est de" ,total_france2014_2025,"Twh")
#par région française
conso_par_region = {}
with open("conso_region_france.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)  # enlever l'en-tête

    for row in reader:
        region = row[1]
        valeur = float(row[3].replace(",", "."))

        if region in conso_par_region:
            conso_par_region[region] = conso_par_region[region] + valeur
        else:
            conso_par_region[region] = valeur

classement = list(conso_par_region.items())

for i in range(len(classement)):
    for j in range(i + 1, len(classement)):
        if classement[i][1] < classement[j][1]:
            classement[i], classement[j] = classement[j], classement[i]

for region, total in classement:
    print(region, ":", round(total, 2), "TWh")#donne le classement arrondi a 2 chiffres après la virgule des régions les plus consommatrices
    
regions = []
consommations = []

for region, valeur in classement:
    regions.append(region)
    consommations.append(valeur)

plt.bar(regions,consommations)
plt.title("Consommation totale d'électricité par région")
plt.ylabel('consommation en Twh')
plt.xlabel('Région')
plt.xticks(rotation=45, ha="right")#oriente de 45° les régions pour un meilleur affichage
plt.show()

conso_plus_grand=(consommations[0]-total_france2014_2025)/total_france2014_2025*100
print("la consommation de la région la plus consommatrice correspond a une difference de",round(conso_plus_grand),"soit environ",round(conso_plus_grand+100),"% du total")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Partie 2 : Conommation en Europe
#consommation totale de l'europe
table_UE = []
with open('conso_pays_europe.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table_UE.append(row)
        
conso_europe=[]
for i in range(1, len(table_UE)):
        conso_europe.append(table_UE[i][3])
        
valeur3 = []
for d in conso_europe:
    valeur_float3 = float(d.replace(",", "."))
    valeur3.append(int(valeur_float3))
    
dates3=[]
for j in range(1,len(table_UE)):
    dates3.append(table_UE[j][0][:4])

plt.bar(dates3,valeur3)
plt.title("Evolution de la consommation d'électricité en Europe ")
plt.ylabel('conso en Twh')
plt.xlabel('date')
plt.show()

total_UE2016_2025 = 0
for v in valeur3:
    total_UE2016_2025 = total_UE2016_2025 + v
print("La consommation totale de l'Europe entre 2016 et 2025 est de" ,total_UE2016_2025,"Twh")


#on étudie la consommation par pays:
conso_par_pays = {}
with open("conso_pays_europe.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)  # enlever l'en-tête

    for row in reader:
        pays = row[1]
        valeur2 = float(row[3].replace(",", "."))#on passe les valeurs de str à float

        if pays in conso_par_pays:
            conso_par_pays[pays] = conso_par_pays[pays] + valeur2
        else:
            conso_par_pays[pays] = valeur2

classement_europe = list(conso_par_pays.items())
for p in range(len(classement_europe )):
    for l in range(p + 1, len(classement_europe )):
        if classement_europe [p][1] < classement_europe [l][1]:
            classement_europe [p], classement_europe [l] = classement_europe [l], classement_europe [p]
print(classement_europe )

for pays, total2 in classement_europe:
    print(pays, ":", round(total2, 2), "TWh")#donne le classement arrondi a 2 chiffres après la virgule des régions les plus consommatrices
    
pays_europe = []
consommations2 = []

for pays, valeur2 in classement_europe:
    pays_europe.append(pays)
    consommations2.append(valeur2)

plt.bar(pays_europe,consommations2)
plt.title("Consommation totale d'électricité par pays")
plt.ylabel('consommation en Twh')
plt.xlabel('pays')
plt.xticks(rotation=45, ha="right")#oriente de 45° les régions pour un meilleur affichage
plt.show()

conso_plus_grand_europe=(consommations2[0]-total_UE2016_2025)/total_UE2016_2025*100
print("la consommation de la région la plus consommatrice correspond a une difference de",round(conso_plus_grand_europe),"soit environ",round(conso_plus_grand_europe+100),"% du total")

#par moyenne
table_UE = []

somme_annee = {}

with open("conso_pays_europe.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    next(reader) 

    for row in reader:
        table_UE.append(row)

        date = row[0]
        pays2 = row[1] 
        valeur = float(row[3].replace(",", "."))

        annee = date[:4]
        cle = (pays2, annee)

        if cle in somme_annee:
            somme_annee[cle] = somme_annee[cle] + valeur
        else:
            somme_annee[cle] = valeur

somme_par_pays = {}
compteur_par_pays = {}

for (pays, annee) in somme_annee:
    total_annuel = somme_annee[(pays, annee)]

    if pays in somme_par_pays:
        somme_par_pays[pays] = somme_par_pays[pays] + total_annuel
        compteur_par_pays[pays] = compteur_par_pays[pays] + 1
    else:
        somme_par_pays[pays] = total_annuel
        compteur_par_pays[pays] = 1

moyenne_annuelle = {}

for pays in somme_par_pays:
    moyenne_annuelle[pays] = somme_par_pays[pays] / compteur_par_pays[pays]
    
for pays in moyenne_annuelle:
    print(pays, ":", round(moyenne_annuelle[pays], 2), "TWh/an")
    
classement3 = list(moyenne_annuelle.items())

for x in range(len(classement3)):
    for y in range(x + 1, len(classement3)):
        if classement3[x][1] < classement3[y][1]:
            classement3[x], classement3[y] = classement3[y], classement3[x]

pays4 = []
consommations4 = []

for pays, valeur in classement3:
    pays4.append(pays)
    consommations4.append(valeur)
    
plt.bar(pays4,consommations4)
plt.title("Consommation moyenne par an pour chaque pays d'Europe")
plt.ylabel('consommation en Twh')
plt.xlabel('pays')
plt.xticks(rotation=45, ha="right")#oriente de 45° les régions pour un meilleur affichage
plt.show()