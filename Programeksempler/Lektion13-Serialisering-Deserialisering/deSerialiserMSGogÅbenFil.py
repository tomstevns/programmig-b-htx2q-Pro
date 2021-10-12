"""Du skal nu gøre det modsatte af hvad der blev foretaget i den
første fil python fil hvor vi serialiserede data"""

#Definer JSON format
import json

#Åben fil
f = open("serializedMessageFile.txt", "r")
# Læs indhold af fil
jsonBesked = f.read()
#Luk fil
f.close()

# print besked ud på JSON format
# Læg marke til at variablen "jsonBesked" printes ud som et name:value pair
print("jsonBeskeden er:  ", jsonBesked)

#deserialiser fil
besked = json.loads(jsonBesked)

#Print den besked som din modspiller har sendt til dig
print("besked er: ", besked)







#definer indhold af besked
besked = {"alt_vel":True}

#konverter "besked" til et JSON format
jsonBesked = json.dumps(besked)


#Gem jsonBesked i en fil



