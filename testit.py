from pokeri import checkHand
from pokeri import makeCard
from pokeri import printResults
'''Testataan palauttaako kasien tarkistusfunktiot oikeat arvot valmiiksi maaritellyilla kasilla
'''

straight1 = [makeCard(1, "hertta"), makeCard(2, "hertta"), makeCard(3, "hertta"), makeCard(4, "hertta"),
             makeCard(5, "hertta")]
straight2 = [makeCard(1, "hertta"), makeCard(10, "ruutu"), makeCard(11, "pata"), makeCard(12, "pata"),
             makeCard(13, "hertta")]
straight3 = [makeCard(4, "hertta"), makeCard(5, "ruutu"), makeCard(6, "pata"), makeCard(7, "pata"),
             makeCard(8, "hertta")]
flush = [makeCard(4, "hertta"), makeCard(6, "hertta"), makeCard(8, "hertta"), makeCard(10, "hertta"),
         makeCard(11, "hertta")]
twopair1 = [makeCard(1, "hertta"), makeCard(1, "ruutu"), makeCard(7, "hertta"), makeCard(7, "risti"),
            makeCard(9, "hertta")]
twopair2 = [makeCard(5, "ruutu"), makeCard(5, "hertta"), makeCard(6, "pata"), makeCard(11, "hertta"),
            makeCard(11, "pata")]
twopair3 = [makeCard(6, "pata"), makeCard(9, "hertta"), makeCard(9, "risti"), makeCard(13, "pata"),
            makeCard(13, "hertta")]
randomhand = [makeCard(4, "hertta"), makeCard(7, "pata"), makeCard(9, "ruutu"), makeCard(12, "risti"),
              makeCard(13, "pata")]
hands = [straight1, straight2, straight3, flush, twopair1, twopair2, twopair3, randomhand]
results = []
for y in hands:
    results.append(checkHand(y))
printResults(hands)
print(results)
