"""Filerne finde du på GitHub som følger:

https://github.com/tomstevns/programmig-b-htx2q-Pro/tree/master/Programeksempler/Lektion13-Serialisering-Deserialisering



Du skal nu gøre det modsatte af hvad der blev foretaget i den første fil python fil hvor vi serialiserede data

Jeg har fjernet lidt af koden i "TryItYourselvdeSerialiserMSGogÅbenFil.py",

som du selv skal finde ud af at løse.

Svarene på opgaven finder du i "deSerialiserMSGogÅbenFil.py"

De steder hvor der står ***************** skal du selv tilrette python-koden """





#Definer JSON format
import *****

#Åben fil
f = open(****************
# Læs indhold af fil
jsonBesked = f.************
#Luk fil
f.*************

# print besked ud på JSON format
# Læg marke til at variablen "jsonBesked" printes ud som et name:value pair
print("jsonBeskeden er:  ", ***********)

#deserialiser fil
besked = json.l******************



#Print den besked som din modspiller har sendt til dig
print("besked er: ", ****************)







#definer indhold af besked
besked = {"alt_vel":True}

#konverter "besked" til et JSON format
jsonBesked = json.dumps(besked)


#Gem jsonBesked i en fil



