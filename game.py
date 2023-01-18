from games.blackjack.blackjack import BlackJack
from games.slotmachine.slotmachine import SlotMachine
from games.poker.poker import Poker

class Game():
    def __init__(self, wallet = 100000):
        self.wallet = wallet

    def start(self):

        cmd = ""

        # Gambleton Introduction!
        print(f'''
         _       _         __                                      _             
        ( )  _  ( )       (_ )                                    ( )_           
        | | ( ) | |   __   | |    ___    _     ___ ___     __     | ,_)   _      
        | | | | | | /'__`\ | |  /'___) /'_`\ /' _ ` _ `\ /'__`\   | |   /'_`\    
        | (_/ \_) |(  ___/ | | ( (___ ( (_) )| ( ) ( ) |(  ___/   | |_ ( (_) )   
        `\___x___/'`\____)(___)`\____)`\___/'(_) (_) (_)`\____)   `\__)`\___/'   
                                                                                
                                                                                
         ___                      _      __        _____              _          
        (  _`\                   ( )    (_ )      (_   _)            ( )         
        | ( (_)   _ _   ___ ___  | |_    | |    __  | |   _     ___  | |         
        | |___  /'_` )/' _ ` _ `\| '_`\  | |  /'__`\| | /'_`\ /' _ `\| |         
        | (_, )( (_| || ( ) ( ) || |_) ) | | (  ___/| |( (_) )| ( ) || |         
        (____/'`\__,_)(_) (_) (_)(_,__/'(___)`\____)(_)`\___/'(_) (_)(_)         
                                                                     (_)
    ''')
               
        while True:
            try:
                print(f'''
    ┌─────┐         ┌─────┐         ┌─────┐         ┌─────┐         ┌─────┐   
    |  1  |         |  2  |         |  3  |         |  4  |         |  5  |
    └─────┘         └─────┘         └─────┘         └─────┘         └─────┘
   BLACKJACK         POKER        SLOT MACHINE
                    
    Current Wallet : [ {self.wallet} $ ]
                ''')           
                cmd = int(input("Choose a Game : "))

            # ValueError checks the appropriate type
            except ValueError:
                print("Please choose from the options")
                # Continue goes back to try until conditions are met
                continue

            if cmd == 1:
                self.wallet = BlackJack(self.wallet).play()
            if cmd == 3:
                SlotMachine(self.wallet).play()
            if cmd == 2:
               return

Game().start()
