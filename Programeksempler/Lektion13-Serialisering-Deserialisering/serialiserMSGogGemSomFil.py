#Definer JSON format
import json

#definer indhold af besked
besked = {"alt_vel":True}

#konverter "besked" til et JSON format
jsonBesked = json.dumps(besked)

# print besked ud på JSON format
# Læg marke til at variablen "jsonBesked" printes ud som et name:value pair
print("jsonBesked: ", jsonBesked)

#Gem jsonBesked i en fil

f = open("serializedMessageFile.txt", "a")

f.write(jsonBesked)
f.close()



