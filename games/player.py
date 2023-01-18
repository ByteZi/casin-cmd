class Player():
    def __init__(self, deck, isDealer):
        self.score = 0 
        self.deck = deck
        self.hand = []
        self.isDealer = isDealer
        self.pokerDict = {
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            '10' : 10,
            'J' : 11,
            'Q' : 12,
            'K' : 13,
            'A' : 14
        }

# BlackJack
    def deal(self):
        self.hand.extend(self.deck.draw(2))
        self.checkScore()
        self.show()
        if self.score == 21:
            return 1
        return 0

    def hit(self):
        card = self.deck.draw(1)
        self.hand.extend(card)
        self.checkScore()
        self.show()
  
        if self.score > 21:
            return 1
        return 0

    def checkScore(self):
        a_counter = 0 
        self.score = 0
        for card in self.hand:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()
        while a_counter > 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    def show(self):
        if self.isDealer is False:
            print(f'''
┌─────────────────────┐
|                     | 
|        DEALER       | 
|         {self.score:<2}          |
|                     |
└─────────────────────┘
            ''')
            
            
        else:
            print(f'''
┌─────────────────────┐
|                     | 
|       PLAYER        | 
|         {self.score:>2}          |
|                     |
└─────────────────────┘
            ''')
            
        

        for card in self.hand:
            card.show()

# Poker
    def check_straight(self):
        values = []
        for i in self.hand:
            temp = f'{i.value}{i.suit}'
            values.append(temp)

    def check_flush(self):
        suits = len(set([i.suit for i in self.hand]))
        if suits == 1:
            return "Flush"





