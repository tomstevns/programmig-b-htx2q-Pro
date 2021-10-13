import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

#instanciate an object me
me = Object()
#Add an attribute name to the object me
me.name = "Frederik"
#Add an attribute age to the object me
me.age = 53
#instanciate an inner-object dog to the object me
me.dog = Object()
#Add an attribute name to the object me
me.dog.name = "Grace"
#Add an attribute purebredNname to the object me
me.dog.purebredName = "Border Collie"
#Place two empty lines
print("\n\n")
#Print the Object me into as a JSON format
print("Print the Object me in JSON format\n\n",me.toJSON())
#Print Content of the Object me
print("[Print the attributes of Object me]\n","me.name = ",me.name,"\n","me.age = ",me.age)
#Print the attributes of inner-Object dog
print("[Print the attribute of inner-Object dog]\n","me.dog.name = ", me.dog.name,"\n","me.dog.purebredName = ", me.dog.purebredName, "\n")

f = open("serializedMessageFile.txt", "w")
f.flush()
f.write(me.toJSON())
f.close()
