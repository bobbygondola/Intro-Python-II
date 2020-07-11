# wite a class to hold item information

class Item():

    def __init__(self, item_name, item_desc):
        self.item_name = item_name
        self.item_desc = item_desc
        
    def __str__(self):
        return f"Item: {self.item_name}, Desc: {self.item_desc}"
    
    def print_name(self):
        print(self)
    
        