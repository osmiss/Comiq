from pokeri import isFlush
from pokeri import isStraight
from pokeri import isTwopair

'''Testataan palauttaako kasien tarkistusfunktiot oikeat arvot valmiiksi maaritellyilla kasilla
'''
straight1 = [(1, "hertta"), (2, "hertta"), (3, "hertta"), (4, "hertta"), (5, "hertta")]
straight2 = [(1, "hertta"), (10, "ruutu"), (11, "pata"), (12, "pata"), (13, "hertta")]
straight3 = [(4, "hertta"), (5, "ruutu"), (6, "pata"), (7, "pata"), (8, "hertta")]
flush = [(4, "hertta"), (6, "hertta"), (8, "hertta"), (10, "hertta"), (11, "hertta")]
twopair1 = [(1, "hertta"), (1, "ruutu"), (7, "hertta"), (7, "risti"), (9, "hertta")]
twopair2 = [(5, "ruutu"), (5, "hertta"), (6, "pata"), (11, "hertta"), (11, "pata")]
twopair3 = [(6, "pata"), (9, "hertta"), (9, "risti"), (13, "pata"), (13, "hertta")]
randomhand = [(4, "hertta"), (7, "pata"), (9, "ruutu"), (12, "risti"), (13, "pata")]
print("Kaksien parien testaus, pitaisi tulla 3 ensimmaista True ja lopuista False")
print(isTwopair(twopair1))
print(isTwopair(twopair2))
print(isTwopair(twopair3))
print(isTwopair(straight1))
print(isTwopair(straight2))
print(isTwopair(straight3))
print(isTwopair(flush))
print(isTwopair(randomhand))
print("Varien testaus, pitaisi tulla ensimmaisesta kahdesta True ja lopuista False")
print(isFlush(straight1))
print(isFlush(flush))
print(isFlush(straight2))
print(isFlush(straight3))
print(isFlush(twopair1))
print(isFlush(twopair2))
print(isFlush(twopair3))
print(isFlush(randomhand))
print("Suorien testaus, pitaisi tulla ensimmaisesta kolmesta True ja lopuista False")
print(isStraight(straight1))
print(isStraight(straight2))
print(isStraight(straight3))
print(isStraight(flush))
print(isStraight(twopair1))
print(isStraight(twopair2))
print(isStraight(twopair3))
print(isStraight(randomhand))
print("Varisuorien testaus, pitaisi tulla ensimmainen True ja loput False")
print(isFlush(straight1) and isStraight(straight1))
print(isStraight(straight2) and isFlush(straight2))
print(isStraight(straight3) and isFlush(straight3))
print(isFlush(flush) and isStraight(flush))
print(isFlush(twopair1) and isStraight(twopair1))
print(isFlush(twopair2) and isStraight(twopair2))
print(isFlush(twopair3) and isStraight(twopair3))
print(isFlush(randomhand) and isStraight(randomhand))
