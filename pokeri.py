import random


def luoPakka():
    numerot = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    maat = ["pata", "risti", "ruutu", "hertta"]
    pakka = []
    i = 0
    j = 0
    while True:
        pakka += [(numerot[i], maat[j])]
        i += 1
        if i == 13:
            j += 1
            i = 0
            if j == 4:
                break
    return pakka


def onkoVari(kasi):
    tarkasteltavakortti = kasi[0]
    maa = tarkasteltavakortti[1]
    palautettava = False
    for x in kasi:
        if maa == x[1]:
            palautettava = True
        else:
            palautettava = False
            break
    return palautettava


def onkoSuora(kasi):
    kortti = kasi[0]
    kn = kortti[0]
    palautettava = False

    for i in range (1, 5):
        seuraavakortti = kasi[i]
        if kn + 1 == seuraavakortti[0]:
            palautettava = True
        else:
            palautettava = False
            break
    if kn == 1:
        kn = 14
        for i in range(1, 5):
            seuraavakortti = kasi[i]
            if kn + 1 == seuraavakortti[0]:
                palautettava = True
            else:
                palautettava = False
                break
    return palautettava


def onkoKaksiparia(kasi):
    palautettava = False
    kortti1 = kasi[0]
    kn1 = kortti1[0]
    kortti2 = kasi[1]
    kn2 = kortti2[0]
    kortti3 = kasi[2]
    kn3 = kortti3[0]
    kortti4 = kasi[3]
    kn4 = kortti4[0]
    kortti5 = kasi[4]
    kn5 = kortti5[0]
    if kn1 == kn2 and kn3 != kn2:
        if kn3 == kn4 and kn4 != kn5:
            palautettava = True
        elif kn4 == kn5 and kn4 != kn3:
            palautettava = True
    if kn1 != kn2:
        if kn2 == kn3 and kn3 != kn4 and kn4 == kn5:
            palautettava = True
    return palautettava


def numeroidenMuunto(kasi):
    for i in range(0, 5):
        kortti = kasi[i]
        kn = kortti[0]
        if kn == 1:
            kn = 'A'
            kasi[i] = (kn, kortti[1])
        elif kn == 11:
            kn = 'J'
            kasi[i] = (kn, kortti[1])
        elif kn == 12:
            kn = 'Q'
            kasi[i] = (kn, kortti[1])
        elif kn == 13:
            kn = 'K'
            kasi[i] = (kn, kortti[1])
    return kasi


pakka = luoPakka()
random.shuffle(pakka)
kasi1 = []
kasi2 = []
kasi3 = []
kadet = [kasi1, kasi2, kasi3]
while len(kasi1) < 5:
    kasi1.append(pakka[0])
    del pakka[0]
    kasi2.append(pakka[0])
    del pakka[0]
    kasi3.append(pakka[0])
    del pakka[0]
pelaajannumero = 1
for x in kadet:
    tulostettava = numeroidenMuunto(x[:])
    print("pelaajan " + str(pelaajannumero) + " kasi: " + str(tulostettava))
    x.sort()
    if onkoVari(x):
        if onkoSuora(x):
            print("pelaajalla " + str(pelaajannumero) + " Varisuora")
        else:
            print("pelaajalla " + str(pelaajannumero) + " Vari")
    elif onkoSuora(x):
        print("pelaajalla " + str(pelaajannumero) + " Suora")
    elif onkoKaksiparia(x):
        print("pelaajalla " + str(pelaajannumero) + " Kaksi paria")
    else:
        print("pelaajalla " + str(pelaajannumero) + " Ei mitaan haetuista")
    pelaajannumero += 1
