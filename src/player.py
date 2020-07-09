# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return "Hi {}.".format(self.name)