import random
import collections


class GameLogic:

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