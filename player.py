class Player:
    def __init__(self):
        self.energy = 3
        self.courage = 0
        self.items = []

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def lose_energy(self):
        if self.energy > 0:
            self.energy -= 1

    def gain_courage(self):
        self.courage += 1
