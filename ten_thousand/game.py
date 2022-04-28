try:
    from ten_thousand.game_logic import GameLogic
    from ten_thousand.banker import Banker
except:
    from game_logic import GameLogic
    from banker import Banker
from collections import Counter
import sys

class Game():
    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_of_dice = 6
        self.round = 0
        self.dice_list = []
        self.dice_string = ''
        self.roller = None
        self.num_rounds = num_rounds


    def create_dice_string(self, tuple_of_dice):
        return_string = ''
        for die in tuple_of_dice:
            return_string += f' {die}'
        return return_string

    def play(self, roller=GameLogic.roll_dice):
        self.roller = roller

        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        start_response = input('> ')
        if start_response == 'n':
            print('OK. Maybe another time')
            sys.exit()
        elif start_response == 'y':
            self.start_new_round()
            playing = True
            while playing == True:
                print('Enter dice to keep, or (q)uit:')
                keep_or_quit = input('> ')
                if keep_or_quit == 'q':
                    print(f'Thanks for playing. You earned {self.banker.balance} points')
                    sys.exit()
                else:
                    keep_list = []
                    for num in keep_or_quit:
                        keep_list.append(int(num))
                    while GameLogic.validate_keepers(self.dice_list, keep_list) == False:
                        print('Cheater!!! Or possibly made a typo...')
                        print(f'***{self.dice_string} ***')
                        print('Enter dice to keep, or (q)uit:')
                        keep_or_quit = input('> ')
                        if keep_or_quit == 'q':
                            print(f'Thanks for playing. You earned {self.banker.balance} points')
                            sys.exit()
                        else:
                            keep_list = []
                            for num in keep_or_quit:
                                keep_list.append(int(num))
                    points = GameLogic.calculate_score(keep_list)
                    self.banker.shelf(points)
                    self.num_of_dice -= len(keep_list)
                    print(f'You have {self.banker.shelved} unbanked points and {self.num_of_dice} dice remaining')
                    print('(r)oll again, (b)ank your points or (q)uit:')
                    roll_bank_quit = input('> ')
                    if roll_bank_quit == 'b':
                        print(f'You banked {self.banker.shelved} points in round {self.round}')
                        self.banker.bank()
                        print(f'Total score is {self.banker.balance} points')
                        self.start_new_round()
                    elif roll_bank_quit == 'q':
                        print(f'Thanks for playing. You earned {self.banker.balance} points')
                        sys.exit()
                    elif roll_bank_quit == 'r':
                        self.user_roll()


    def start_new_round(self):
        self.round += 1
        if self.round > self.num_rounds:
            print(f'Thanks for playing. You earned {self.banker.balance} points')
            sys.exit()
        self.num_of_dice = 6
        print(f'Starting round {self.round}')
        self.user_roll()

    def user_roll(self):
        self.dice_string = ''
        if self.num_of_dice == 0:
            self.num_of_dice = 6
        print(f'Rolling {self.num_of_dice} dice...')
        self.dice_list = self.roller(self.num_of_dice)
        self.dice_string = self.create_dice_string(self.dice_list)
        print(f'***{self.dice_string} ***')
        if len(GameLogic.get_scorers(self.dice_list)) == 0:
            self.zilch()
    

    def zilch(self):
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f'You banked 0 points in round {self.round}')
        print(f'Total score is {self.banker.balance} points')
        self.start_new_round()
            
                








if __name__ == '__main__':
    game = Game()
    game.play()