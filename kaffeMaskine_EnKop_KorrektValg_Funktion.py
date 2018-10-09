# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:49:09 2018

Dette program modellerer funktionaliteten af en kaffemaskine.
Brugeren kan vælge mellem tre typer kaffe, tre størrelser og tre styrker.
Denne udgave tager højde for forkert valg fra brugerens side via et while loop.
Bruger funktioner til at genbruge kode

@author: HTH
"""

###############################################################################
# Definerer variable
kaffeStyrkeListe = ["Mild", "Almindelig", "Stærk"]
kopStørrelseListe = ["Lille", "Mellem", "Stor"]
kaffeTypeListe = ["Kaffe", "Capuccino", "Espresso"]

# Brugerens valg bliver gemt i en liste
brugerensValgListe = []

###############################################################################
# Funktions-definitioner
def brugerensValg(valg, muligheder, brugerensValgListe, korrektValg):
    for valgIndeks in range(len(muligheder)):
        if valg == muligheder[valgIndeks]:
            brugerensValgListe.append(valg)
            korrektValg = True
            return brugerensValgListe, korrektValg
    print("Ugyldigt valg.\n")
    korrektValg = False
    return brugerensValgListe, korrektValg

###############################################################################
# Brugeren vælger styrke
while True:
    korrektValg = False
    styrke = input("Vælg styrke: Mild, Almindelig, Stærk: ")
    styrke = styrke.title()
    brugerensValgListe, korrektValg = brugerensValg(styrke, kaffeStyrkeListe, brugerensValgListe, korrektValg)
    if korrektValg:
        break

################################################################################
# Brugeren vælger størrelse
while True:
    korrektValg = False
    størrelse = input("Vælg størrelse: Lille, Mellem, Stor: ")
    størrelse = størrelse.title()
    brugerensValgListe, korrektValg = brugerensValg(størrelse, kopStørrelseListe, brugerensValgListe, korrektValg)
    if korrektValg:
        break
    
################################################################################
# Brugeren vælger type
while True:
    korrektValg = False
    kaffeType = input("Vælg type: Kaffe, Capuccino, Espresso: ")
    kaffeType = kaffeType.title()
    brugerensValgListe, korrektValg = brugerensValg(kaffeType, kaffeTypeListe, brugerensValgListe, korrektValg)
    if korrektValg:
        break
    
################################################################################
# Udskriver til sidst brugerens valg
print("Du har valgt en: " + brugerensValgListe[1].lower() + ", " + brugerensValgListe[0].lower() + " " + brugerensValgListe[2].lower())