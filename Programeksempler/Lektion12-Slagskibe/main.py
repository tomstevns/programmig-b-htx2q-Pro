#

def checkPos(txt):
    if txt.isnumeric():    # Tjekker om værdien txt er et tal

        if int(txt) < 10:  # Tjekker om at værdien er under 10
            return True
        else:
            return False
    else:
        return False


def getPos():
    while True:
        x = input("Indtast x position: \n")
        if checkPos(x):
            break
        else:
            print("Dit x kordinat er ikke gyldig.")

    while True:
        y = input("Indtast y position: \n")
        if checkPos(y):
            break
        else:
            print("Dit y  kordinat er ikke gyldig.")

    position = [int(x), int(y)]

    return position


def main():
    print("Velkommen til Sænkeslagskibe" )

    x, y = getPos()

    print(str(x), "Dette er din x Koordinat, " + str(y), "Dette er din y Koordinat \n Angrib dette punkt")

    print('(' + str(x)+',' + str(y) + ')')

main()
