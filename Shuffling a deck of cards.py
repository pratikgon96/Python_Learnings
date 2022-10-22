import random
#first make a deck of 13 cards in order
cardfaces = []
deck = []
royals = ['J', 'Q', 'K', 'A']
suits = ['Hearts', 'Spades', 'Club', 'Diamond']


for i in range(2, 11):
    cardfaces.append(str(i))

for j in range(4):
    cardfaces.append(royals[j])


#attach the suits to the 13 cards

for k in range(4):
    for l in range(13):
        cards = (cardfaces[l] + ' of ' + suits[k])

        deck.append(cards)

#shuffle the card
random.shuffle(deck)

for m in range(13):
    print(deck[m])