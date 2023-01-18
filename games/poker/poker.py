from games.deck.deck import Deck
from games.player import Player

class Poker:
    def __init__(self, wallet):
        self.deck = Deck()
        self.deck.generate()
        self.table = []

        self.player = Player(self.deck, True)
        self.C1 = Player(self.deck, False)

        self.wallet = wallet
        self.pot = 0

    def play(self):

        print(self.player.check_straight())
