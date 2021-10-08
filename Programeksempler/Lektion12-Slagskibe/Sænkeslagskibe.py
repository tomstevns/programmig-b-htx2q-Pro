import random


spilleplade = []

for x in range(0,11):
  spilleplade.append(["o"] * 11)

def print_spilleplade(spilleplade):
  for row in spilleplade:
    print (" ".join(row))

print("Lad os spille sænke slagskibe!")
print("Der kan kun være 2 spillere med")
print("Den første spiller som bliver valgt har alle de ulige ture og den anden spiller har alle de lige")

player_1 = input("Skriv første spillers navn: ")
player_2 = input("Skriv anden spillers navn: ")
players = [player_1, player_2]

def random_player(players):
    return random.choice(players)

def random_row(spilleplade):
  return random.randint(0,len(spilleplade)-1)

def random_col(spilleplade):
  return random.randint(0,len(spilleplade[0])-1)

if random_player(players) == player_1:
  print(player_1, "Starter først.")
else:
  print(player_2, "Starter først.")

ship_y_1 = random_row(spilleplade)
ship_x_1 = random_col(spilleplade)


ship_y_2 = random_row(spilleplade)
ship_x_2 = random_col(spilleplade)


print_spilleplade(spilleplade)

player_start = random_player(players)



hit_count = 0

for tur in range(6):
     y_variable = int(input("Gæt en y-værdi: (Du kan skrive et tal mellem: 0-10) "))
     x_variable = int(input("Gæt en x-værdi : (Du kan skrive et tal mellem: 0-10) "))

     if (y_variable == ship_y_1 and x_variable == ship_x_1) or (y_variable == ship_y_2 and x_variable == ship_x_2):
            hit_count = hit_count + 1
            spilleplade[y_variable][x_variable] = "*"
            print ("Tillykke! ")
            if hit_count == 1:
                   print("Du sank dit første skib!")
            elif hit_count == 2:
                   print("Du sank dit andet skib! Du vandt!")
                   print_spilleplade(spilleplade)
                   break
     else:
            if (y_variable < 0 or y_variable > 11)  or (x_variable < 0 or x_variable > 11):
                   print ("åhh åhh, det sted er der ikke engang.")
            elif(spilleplade[y_variable][x_variable] == "X"):
                   print ("Det sted har du allerede prøvet at ramme.")
            else:
                 print ("Du ramte forbi mit skib!")
                 spilleplade[y_variable][x_variable] = "X"
            print ("Tur",tur + 1)
     print_spilleplade(spilleplade)
print ("skib 1 er skjult på:")
print (ship_y_1)
print (ship_x_1)

print ("Skib 2 er skjult på :")
print (ship_y_2)
print (ship_x_2)
