class Items():
    def __init__(self, name=None, description=None, value=None):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "Name: {}\nValue: {}\nDescription: ".format(self.name, self.description, self.value)

    def setItemName(self, name):
        self.name = name

    def getItemName(self):
        return self.name
    