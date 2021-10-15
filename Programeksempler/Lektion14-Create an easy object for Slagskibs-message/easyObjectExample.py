import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)



j =""
class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)




#instanciate an object me
me = Object()
#Add an attribute name to the object me
me.name = "Frederik"
#Add an attribute age to the object me
me.mesage = "hej"
#instanciate an inner-object dog to the object me

#Place two empty lines
print("\n\n")
#Print the Object me into as a JSON format

print("me as python")
print(me)
print("Print the Object me in JSON format\n\n",me.toJSON())
#Print Content of the Object me
print("[Print the attributes of Object me]\n","me.name = ",me.name,"\n","me.age = ",me.age)
#Print the attributes of inner-Object dog
print("[Print the attribute of inner-Object dog]\n","me.dog.name = ", me.dog.name,"\n","me.dog.purebredName = ", me.dog.purebredName, "\n")

f = open("serializedMessageFile.txt", "w")
f.flush()
f.write(me.toJSON())
f.close()

#Nu lad vi som om at filen er blevet sendt til en modtagers outlook og gemt i en folder

#Modtager åbner og læser indholdet i filen på JSON format
print("[Denne del af programmet kører normalt i modtagerens deSerialiserings program]")
f = open("serializedMessageFile.txt", "r")
filensTxtpåJSONformat = f.read()
print("printer filens indhold i JSON format","\n\n",filensTxtpåJSONformat)
modtMe = Object.toPython(filensTxtpåJSONformat)

print(modtMe)

"""#Print Content of the Object me
print("[Print the attributes of Objec me]\n","modtMe.name = ",modtMe.name,"\n","modtMe.age = ",modtMe.age)
#Print the attributes of inner-Object dog
print("[Print the attribute of inner-Object dog]\n","modtMe.dog.name = ", modtMe.dog.name,"\n","modtMe.dog.purebredName = ", modtMe.dog.purebredName, "\n")
"""

