import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

#Assuming all hands are random and sorted from lowest to highest

class card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        

def hasStraightFlush(hand):
    for i in hand:                                                  #for example, say first card is a 2
        for j in hand:
            if (j.rank==i.rank+1 and i.suit == j.suit):  #check if any of the others is a 3
                for k in hand:
                    if (k.rank == j.rank+1 and i.suit == k.suit):   #if so check for a 4
                        for l in hand:
                            if (l.rank == k.rank+1 and i.suit == l.suit):  #if so check for a 5
                                for m in hand:
                                    if(m.rank == l.rank+1 and i.suit == m.suit):  #if so then you finally have a straight
                                        for n in hand:
                                            if(n.rank ==m.rank+1 and i.suit == n.suit):
                                                for o in hand:
                                                    if (o.rank == n.rank+1 and i.suit == o.suit):
                                                        return [True,o.rank]
                                                return [True, n.rank]
                                        return [True,m.rank]                    #Now we're just checking if there's a higher straight
    return [False,0]
    
def has4OfAKind(hand):
    for i in hand:
        count = 0
        for j in hand:
            if (i.rank == j.rank):  #counts how many of the same card are in the hand, note, when i = j you are comparing
                count+=1            #a card against ITSELF but that's okay because there is always at least one of each card
            if count == 4:
                return [True, i.rank]
    return [False, 0]

def has3OfAKind(hand):
    for i in hand:
        count = 0
        for j in hand:
            if (i.rank == j.rank):
                count+=1 
            if count == 3:
                return [True, i.rank]
    return [False, 0]

def hasFullHouse(hand):
    set3Rank = 20   #arbitrary number that can't be confused with a card rank
    breakit = False   #This is purely to simplify breaking out of a nested loop a few lines down
    for i in hand:
        count = 0
        for j in hand:
            if (i.rank == j.rank):
                count+=1 
            if count == 3:
                set3Rank = i.rank
                breakit = True
                break
        if breakit:
            break
    if not breakit:   #if the whole nested loop ran and there is no set of 3, there is no full house
        return [False, 0,0]
    for l in hand:
        if l.rank != set3Rank:  #this avoids re-counting the set of 3
            count = 0
            for m in hand:
                if l.rank == m.rank:
                    count+=1
                if count == 2:
                    return [True, set3Rank, m.rank]
    return [False, 0,0]
    
def hasFlush(hand):
    for i in hand:
        count = 0
        maxRank = i.rank
        for j in hand:
            if (i.suit == j.suit):
                count+=1 
                if j.rank > maxRank:
                    maxRank = j.rank
            if count == 5:
                return [True, maxRank]
    return [False, 0]
    
def hasStraight(hand):  #remember to account for Ace being high and low for straights
    for i in hand:  #for example, say first card is a 2
        for j in hand:
            if (j.rank==i.rank+1):             #check if any of the others is a 3
                for k in hand:
                    if (k.rank == j.rank+1):   #if so check for a 4
                        for l in hand:
                            if (l.rank == k.rank+1):  #if so check for a 5
                                for m in hand:
                                    if(m.rank == l.rank+1):  #if so then you finally have a straight
                                        for n in hand:
                                            if(n.rank ==m.rank+1):
                                                for o in hand:
                                                    if (o.rank == n.rank+1):
                                                        return [True,o.rank]
                                                return [True, n.rank]
                                        return [True,m.rank]                    #Now we're just checking if there's a higher straight
    return [False,0]
    
def has2Pair(hand):
    setRank = 20   #arbitrary number that can't be confused with a card rank
    breakit = False   #This is purely to simplify breaking out of a nested loop a few lines down
    for i in hand:
        count = 0
        for j in hand:
            if (i.rank == j.rank):
                count+=1 
            if count == 2:
                setRank = i.rank
                breakit = True
                break
        if breakit:
            break
    if not breakit:   #if the whole nested loop ran and there is no set of 3, there is no full house
        return [False,0,0]
    for l in hand:
        if l.rank != setRank:  #this avoids re-counting the set of 3
            count = 0
            for m in hand:
                if l.rank == m.rank:
                    count+=1
                if count == 2:
                    return [True, setRank, m.rank]
    return [False, 0, 0]
    
def hasPair(hand):
    for i in hand:
        count = 0
        for j in hand:
            if (i.rank == j.rank):
                count+=1 
            if count == 2:
                return [True,j.rank]
    return [False,0]

    
