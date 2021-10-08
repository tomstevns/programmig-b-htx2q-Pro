
def getPos():
    x = int(input("Indtast x position: \n"))
    y = int(input("Indtast y position: \n"))
    position = [x,y]
    return position

def main():
    print("Velkommen til Sænkeslagskibe" )


    x, y = getPos()

    print(str(x),"Dette er din x Koordinat, " + str(y),"Dette er din y Koordinat \n Angrib dette punkt")

    print(x , y)

main()
