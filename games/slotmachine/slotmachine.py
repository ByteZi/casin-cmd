import random

class SlotMachine():
    def __init__(self, wallet):
        self.wallet = wallet
    
    def play(self):
        
        symbols = ["@", "$", "&"]
        cmd = ''


        while True:
            try:
                bet = int(input("How much are you betting? : "))
            except ValueError:
                print("Must be integers")
                continue
            if bet > self.wallet:
                print("You dont have enough")
            else:
                break
        
        while cmd.lower() != 'exit':
            
            cmd = input("Roll | Exit : ")

            if cmd.lower() == 'roll':

                grid = [
                    [symbols[random.randint(0,2)],symbols[random.randint(0,2)],symbols[random.randint(0,2)]],
                    [symbols[random.randint(0,2)],symbols[random.randint(0,2)],symbols[random.randint(0,2)]],
                    [symbols[random.randint(0,2)],symbols[random.randint(0,2)],symbols[random.randint(0,2)]]
                ]
                
                sq_1 = grid[1][0]
                sq_2 = grid[1][1]
                sq_3 = grid[1][2]

                print("\n")
                for i in grid:
                    print(i)
                print('\n')

                if sq_1 == sq_2 and sq_2 == sq_3:
                    print('\n You won! \n')
                else:
                    print('\n You lost \n')

    def reset(self):
        
        retry = ''

        while retry!= 'y' or retry != 'n':
            retry = input('Play again? [Y] [N] : ')
            retry.lower()

            if retry == 'y':
                return 1
                
            if retry == 'n':
                return 0