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
print(len(valeur))

total_france2014_2025=0
for i in range(230, 373):  #valeur de 2014 à 2025
    total_france2014_2025 = total_france2014_2025 + valeur[i]
print("La consomation totale de la france entre 2014 et 2025 est de" ,total_france2014_2025,"Twh")

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