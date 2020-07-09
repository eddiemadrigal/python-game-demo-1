# Implement a class to hold room information. This should have name and
# description attributes.

from item import Items

class Room(Items):
    def __init__(self, location, description, n_to=None, s_to=None, w_to=None, e_to=None, item=None):
        super().__init__()
        self.location = location
        self.description = description
        possible_direction = [n_to, s_to, w_to, e_to]
        for goto in possible_direction:
            if goto == None:
                self.goto = None
            else:
                self.goto = goto

    def __str__(self):
        return "You are at {}. {}.".format(self.location, self.description)
    

