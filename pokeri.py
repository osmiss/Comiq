import random


def createDeck():            # Metodi, joka muodostaa pakan. pakka on lista, jossa kortit ovat tuple muotoisia muuttujia
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ["pata", "risti", "ruutu", "hertta"]
    deck = []
    i = 0
    j = 0
    while True:
        deck += [(numbers[i], suits[j])]
        i += 1
        if i == 13:
            j += 1
            i = 0
            if j == 4:
                break
    return deck


def isFlush(hand):             # Metodi, joka tarkistaa kadesta mahdollisen varin. Saa parametrina tarkasteltavan kaden
    firstcard = hand[0]
    suit = firstcard[1]
    returnable = False
    for x in hand:
        if suit == x[1]:
            returnable = True
        else:
            returnable = False
            break
    return returnable


def isStraight(hand):          # Metodi, joka tarkistaa kadesta mahdollisen suoran. Saa parametrina tarkasteltavan kaden
    card = hand[0]
    cardnumber = card[0]
    returnable = False
    for i in range(1, 5):
        nextcard = hand[i]
        if cardnumber + 1 == nextcard[0]:
            returnable = True
        else:
            returnable = False
            break
    if cardnumber == 1:
        cardnumber = 14
        for i in range(1, 5):
            nextcard = hand[i]
            if cardnumber + 1 == nextcard[0]:
                returnable = True
            else:
                returnable = False
                break
    return returnable


def isTwopair(hand):  # Metodi, joka tarkistaa kadesta mahdollisen kaksi pari. Saa parametrina tarkasteltavan kaden
    returnable = False
    card1 = hand[0]
    cardnumber1 = card1[0]
    card2 = hand[1]
    cardnumber2 = card2[0]
    card3 = hand[2]
    cardnumber3 = card3[0]
    card4 = hand[3]
    cardnumber4 = card4[0]
    card5 = hand[4]
    cardnumber5 = card5[0]
    if cardnumber1 == cardnumber2 and cardnumber3 != cardnumber2:
        if cardnumber3 == cardnumber4 and cardnumber4 != cardnumber5:
            returnable = True
        elif cardnumber4 == cardnumber5 and cardnumber4 != cardnumber3:
            returnable = True
    if cardnumber1 != cardnumber2:
        if cardnumber2 == cardnumber3 and cardnumber3 != cardnumber4 and cardnumber4 == cardnumber5:
            returnable = True
    return returnable


def numberToletter(hand):         # Muuntaa assan, kuninkaan, kuningattaren ja jatkan arvon kirjaimeksi tulosteeseen
    for i in range(0, 5):
        card = hand[i]
        cardnumber = card[0]
        if cardnumber == 1:
            cardnumber = 'A'
            hand[i] = (cardnumber, card[1])
        elif cardnumber == 11:
            cardnumber = 'J'
            hand[i] = (cardnumber, card[1])
        elif cardnumber == 12:
            cardnumber = 'Q'
            hand[i] = (cardnumber, card[1])
        elif cardnumber == 13:
            cardnumber = 'K'
            hand[i] = (cardnumber, card[1])
    return hand


def deal(deck):
    hand1 = []
    hand2 = []
    hand3 = []
    hands = [hand1, hand2, hand3]
    while len(hand1) < 5:           # korttien jako pelaajille
        hand1.append(deck[0])
        del deck[0]
        hand2.append(deck[0])
        del deck[0]
        hand3.append(deck[0])
        del deck[0]
    return hands


def checkAndprintcards(hands):
    playernumber = 1
    for x in hands:           # Kasien tulostus ja tarkistus, joka tulostaa joko etsityn kaden tai "ei mitaan haetuista"
        printedhand = numberToletter(x[:])
        print("pelaajan " + str(playernumber) + " hand: " + str(printedhand))
        x.sort()           # Jarjestetaan kadet jarjestykseen pienimmasta suurimpaan kasien tarkistuksen helpottamiseksi
        if isFlush(x):
            if isStraight(x):
                print("pelaajalla " + str(playernumber) + " Varisuora")
            else:
                print("pelaajalla " + str(playernumber) + " Vari")
        elif isStraight(x):
            print("pelaajalla " + str(playernumber) + " Suora")
        elif isTwopair(x):
            print("pelaajalla " + str(playernumber) + " Kaksi paria")
        else:
            print("pelaajalla " + str(playernumber) + " Ei mitaan haetuista")
        playernumber += 1


def start():
    deck = createDeck()  # Ohjelman alku, josta kutsutaan pakan muodostavaa metodia
    random.shuffle(deck)  # Pakan sekoitus
    hands = deal(deck)
    checkAndprintcards(hands)


start()  # Ohjelman kaynnistava komento
