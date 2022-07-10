#coci17c1p1

cards = [0,0,4,4,4,4,4,4,4,4,12,4]

the_draw = [0,0,0,0,0,0,0,0,0,0,0,0]


cards_drawn = int(input())

xx = 21
for i in range(cards_drawn):
    card = int(input())
    cards[card] -= 1
    xx -= card

xx = xx+1

if sum(cards[:xx])>sum(cards[xx:]):
    print('VUCI')
else:
    print('DOSTA')



