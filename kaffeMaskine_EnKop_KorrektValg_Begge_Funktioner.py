# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:57:05 2018

Dette program modellerer funktionaliteten af en kaffemaskine.
Brugeren kan vælge mellem tre typer kaffe, tre størrelser og tre styrker.
Denne udgave tager højde for forkert valg fra brugerens side via et while loop.
Bruger funktioner til at genbruge koden, både når brugeren skal vælge styrke etc., 
samt når valgene skal gemmes i listerne

Funktionerne har docstrings som dokumenterer hvordan de fungerer, samt hvilke 
inputs og outputs de har 

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
    """
    Denne funktion tager som input gyldige valg og brugerens eget valg, og gemmer 
    disse i en liste.
    
    Input:
        valg: brugerens valg (str)
        muligheder: liste over valgmuligheder (liste af str)
        brugerensValgListe: liste med valg som brugeren allerede har foretaget (liste af str)
        korrektValg: indikator om valget er rigtigt (bool)
    
    Output:
        brugerensValgListe: samme som input, men tilføjet med brugerens valg (liste af str)
        korrektValg: indikator om valget er rigtigt (bool)
    """
    for valgIndeks in range(len(muligheder)):
        if valg == muligheder[valgIndeks]:
            brugerensValgListe.append(valg)
            korrektValg = True
            return brugerensValgListe, korrektValg
    print("Ugyldigt valg.\n")
    korrektValg = False
    return brugerensValgListe, korrektValg

def valgTrin(valgBesked, brugerensValgListe, muligheder):
    """
    Denne funktion beder brugeren om et valg (f.eks. kaffetype), op gentager dette 
    indtil et gyldigt valg er lavet. Valget bliver gemt i en liste.
    
    Input:
        valgBesked: tekstbesked med information til brugeren om valgmuligheder (str)
        brugerensValgListe: liste med valg som brugeren allerede har foretaget (liste af str)
        muligheder: liste over valgmuligheder (liste af str)
        
    Output:
        Intet
    """
    while True:
        korrektValg = False
        valg = input(valgBesked)
        brugerensValgListe, korrektValg = brugerensValg(valg, muligheder, brugerensValgListe, korrektValg)
        if korrektValg:
            return
    

# Brugeren vælger styrke
valgTrin("Vælg styrke: Mild, Almindelig, Stærk: ", brugerensValgListe, kaffeStyrkeListe)

# Brugeren vælger størrelse
valgTrin("Vælg størrelse: Lille, Mellem, Stor: ", brugerensValgListe, kopStørrelseListe)

# Brugeren vælger type
valgTrin("Vælg type: Kaffe, Capuccino, Espresso: ", brugerensValgListe, kaffeTypeListe)

# Udskriver til sidst brugerens valg
print("Du har valgt en: " + brugerensValgListe[1].lower() + ", " + brugerensValgListe[0].lower() + " " + brugerensValgListe[2].lower())