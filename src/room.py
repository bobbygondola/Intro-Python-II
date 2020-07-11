# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.items = []
    
    def __str__(self):
        for i in self.items:
            return str(i)            # still doesnt display all potions
        # return f" {self.items[0]}" # works too
    
    #write removed function
    # on remove .remove from self.items
    def remove(self):
        self.items.remove(self.items[0])
    
    
    
    
        
        
        
    

