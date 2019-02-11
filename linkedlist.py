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

    def find_max(self, hedgehog = self.head):
        if hedgehog.next == None:
            return hedgehog.number
        else:
            max_of_rest = self.find_max(hedgehog.next)
            return max_of_rest if max_of_rest > hedgehog.number else hedgehog.number