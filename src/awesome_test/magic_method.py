#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

import collections as clst

Card = clst.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks for suit in self.suits]
        

    def __len__(self):
        return len(self._cards)

    def __getitem(self,position):
        return self._cards[position]

if __name__ == "__main__":
    beer_card = Card('7','diamonds')
    print(beer_card)
    fd_op = FrenchDeck()
    print(len(fd_op))
