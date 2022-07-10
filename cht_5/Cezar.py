#coci17c1p1

cards = [0,0,4,4,4,4,4,4,4,4,12,4]

the_draw = [0,0,0,0,0,0,0,0,0,0,0,0]


cards_drawn = int(input())

max_allowed = 21
for i in range(cards_drawn):
    card = int(input())
    cards[card] -= 1
    max_allowed -= card

max_allowed = max_allowed+1

if sum(cards[:max_allowed])>sum(cards[max_allowed:]):
    print('VUCI')
else:
    print('DOSTA')



