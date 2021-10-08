
#


def getPos():
    tjek = True
    while tjek:
        x = int(input("Indtast x position: \n"))
        if x > 10:
            print("Dit x kordinat er ikke gyldigt.")
        else:
            tjek = False
    tjek = True
    while tjek:
        y = int(input("Indtast y position: \n"))
        if y > 10:
            print("Dit y kordinat er ikke gyldigt.")
        else:
            tjek = False

    position = [x,y]
    return position

def main():
    print("Velkommen til Sænkeslagskibe" )

    x, y = getPos()

    print(str(x), "Dette er din x Koordinat, " + str(y), "Dette er din y Koordinat \n Angrib dette punkt")

    print('(' + str(x)+',' + str(y) + ')')

main()
