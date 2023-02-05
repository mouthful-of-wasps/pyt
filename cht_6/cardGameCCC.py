card_values = {
    'two'   :2, 
    'three' :3,
    'four'  :4,
    'five'  :5,
    'six'   :6,
    'seven' :7,
    'eight' :8,
    'nine'  :9,
    'ten'   :10,
    'jack'  :11,
    'queen' :12,
    'king'  :13,
    'ace'   :14
}

cards = []

f=open("cards.txt",'r')

for i in range(52):
    card = f.readline().strip('\n')
    cards.append(card_values[card])

f.close()


#for i in range(52):
   # cards.append(card_values[input()])

playerA=0
playerB=0
high = 10
for i in range(51):
    m = cards[i] - high 
    tjek = []
    if m>0:
   #     print(i+m)
        if i + m <= 51:
            
            for ii in range(m):
           #     print(f'i {i}, m {m}, ii {ii}, {cards[i+ii+1]}')
                tjek.append(cards[i+ii+1])
                
               # print(tjek)
            if max(tjek) <= high:
                if i%2 == 0:
                    playerA += m
                    print(f'Player A scores {m} point(s).')
                else:
                    playerB += m
                    print(f'Player B scores {m} point(s).') 

print(f'Player A: {playerA} point(s).')
print(f'Player B: {playerB} point(s).')