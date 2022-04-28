import random
import collections


class GameLogic:

    @staticmethod
    def validate_keepers(dice_list, keep_list):
        counted_dice_list = collections.Counter(dice_list)
        counted_keep_list = collections.Counter(keep_list)
        for num in counted_keep_list:
            if counted_keep_list[num] > counted_dice_list[num]:
                return False
        return True

    @staticmethod
    def calculate_score(dice):
        sorted_dice = collections.Counter(dice)
        points = 0
        if len(sorted_dice) == 6:
            points += 1500
        elif len(sorted_dice) == 3 and set(sorted_dice.values()) == set((2, 2, 2)):
            points += 1500
        else:
            for key, count in sorted_dice.items():
                if count >= 3:
                    if key == 1:
                        points += (count - 2) * 1000
                    else:
                        points += (count - 2) * key * 100
                else:
                    if key == 5:
                        points += 50 * count
                    if key == 1:
                        points += 100 * count
        return points


    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
        return tuple(dice_list)

    @staticmethod
    def get_scorers(rolled_dice):
        dice_count = collections.Counter(rolled_dice)
        scoring_dice = []
        for die_value in dice_count:
            if die_value == 1 or die_value == 5:
                for x in range(dice_count[die_value]):
                    scoring_dice.append(die_value)
            else:
                if dice_count[die_value] > 2:
                    for x in range(dice_count[die_value]):
                        scoring_dice.append(die_value)
        return tuple(scoring_dice)

