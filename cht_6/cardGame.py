'''
Write a program that will keep score for a simple two-player game, played with a deck of cards. 
There are 52 cards in the deck; four of each of 13 possible names: 
two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace. 
The cards labelled jack, queen, king, and ace are collectively known as high cards.

The deck is shuffled and placed face-down on the table. Player A turns over the top card and places it on a pile; 
then player B turns over the top card and places it on the pile. A and B alternate until the deck is exhausted. The game is scored as follows:

    If a player turns over an ace, with at least 4 cards remaining to be turned over, and none of the next 4 cards is a high card, that player scores 4 points
    If a player turns over a king, with at least 3 cards remaining to be turned over, and none of the next 3 cards is a high card, that player scores 3 points
    If a player turns over a queen, with at least 2 cards remaining to be turned over, and none of the next 2 cards is a high card, that player scores 2 points
    If a player turns over a jack, with at least 1 card remaining to be turned over, and the next card is not a high card, that player scores 1 point

'''
import random

class Deck():
    card_list = []

    def __init__(self):
        self.construct_deck()
        self.shuffle_deck()
    
    def construct_deck(self):
        for ii in range(4):    
            for i in range(1,14):
                self.card_list.append(i+1)

    def shuffle_deck(self):
        random.shuffle(self.card_list)
        self.card_list.insert(0,None)
    
    def __str__(self):
        return ', '.join([str(i) for i in self.card_list])

mitDeck = Deck()

high = 10

playerA = 0
playerB = 0
print(mitDeck)
for i in range(1,51):
    m = mitDeck.card_list[i] - high 
    tjek = []
    if m>0:
        print(i+m)
        if i + m < 52:
            for ii in range(1,m+1):
                tjek.append(mitDeck.card_list[i+ii])
               # print(tjek)
            if max(tjek) < high:
                if i%2 == 1:
                    playerA += m
                else:
                    playerB += m

print(f'PLAYER A: {playerA} point(s)\nPLAYER B: {playerB} points')