def win(hand1,hand2):  #returns 1 if hand1 beats hand2, -1 if hand2 beats hand1, and 0 if they split the pot
    x = hasStraightFlush(hand1)[0]
    y = hasStraightFlush(hand2)[0]
    if (x or y):
        if(x and y):
            if(hasStraightFlush(hand1)[1] > hasStraightFlush(hand2)[1]):
                return 1
            elif(hasStraightFlush(hand1)[1] < hasStraightFlush(hand2)[1]):
                return -1
            else:
                return 0
        elif(x):
            return 1
        elif(y):
            return -1
    x = has4OfAKind(hand1)[0]
    y = has4OfAKind(hand2)[0]
    if (x or y):
        if(x and y):
            if(has4OfAKind(hand1)[1] > has4OfAKind(hand2)[1]):
                return 1
            elif(has4OfAKind(hand1)[1] < has4OfAKind(hand2)[1]):
                return -1
            else:
                return 0
        elif(x):
            return 1
        elif(y):
            return -1
    x = hasFullHouse(hand1)[0]
    y = hasFullHouse(hand2)[0]
    if (x or y):
        if(x and y):
            if(hasFullHouse(hand1)[1] > hasFullHouse(hand2)[1]):
                return 1
            elif(hasFullHouse(hand1)[1] < hasFullHouse(hand2)[1]):
                return -1
            elif(hasFullHouse(hand1)[2] > hasFullHouse(hand2)[2]):
                return 1
            elif(hasFullHouse(hand1)[2] < hasFullHouse(hand2)[2]):
                return -1
            else:
                return 0
        elif(x):
            return 1
        elif(y):
            return -1
    x = hasFlush(hand1)[0]
    y = hasFlush(hand2)[0]
    if (x or y):
        if(x and y):
            if(hasFlush(hand1)[1] > hasFlush(hand2)[1]):
                return 1
            elif(hasFlush(hand1)[1] < hasFlush(hand2)[1]):
                return -1
            else:
                return 0      #If 2 players have a flush with the same high card, it would then go to the second highest card, but this is such an unlikely edge case that it is negligible
        elif(x):
            return 1
        elif(y):
            return -1
    x = hasStraight(hand1)[0]
    y = hasStraight(hand2)[0]
    if (x or y):
        
        if(x and y):
            if(hasStraight(hand1)[1] > hasStraight(hand2)[1]):
                return 1
            if (hasStraight(hand1)[1] < hasStraight(hand2)[1]):
                return -1
            else:
                return 0  
        elif(x):
            return 1
        elif(y):
            return -1
    x = has3OfAKind(hand1)[0]
    y = has3OfAKind(hand2)[0]
    if (x or y):
        if(x and y):
            if(has3OfAKind(hand1)[1] > has3OfAKind(hand2)[1]):
                return 1
            elif(has3OfAKind(hand1)[1] < has3OfAKind(hand2)[1]):
                return -1
            elif ((hand1[0].rank > hand2[0].rank and hand1[0].rank > hand2[1].rank) or (hand1[1].rank>hand2[0].rank and hand1[1].rank > hand2[1].rank)):
                return 1
            elif ((hand2[0].rank > hand1[0].rank and hand2[0].rank > hand1[1].rank) or (hand2[1].rank>hand1[0].rank and hand2[1].rank > hand1[1].rank)):
                return -1
            elif ((hand1[0].rank > hand2[0].rank or hand1[0].rank > hand2[1].rank) and (hand1[1].rank>hand2[0].rank or hand1[1].rank > hand2[1].rank)):
                return 1
            elif ((hand2[0].rank > hand1[0].rank or hand2[0].rank > hand1[1].rank) and (hand2[1].rank>hand1[0].rank or hand2[1].rank > hand1[1].rank)):
                return -1
            else:
                return 0 
        elif(x):
            return 1
        elif(y):
            return -1
    x = has2Pair(hand1)[0]
    y = has2Pair(hand2)[0]
    if (x or y):
        if(x and y):
             if(has2Pair(hand1)[1] > has2Pair(hand2)[1]):
                return 1
             elif(has2Pair(hand1)[1] < has2Pair(hand2)[1]):
                return -1
             else:
                if(has2Pair(hand1)[2] > has2Pair(hand2)[2]):
                    return 1
                elif(has2Pair(hand1)[2] < has2Pair(hand2)[2]):
                    return -1
                else:
                    max1 = 0
                    max2 = 0
                    for i in hand1:
                        if (i.rank != has2Pair(hand1)[1] and i.rank != has2Pair(hand1)[2]):
                            if i.rank > max1:
                                max1 = i.rank
                    for j in hand2:
                        if (j.rank != has2Pair(hand2)[1] and j.rank != has2Pair(hand2)[2]):
                            if j.rank > max2:
                                max2 = j.rank
                    if max1 > max2:
                        return 1
                    if max1 < max2:
                        return -1
                    else:
                        return 0
        elif(x):
            return 1
        elif(y):
            return -1
    x = hasPair(hand1)[0]
    y = hasPair(hand2)[0]
    if (x or y):
        if(x and y):
            if(hasPair(hand1)[1] > hasPair(hand2)[1]):
                return 1
            elif(hasPair(hand1)[1] < hasPair(hand2)[1]):
                return -1
            elif ((hand1[0].rank > hand2[0].rank and hand1[0].rank > hand2[1].rank) or (hand1[1].rank>hand2[0].rank and hand1[1].rank > hand2[1].rank)):
                return 1
            elif ((hand2[0].rank > hand1[0].rank and hand2[0].rank > hand1[1].rank) or (hand2[1].rank>hand1[0].rank and hand2[1].rank > hand1[1].rank)):
                return -1
            else:
                """for i in hand1:
                    print(i.rank,end = " ")
                print()
                for j in hand2:
                    print(j.rank, end = " ")
                print('pair')"""
                return 0
        elif(x):
            return 1
        elif(y):
            return -1          #Now compare high card, the first two elements are the only different ones, so they are all we need to compare
    if ((hand1[0].rank > hand2[0].rank and hand1[0].rank > hand2[1].rank) or (hand1[1].rank>hand2[0].rank and hand1[1].rank > hand2[1].rank)):
        return 1
    elif ((hand2[0].rank > hand1[0].rank and hand2[0].rank > hand1[1].rank) or (hand2[1].rank>hand1[0].rank and hand2[1].rank > hand1[1].rank)):
        return -1
    else:
        return 0

