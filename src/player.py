# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        
    def pickup(self, items):
        #add item to players inventory
        self.inventory.append(str(self.current_room.items))