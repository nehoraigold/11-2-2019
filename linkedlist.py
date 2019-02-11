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

    def add_first(self, number):
        new_hedgehog=Hedgehog(number)
        new_hedgehog.next= self.head
        self.head=new_hedgehog
        self.length +=1
        return self.head