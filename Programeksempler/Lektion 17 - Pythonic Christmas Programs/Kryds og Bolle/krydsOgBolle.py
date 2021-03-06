""" Find fem fejl i Kryds og Bolle programmet
***************************************************************************
***     Læs venligst det hele før du går i gang med at løse opgaven     ***
***************************************************************************

I denne opgave skal du arbejde med søg og erstat funktionen i PyCharm.
Jeg har ændret fem væsentlige syntakser i koden som du nu skal søge og erstatte på.
Start med at læse koden og se om du kan finde de 5 fejl.
En god hjælp er at føre musen henover de steder som er understreget med rødt,
her får du nemlig et hint om hvad der er galt i koden.

***   Sådan kan du udføre SØG og ERSTAT lettest som beskrevet nedenfor! ***

"Søg og erstat" funktionen fremkommer ved  at trykke på CTRL knappen sammen med R(CTRL+R)
Nu vises to forstørrelsesglas øverst.

    1.    I det øverste indsættes de karakterer du ønsker at ændre
    2.    I det nederste indsættes de karakterer du ønsker at erstatte
    3.    Herefter skal du klikke på "Replace All"

    4.    Du kan nu starte med at overveje om // er korrekt notation i Python som er den først af de fem fejl
"""

import random


board=[i for i in range(0,9)]
player, computer = '',''
# Corners, Center and Others, respectively
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
# Table
tab=range(1,10)
def print_board():
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1:
                end+='---------\n'
        char=' '
        if i in ('X','O') :char=i;
        x+=1
        print(char,end=end)
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[-1]
    return chars
def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False
def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player:
            places.append(x)
            x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win
def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)
# AI goes here
def computer_move():
    move=-1
    # if I can win, others do not matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
       # if player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)
def space_exist():
    return board.count('X') + board.count('O') != 9
player, computer = select_char()

print('Spiller er [%s] og Computer er [%s]' % (player, computer))
result='%%% Det står lige - ingen vandt ! %%%'
while space_exist():
    print_board()
    print('#Placer dit kryds ! [1-9]  ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Ukorrekt nummer ! Prøv igen !')
        continue
    #
    if won:
        result='*** Tillykke ! Du har vundet ! ***'
        break
    elif computer_move()[1]:
        result='=== Du har tabt ! =='
        break;
print_board()
print(result)
