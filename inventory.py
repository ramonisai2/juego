class Inventory:
    def __init__(self):
        self.items = []
        self.max_slots = 20

    def add_item(self, item):
        if len(self.items) < self.max_slots:
            self.items.append(item)
            return True
        return False