testHand1 = [card(2,3),card(7,3),card(3,3),card(4,2),card(4,3),card(5,3),card(6,3)]
testHand2 = [card(2,2),card(2,2),card(2,2),card(2,2),card(6,2),card(7,2),card(8,2)]
testHand3 = [card(2,3),card(4,3),card(5,3),card(7,2),card(8,2),card(10,2),card(13,2)]

MY_HAND = [card(6,1),card(5,1)]

def generateDeck(my_hand = MY_HAND): #To avoid the possibility of having duplicate cards from the get-go, I'm making a 50 card deck that doesn't include MY_HAND
    deck = []
    for i in range(13):
        for j in range(4):
            if ((my_hand[0].rank == i + 2 and my_hand[0].suit == j+1) or (my_hand[1].rank == i+2 and my_hand[1].suit == j+1)):
                continue
            else:
                deck.append(card(i+2,j+1))
    return deck

def generateHands(deck,my_hand = MY_HAND):
    hand1 = my_hand
    hand2 = []
    flop = []
    for i in range(5):
        flop.append(deck.pop(np.random.randint(0,len(deck))))    #deck.pop() is perfect because it returns the value at deck[n] and deletes it from deck, so you don't have any repeated cards
    for i in range(2):
        hand2.append(deck.pop(np.random.randint(0,len(deck))))
    hand1 = hand1 + flop
    hand2 = hand2 + flop
    return hand1,hand2

"""
hand1, hand2 = generateHands(generateDeck())
temp = win(hand1,hand2)
print(temp)
for i in hand1:
    print(i.rank,end = " ")
print()
for j in hand2:
    print(j.rank, end = " ")
"""

trials = []

for j in range(10):
    wins = 0
    losses = 0
    ties = 0
    for i in range(5000):
        hand1, hand2 = generateHands(generateDeck())
        temp = win(hand1,hand2)
        if temp == 1:
            wins += 1
        elif temp == -1:
            losses += 1
        elif temp == 0:
            ties += 1
    trials.append(wins/(wins+losses))

plt.hist(trials)

print(wins,losses,ties)
print(sp.mean(trials))
