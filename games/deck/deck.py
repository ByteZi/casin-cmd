import random
from games.deck.card import Card


class Deck():
    def __init__(self):
        self.deck = []
    
    def generate(self):
        for s in range(4):
            for c in range(1,14):
                self.deck.append(Card(c, s))

    def draw(self, iteration):
        cards = []
        for i in range(iteration):
            card = random.choice(self.deck)
            cards.append(card)
            self.deck.remove(card)
        return cards




