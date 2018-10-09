# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:13:07 2018

Dette program modellerer funktionaliteten af en kaffemaskine.
Brugeren kan vælge mellem tre typer kaffe, tre størrelser og tre styrker.
Denne udgave tager højde for forkert valg fra brugerens side via et while loop.

@author: HTH
"""

# Definerer variable
kaffeStyrkeListe = ["Mild", "Almindelig", "Stærk"]
kopStørrelseListe = ["Lille", "Mellem", "Stor"]
kaffeTypeListe = ["Kaffe", "Capuccino", "Espresso"]

# Brugerens valg bliver gemt i en liste
brugerensValg = []

###############################################################################
# Brugeren vælger styrke
while True:    
    styrke = input("Vælg styrke: Mild, Almindelig, Stærk: ")
    styrke = styrke.title()
    
    # Matcher brugerens valg af styrke med mulige valg
    if styrke == kaffeStyrkeListe[0]: # Mild
        brugerensValg.append(styrke)
        break
    elif styrke == kaffeStyrkeListe[1]: # Almindelig
        brugerensValg.append(styrke)
        break
    elif styrke == kaffeStyrkeListe[2]: # Stærk
        brugerensValg.append(styrke)
        break
    else:
        print("\nUgyldigt valg af styrke.")
    
###############################################################################
# Brugeren vælger størrelse
while True:
    størrelse = input("Vælg størrelse: Lille, Mellem, Stor: ")
    størrelse = størrelse.title()

    # Matcher brugerens valg af størrelse med mulige valg
    if størrelse == kopStørrelseListe[0]: # Lille
        brugerensValg.append(størrelse)
        break
    elif størrelse == kopStørrelseListe[1]: # Mellem
        brugerensValg.append(størrelse)
        break
    elif størrelse == kopStørrelseListe[2]: # Stor
        brugerensValg.append(størrelse)
        break
    else:
        print("\nUgyldigt valg af størrelse.")

###############################################################################
# Brugeren vælger type
while True:
    kaffeType = input("Vælg type: Kaffe, Capuccino, Espresso: ")
    kaffeType = kaffeType.title()
    
    # Matcher brugerens valg af type med mulige valg
    if kaffeType == kaffeTypeListe[0]: # Kaffe
        brugerensValg.append(kaffeType)
        break
    elif kaffeType == kaffeTypeListe[1]: # Capuccino
        brugerensValg.append(kaffeType)
        break
    elif kaffeType == kaffeTypeListe[2]: # Espresso
        brugerensValg.append(kaffeType)
        break
    else:
        print("\nUgyldigt valg af kaffetype.")
    
# Udskriver til sidst brugerens valg
print("Du har valgt en: " + brugerensValg[1].lower() + ", " + brugerensValg[0].lower() + " " + brugerensValg[2].lower())