

class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self, points_to_shelf):
        self.shelved += points_to_shelf

    def clear_shelf(self):
        self.shelved = 0
    
    def bank(self):
        self.balance += self.shelved
        self.clear_shelf()