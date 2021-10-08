
#


def getPos():
    try:
        while True:
            x = int(input("Indtast x position: \n"))
            if x > 10:
                print("Dit x kordinat er ikke gyldig.")
            else:
                break

        while True:
            y = int(input("Indtast y position: \n"))
            if y > 10:
                print("Dit y kordinat er ikke gyldig.")
            else:
                break
    except:
        print("Fejl. Input skal være tal.\n")
        getPos()


    position = [x,y]
    return position


def main():
    print("Velkommen til Sænkeslagskibe" )

    x, y = getPos()

    print(str(x), "Dette er din x Koordinat, " + str(y), "Dette er din y Koordinat \n Angrib dette punkt")

    print('(' + str(x)+',' + str(y) + ')')

main()
