import random
x = 9



taquin = [0,3,5,4,2,1,6,7,8]

taquin2 = taquin.copy()

nbSwap = 0
mouvementPrecedent = 0
plusCourt = []
wtf = []
taillePlusCourt = 1000000000

def legalMoove(tab):
     index = tab.index(0)
     if index == 0:
         return [1,3]
     if index == 1:
         return [-1,3,1]
     if index == 2:
         return [-1,3]
     if index == 3:
         return [-3,1,3]
     if index == 4:
         return  [-3,-1,1,3]
     if index == 5:
         return [-3,-1,3]
     if index == 6:
         return [-3,1]
     if index == 7:
         return [-3,-1,1]
     if index == 8:
         return [-3,-1]

def choixMouvement(list):
    wtf = random.choice(list)
    return wtf

def afficherTaquin(list):
    tab1 = []
    tab2 = []
    tab3 = []
    tab1.append(list[0])
    tab1.append(list[1])
    tab1.append(list[2])
    tab2.append(list[3])
    tab2.append(list[4])
    tab2.append(list[5])
    tab3.append(list[6])
    tab3.append(list[7])
    tab3.append(list[8])
    print(tab1)
    print(tab2)
    print(tab3)
    print()

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def nombreElemOk(list):
    count = 0
    for s in range(0,len(list)):
        if s == list[s]:
            count += 1
    return count

for s in range(0,50000):
    while nombreElemOk(taquin) != 9:
        posX = taquin.index(0)
        mouvementPossible = legalMoove(taquin)
        if nbSwap == 0:
            mouvementChoisi = choixMouvement(mouvementPossible)
        elif nbSwap > 0:
            mouvementPossible.remove(mouvementPrecedent*-1)
            mouvementChoisi = choixMouvement(mouvementPossible)

        plusCourt.append(mouvementChoisi)
        posElementChoisi = posX + mouvementChoisi
        swapPositions(taquin, posX, posElementChoisi)
        mouvementPrecedent = mouvementChoisi
        nbSwap += 1
        if nbSwap > taillePlusCourt:
            break
        if nbSwap > 50:
            break
    if nbSwap < taillePlusCourt:
        print(plusCourt)
        taillePlusCourt = nbSwap
        wtf = []
        wtf = plusCourt.copy()
    else:
        plusCourt = []
    nbSwap = 0
    taquin = taquin2.copy()

print(taillePlusCourt)

