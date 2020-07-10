# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        return f"Name: {self.inventory[0]}"
    
    def pickup(self, items):
        #add item to players inventory
        self.inventory.append(self.current_room.items[0])
    
    def drop(self, items):
        ##delete from inventory
        self.inventory.remove(self.current_room.items[0])