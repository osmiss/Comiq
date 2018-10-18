import random


class Card(object):
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __lt__(self, other):
        return self.number < other.number

    '''def __str__(self):
        return "(" + self.number + ", " + self.suit + ")"
'''

def makeCard(number, suit):
    card = Card(number, suit)
    return card

'''Metodi, joka muodostaa pakan. Pakka on lista,
jossa kortit ovat Card luokasta muodostettuja object muuttujia'''
def createDeck():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ["pata", "risti", "ruutu", "hertta"]
    deck = []
    i = 0
    j = 0
    while True:
        deck.append(makeCard(numbers[i], suits[j]))
        i += 1
        if i == 13:
            j += 1
            i = 0
            if j == 4:
                break
    return deck


def isFlush(hand):             # Metodi, joka tarkistaa kadesta mahdollisen varin. Saa parametrina tarkasteltavan kaden
    firstcard = hand[0]
    suit = firstcard.suit
    returnable = False
    for x in hand:
        if suit == x.suit:
            returnable = True
        else:
            returnable = False
            break
    return returnable


def isStraight(hand):          # Metodi, joka tarkistaa kadesta mahdollisen suoran. Saa parametrina tarkasteltavan kaden
    card = hand[0]
    cardnumber = card.number
    card2 = hand[1]
    nextcardnumber = card2.number
    returnable = False
    if cardnumber == 1 and nextcardnumber != 2:
        cardnumber = 14
        newcard = makeCard(cardnumber, card.suit)
        del hand[0]
        hand.append(newcard)
        card = hand[0]
        cardnumber = card.number
        for i in range(1, 5):
            nextcard = hand[i]
            if cardnumber + 1 == nextcard.number:
                returnable = True
                cardnumber += 1
            else:
                returnable = False
                break
    else:
        for i in range(1, 5):
            nextcard = hand[i]
            if cardnumber + 1 == nextcard.number:
                returnable = True
                cardnumber += 1
            else:
                returnable = False
                break
    return returnable


def isTwopair(hand):  # Metodi, joka tarkistaa kadesta mahdollisen kaksi pari. Saa parametrina tarkasteltavan kaden
    returnable = False
    card1 = hand[0]
    cardnumber1 = card1.number
    card2 = hand[1]
    cardnumber2 = card2.number
    card3 = hand[2]
    cardnumber3 = card3.number
    card4 = hand[3]
    cardnumber4 = card4.number
    card5 = hand[4]
    cardnumber5 = card5.number
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
    for i in range(0, 4):
        card = hand[i]
        cardnumber = card.number
        if cardnumber == 1:
            cardnumber = 'A'
            hand[i] = makeCard(cardnumber, card.suit)
        elif cardnumber == 11:
            cardnumber = 'J'
            hand[i] = makeCard(cardnumber, card.suit)
        elif cardnumber == 12:
            cardnumber = 'Q'
            hand[i] = makeCard(cardnumber, card.suit)
        elif cardnumber == 13:
            cardnumber = 'K'
            hand[i] = makeCard(cardnumber, card.suit)
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


def checkHand(hand):
    # Jarjestetaan kadet jarjestykseen pienimmasta suurimpaan kasien tarkistuksen helpottamiseksi
    sortedhand = sorted(hand)
    for i in range(0, len(hand)):           # Kasien tarkistus, joka palauttaa etsityn kaden tai "ei mitaan haetuista"
        if isFlush(sortedhand):
            if isStraight(sortedhand):
                return "Varisuora"
            else:
                return "Vari"
        elif isTwopair(sortedhand):
            return "Kaksi paria"
        elif isStraight(sortedhand):
            return "Suora"
        else:
            return "Ei mitaan haetuista"


def printResults(hands):
    results = []
    for i in range(0, len(hands)):
        result = checkHand(hands[i])
        results.append(result)
    playernumber = 1
    handswithletters = []
    for k in range(0, len(hands)):
        hand = numberToletter(hands[k])
        handswithletters.append(hand)
    for l in range(0, len(hands)):
        handtobeprint = handswithletters[l]
        print("Pelaajalla " + str(playernumber) + " kasi: " +
              str((handtobeprint[0].number, handtobeprint[0].suit)) +
              str((handtobeprint[1].number, handtobeprint[1].suit)) +
              str((handtobeprint[2].number, handtobeprint[2].suit)) +
              str((handtobeprint[3].number, handtobeprint[3].suit)) +
              str((handtobeprint[4].number, handtobeprint[4].suit)))
        playernumber += 1
    playernumber = 1
    for j in range(0, len(results)):
        print("Pelaajalla " + str(playernumber) + ": " + results[j])
        playernumber += 1


def start():
    deck = createDeck()  # Ohjelman alku, josta kutsutaan pakan muodostavaa metodia
    random.shuffle(deck)  # Pakan sekoitus
    hands = deal(deck)
    printResults(hands)


if __name__ == "__main__":
    start()
