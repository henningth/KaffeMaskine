# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 09:11:44 2018

Dette program modellerer funktionaliteten af en kaffemaskine.
Brugeren kan vælge mellem tre typer kaffe, tre størrelser og tre styrker.
Hvis brugeren indtaster et ugyldigt valg, afsluttes programmet.

@author: HTH
"""

# Definerer variable
kaffeStyrkeListe = ["Mild", "Almindelig", "Stærk"]
kopStørrelseListe = ["Lille", "Mellem", "Stor"]
kaffeTypeListe = ["Kaffe", "Capuccino", "Espresso"]

# Brugerens valg bliver gemt i en liste
brugerensValg = []

# Brugeren vælger styrke
styrke = input("Vælg styrke: Mild, Almindelig, Stærk: ")
størrelse = input("Vælg størrelse: Lille, Mellem, Stor: ")
kaffeType = input("Vælg type: Kaffe, Capuccino, Espresso: ")

# Konverterer valg til tekst kun med små bogstaver
styrke = styrke.title()
størrelse = størrelse.title()
kaffeType = kaffeType.title()

# Matcher brugerens valg af styrke med mulige valg
if styrke == kaffeStyrkeListe[0]: # Mild
    brugerensValg.append(styrke)
elif styrke == kaffeStyrkeListe[1]: # Almindelig
    brugerensValg.append(styrke)
elif styrke == kaffeStyrkeListe[2]: # Stærk
    brugerensValg.append(styrke)
else:
    print("Ugyldigt valg af styrke")
    exit()
    
# Matcher brugerens valg af størrelse med mulige valg
if størrelse == kopStørrelseListe[0]: # Lille
    brugerensValg.append(størrelse)
elif størrelse == kopStørrelseListe[1]: # Mellem
    brugerensValg.append(størrelse)
elif størrelse == kopStørrelseListe[2]: # Stor
    brugerensValg.append(størrelse)
else:
    print("Ugyldigt valg af størrelse")
    exit()
    
# Matcher brugerens valg af størrelse med mulige valg
if kaffeType == kaffeTypeListe[0]: # Kaffe
    brugerensValg.append(kaffeType)
elif kaffeType == kaffeTypeListe[1]: # Capuccino
    brugerensValg.append(kaffeType)
elif kaffeType == kaffeTypeListe[2]: # Espresso
    brugerensValg.append(kaffeType)
else:
    print("Ugyldigt valg af kafftype")
    exit()
    
# Udskriver til sidst brugerens valg
print("Du har valgt en: " + brugerensValg[1] + " " + brugerensValg[0] + " " + brugerensValg[2])