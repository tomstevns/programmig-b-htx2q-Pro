#Opgave 1
#Lav et program som returnerer længden af en streng

def findLængdeAfStreng(inputStreng):
    strengLængde = len(inputStreng)
    return strengLængde
#Test af opgave1
testStreng = "abcdef340958304g"
print("længden af strengen ",testStreng," er ", findLængdeAfStreng(testStreng)," karakterer")
print("længden af strengen ", testStreng," er ",findLængdeAfStreng(testStreng), " karakterer")


#Opgave2
#Lav et program åbner en fil1, skriver "hej med dig" i filen 13153 gange, men den
# 5.158 gang skrives der "farvel med dig"

#Definer og åben en fil
f = open("fil1", "r")

#Lav et loop 13153 gange som skriver
for i in range(13)
    #IF I er 5158 så
    print("I skal nu være 5158")
    #Skrive i filen - "Farvel med dig"
    #Noget med
    f.write("truttelut")
    #ELSE
    #Skrive i filen - "Hej med dig"
    #Noget med
    f.write("vuffelivuf")

#Luk filen fil1



#Opgave3
#Lav et program åbner en fil1,
#Finder rækken hvor der står "farvel med dig" og returnerer række nummeret på rækken


#Opgave4
#Lav et program som kan udskrive et alfabet ved hjælp af ASCII værdier,
# som er tæller i et "While Loop"





