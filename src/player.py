# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player(Room):
    def __init__(self, name, location, description):
        super().__init__(location, description)
        self.name = name

    def __str__(self):
        return "Hi {}. You are at the {}.  {}.".format(self.name, self.location, self.description)