#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

import collections as clst
from random import choice

Card = clst.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank,suit)  for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]
    
    
suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print("rank_value {}".format(rank_value))
    print("lenth: {}".format(len(suits_values)))
    print("current card suit: {}".format(suits_values[card.suit]))
    return rank_value*len(suits_values) + suits_values[card.suit]

   
if __name__ == "__main__":
    beer_card = Card('7','diamonds')
    print(beer_card)
    fd_op = FrenchDeck()
    print(len(fd_op))
    print(choice(fd_op))
    for k in fd_op:
        print(k)
    print("-------------------------\n")    
    for f in reversed(fd_op):
        print(f)
    print("=======\n")
    for i in sorted(fd_op, key=spades_high):
        print(i)
