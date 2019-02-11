class Hedgehog:
    def __init__(self, number):
        self.number = number
        self.next = None


class HedgehogList:
    def __init__(self, head = None):
        self.head = head
        self.length = 0
    
    def is_empty(self):
        return self.head == None