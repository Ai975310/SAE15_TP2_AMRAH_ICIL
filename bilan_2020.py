import csv
energie=[]
with open ('RTE_2020.csv', newline='') as csvfile:
	reader=csv.reader(csvfile, delimiter=',')
	for row in reader:
		if row[7] != '' :
			energie.append(row)
	print(energie)
del energie[0]
conso=0
for i in range(0, len(energie)):
	conso=conso+int(energie[i][4])
print("La consommation totale en 2020 est", conso)

#production de Fioul
prod_fioul=0
for i in range(0, len(energie),2):
	energie[i][7]=int(energie[i][7])
	prod_fioul=prod_fioul+energie[i][7]
	
print("La production de Fioul totale en 2020 est", prod_fioul)

#production de Charbon 
prod_charbon=0
for i in range(0, len(energie),2):
	energie[i][8]=int(energie[i][8])
	prod_charbon=prod_charbon+energie[i][8]
	
print("La production de Charbon totale en 2020 est", prod_charbon)

#production gaz 
prod_gaz=0
for i in range (0,len(energie),2):
	energie[i][9]=int(energie[i][9])
	prod_gaz=prod_gaz+energie[i][9]
	
print("La production de gaz totale en 2020 est", prod_gaz)

#production nucléaire
prod_nucleaire=0
for i in range(0,len(energie),2):
	energie[i][10]=int(energie[i][10])
	prod_nucleaire=prod_nucleaire+energie[i][10]
print("La production nucléaire totale en 2020 est", prod_nucleaire)

#production de l'éolien
prod_eolien=0
for i in range(0,len(energie),2):
	energie[i][11]=int(energie[i][11])
	prod_eolien=prod_eolien+energie[i][11]
print("La production de l'éolien totale en 2020 est", prod_eolien)

#production solaire
prod_solaire=0
for i in range (0,len(energie),2):
	energie[i][12]=int(energie[i][12])
	prod_solaire=prod_solaire+energie[i][12]
print("La production solaire totale en 2020 est", prod_solaire)

#production hydraulique
prod_hydrau=0
for i in range (0,len(energie),2):
	energie[i][13]=int(energie[i][13])
	prod_hydrau=prod_hydrau+energie[i][13]
print("La production hydraulique totale en 2020 est", prod_hydrau)

#bioenergie
prod_bio=0
for i in range (0,len(energie),2):
	energie[i][15]=int(energie[i][15])
	prod_bio=prod_bio+energie[i][15]
print("La production des bioenergies totale en 2020 est", prod_bio)

#Production totale en 2020
production_totale=prod_fioul+prod_charbon+prod_gaz+prod_nucleaire+prod_eolien+prod_solaire+prod_hydrau+prod_bio
print("La production totale en 2020 est", production_totale)

#affichage graphique des productions totales en 2020
import matplotlib.pyplot as plt
categories = ['Fioul', 'Charbon', 'Gaz', 'Nucléaire', 'Éolien', 'Solaire', 'Hydraulique', 'Bioénergie']
productions = [prod_fioul, prod_charbon, prod_gaz, prod_nucleaire, prod_eolien, prod_solaire, prod_hydrau, prod_bio]

plt.bar(categories, productions)
plt.xlabel('Types de production')
plt.ylabel('Production en 2020 (RTE)')
plt.title('Production totale d\'énergie en 2020 par source')
plt.show()


conso=0
for i in range (0,len(energie),2):
	energie[i][4]=int(energie[i][4])
	conso=conso+energie[i][4]
print("La consommation en 2020 est,", conso)

noms = ['Consommations', 'Production']
valeurs = [conso, production_totale]
plt.bar(noms, valeurs) ; plt.show() 


#partie d'energie renouvelable
productions_renouvelable=prod_eolien+prod_solaire+prod_bio+prod_hydrau
productions_non_renouvelable= prod_fioul+prod_charbon+prod_gaz+prod_nucleaire

print("Production renouvelable:", productions_renouvelable)
print ("Production non renouvelable:", productions_non_renouvelable)






