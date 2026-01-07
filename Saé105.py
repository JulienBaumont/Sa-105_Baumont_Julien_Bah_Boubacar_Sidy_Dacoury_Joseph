import csv
from matplotlib import pyplot as plt
#région française :
table_fr = []
with open('conso_brute_France.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table_fr.append(row)
#on commence par évaluer la consommation en France 
conso_france=[]
for i in range(1, len(table_fr)):
        conso_france.append(table_fr[i][2])
print(conso_france)
#on passe de str a int pour les Twh
valeur=[]
for k in conso_france :
    valeur_float=float(k.replace(",", "."))
    valeur.append(int(valeur_float))
print(valeur)

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

table_prod_fr = []
with open('production_elec_france.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        table_prod_fr.append(row)
        
prod_france=[]
for i in range(1, len(table_prod_fr)):
        prod_france.append(table_prod_fr[i][2])
print(prod_france)

valeur_prod=[]
for f in prod_france :
    valeur_float2=float(f.replace(",", "."))
    valeur_prod.append(int(valeur_float2))
print(valeur_prod)

dates2=[]
for j in range(1,len(table_prod_fr)):
    dates2.append(table_prod_fr[j][0][:4])

plt.bar(dates2,prod_france)
plt.title("Evolution de la production d'électricité en France ")
plt.ylabel('production en Twh')
plt.xlabel('date')
plt.show()