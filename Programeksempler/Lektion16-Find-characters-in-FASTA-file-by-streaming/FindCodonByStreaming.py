# Som tekst
import re
import os

def onlyATGC(file):
    if os.path.exists(file):
        f = open(file, "r")
        combinedline = ""
        for i in f.readlines():
            if i[0] != ">":
                combinedline += re.sub('[^ATCG]', '', i)
        return combinedline
    else:
        return False


def antalCodonIString(codon, string):
    antal = 0
    if type(codon) == list:
        for i in codon:
            antal += string.count(i)
    else:
        antal += string.count(codon)
    print("Antal", codon, "=", antal)
    return antal
# En codon
codon = "ATG"
antalCodonIString(codon, onlyATGC("opgave2.fasta"))

# Flere codon
codon = ["TGA", "TAG", "TAA"]
antalCodonIString(codon, onlyATGC("opgave2.fasta"))
