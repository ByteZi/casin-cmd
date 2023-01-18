from games.deck.deck import Deck
from games.player import Player

class BlackJack():
    def __init__(self, wallet):
        self.deck = Deck()
        self.deck.generate()
        self.wallet = wallet
        self.dealer = Player(self.deck, False)
        self.player = Player(self.deck, True)

    def play(self):

        # Figure out imports
        # from game import Game        
    
        while self.wallet > 0:
            try:
                bet = int(input("How much are you betting? : "))
            except ValueError:
                print("Must be integers")
                continue
            
            while True:
                print(f'''
        *=============================================================================================*                                                                                           
        *    _/_/_/    _/          _/_/      _/_/_/  _/    _/        _/    _/_/      _/_/_/  _/    _/ * 
        *   _/    _/  _/        _/    _/  _/        _/  _/          _/  _/    _/  _/        _/  _/    * 
        *  _/_/_/    _/        _/_/_/_/  _/        _/_/            _/  _/_/_/_/  _/        _/_/       * 
        * _/    _/  _/        _/    _/  _/        _/  _/    _/    _/  _/    _/  _/        _/  _/      * 
        *_/_/_/    _/_/_/_/  _/    _/    _/_/_/  _/    _/    _/_/    _/    _/    _/_/_/  _/    _/     * 
        *=============================================================================================*    

        Currency  = [ {self.wallet} ]

                ''')
                if bet > self.wallet:
                    print("You dont have enough")
                    break

                else:

                    player = self.player.deal()
                    dealer = self.dealer.deal()
                    
                    if player == 1:

                        if dealer == 1 :
                            print(f'''
                                ┌─────────────────────┐
                                |                     | 
                                |     IT'S A PUSH     | 
                                |                     |
                                |    Player [{self.player.score:<2}]      |
                                |    Player [{self.dealer.score:<2}]      |
                                └─────────────────────┘
                            ''')
                            reset = self.reset()
                            if reset == 1:
                                break

                            if  reset == 0:
                                return self.wallet


                        print(f'''
                            ┌─────────────────────┐
                            |                     | 
                            |     PLAYER WINS     | 
                            |                     |
                            |    Player [{self.player.score:<2}]      |
                            |    Player [{self.dealer.score:<2}]      |
                            └─────────────────────┘
                        ''')  
                        reset = self.reset()
                        if reset == 1:
                            self.wallet += bet
                            break

                        if  reset == 0:
                            return self.wallet + bet

                    choice = ""
                    
                    while choice != "stand" or choice == 'yes':
                        
                        choice = input("Hit or Stand? : ")
                        choice.lower()

                        if choice == "hit":
                            bust = self.player.hit()

                            if self.player.score == 21:
                                print(f'''
                                    ┌─────────────────────┐
                                    |                     | 
                                    |   PLAYER BLACKJACK  | 
                                    |                     |
                                    |    Player [{self.player.score:<2}]        |
                                    |    Player [{self.dealer.score:<2}]        |
                                    └─────────────────────┘
                                ''')
                                reset = self.reset()
                                if reset == 1:
                                    self.wallet += bet
                                    break

                                if  reset == 0:
                                    return self.wallet + bet
                                

                            if bust == 1:
                                print(f'''
                                    ┌─────────────────────┐
                                    |                     | 
                                    |     PLAYER BUST     | 
                                    |                     |
                                    |    Player [{self.player.score:<2}]        |
                                    |    Player [{self.dealer.score:<2}]        |
                                    └─────────────────────┘
                                ''')
                                reset = self.reset()
                                if reset == 1:
                                    self.wallet -= bet
                                    break

                                if  reset == 0:
                                    return self.wallet - bet
                        
                    while self.dealer.score < 17 and self.dealer.score < self.player.score:
                        bust = self.dealer.hit()
                        if bust == 1 :
                            print(f'''
                                ┌─────────────────────┐
                                |                     | 
                                |     DEALER BUST     | 
                                |                     |
                                |    Player [{self.player.score:<2}]        |
                                |    Player [{self.dealer.score:<2}]        |
                                └─────────────────────┘
                            ''')
                            reset = self.reset()
                            if reset == 1:
                                self.wallet += bet
                                break

                            if  reset == 0:
                                self.wallet += bet
                                return self.wallet - bet
                    
                    player_score = self.player.score
                    dealer_score = self.dealer.score

                    if player_score > dealer_score :
                        print(f'''
                            ┌─────────────────────┐
                            |                     | 
                            |     PLAYER WINS     | 
                            |                     |
                            |    Player [{player_score:<2}]        |
                            |    Player [{dealer_score:<2}]        |
                            └─────────────────────┘
                        ''')
                        reset = self.reset()
                        if reset == 1:
                            self.wallet += bet
                            break

                        if  reset == 0:
                        
                            return self.wallet + bet

                    if player_score < dealer_score :
                        print(f'''
                            ┌─────────────────────┐
                            |                     | 
                            |     DEALER WINS     | 
                            |                     |
                            |    Player [{player_score:<2}]        |
                            |    Player [{dealer_score:<2}]        |
                            └─────────────────────┘
                        ''')
                        reset = self.reset()
                        if reset == 1:
                            self.wallet -= bet
                            break

                        if  reset == 0:
                            return self.wallet - bet

                    if player_score == 21 and dealer_score == 21 :
                        print(f'''
                            ┌─────────────────────┐
                            |                     | 
                            |     IT'S A PUSH     | 
                            |                     |
                            |    Player [{player_score:<2}]        |
                            |    Player [{dealer_score:<2}]        |
                            └─────────────────────┘
                        ''')
                        reset = self.reset()
                        if reset == 1:
                            break

                        if  reset == 0:
                            return self.wallet - bet
        print('''
 ______     ______     __   __     __  __     ______     __  __     ______   ______  
/\  == \   /\  __ \   /\ "-.\ \   /\ \/ /    /\  == \   /\ \/\ \   /\  == \ /\__  _\ 
\ \  __<   \ \  __ \  \ \ \-.  \  \ \  _"-.  \ \  __<   \ \ \_\ \  \ \  _-/ \/_/\ \/ 
 \ \_____\  \ \_\ \_\  \ \_\\"\_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\      \ \_\ 
  \/_____/   \/_/\/_/   \/_/ \/_/   \/_/\/_/   \/_/ /_/   \/_____/   \/_/       \/_/
        ''')
        return 0

    def reset(self):
        self.deck = Deck()
        self.deck.generate()
        self.dealer = Player(self.deck, False)
        self.player = Player(self.deck, True)
        
        retry = ''

        while retry!= 'y' or retry != 'n':
            retry = input('Play again? [Y] [N] : ')
            retry.lower()

            if retry == 'y':
                return 1
                
            if retry == 'n':
                return 0
            
        

    

    
            





