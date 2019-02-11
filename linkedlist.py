class Hedgehog(object):
    # Create a constructure for the class
    def __init__(self, number):
        self.number = number
        self.next = None


class HedgehogList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def add_first(self, number):
         return None

    def add_last(self, number):
        return None

    def get_length(self):
        return None

    def is_empty(self):
        return self.head == None

    def find_max(self, hedgehog = None):
        if hedgehog == None:
            self.find_max(self.head)
        if hedgehog.next == None:
            return hedgehog.number
        else:
            max_of_rest = self.find_max(hedgehog.next)
            return max_of_rest if max_of_rest > hedgehog.number else hedgehog.number
    
    def remove(self, number):
        return None


############ Tests ###############
# run the file and make sure all the tests passes

def test_list(actual, expected):
    item_index = 1
    actual_item = actual
    for item in expected:
        actual_value = actual_item.number if actual_item is not None else None
        err_msg = "element number {} should have the value of {}, got {}".format(
            item_index, item, actual_value)
        assert actual_item is not None and item == actual_item.number, err_msg
        actual_item = actual_item.next


def test_length(linked_list, expected_length):
    err_msg = "Length should be {}, got {}".format(
        expected_length, linked_list.length)
    assert linked_list.length == expected_length, err_msg


def test_value(actual, expected, msg=""):
    err_msg = msg + " should be {}, got {}".format(expected, actual)
    assert actual == expected, err_msg


def test_max(linked_list, expected):
    max = linked_list.find_max()
    test_value(max, expected, "Wrong maximum")


def create_list(numbers):
    list = HedgehogList()
    for item in numbers:
        list.add_last(item)
    return list


if __name__ == "__main__":
    # test 1: Hedgehog class
    first = Hedgehog(4)
    first.next = Hedgehog(1)
    first.next.next = Hedgehog(7)

    test_list(first, [4, 1, 7])
    print("test 1: Hedgehog class passed")

    # test 2: add first & HedgehogList class
    my_list = HedgehogList()
    my_list.add_first(6)
    my_list.add_first(4)
    my_list.add_first(2)

    test_list(my_list.head, [2, 4, 6])
    print("test 2: add first & HedgehogList class passed")

    # test 3: add last
    my_list2 = HedgehogList()
    my_list2.add_last(6)
    my_list2.add_last(4)
    my_list2.add_last(2)

    test_list(my_list2.head, [6, 4, 2])
    print("test 3: add last passed")

    # test 4: length
    my_list = HedgehogList()
    test_length(my_list, 0)
    my_list.add_first(6)
    test_list(my_list.head, [6])
    test_length(my_list, 1)
    my_list.add_first(4)
    test_list(my_list.head, [4, 6])
    test_length(my_list, 2)
    my_list.add_last(8)
    test_list(my_list.head, [4, 6, 8])
    test_length(my_list, 3)
    print("test 4: length passed")

    # test 5: remove
    my_list = create_list([2, 4, 6, 8])
    removed = my_list.remove(3)
    test_value(removed, None)
    removed = my_list.remove(4)
    test_value(removed.number, 4)
    test_list(my_list.head, [2, 6, 8])
    test_length(my_list, 3)
    removed = my_list.remove(2)
    test_value(removed.number, 2)
    test_list(my_list.head, [6, 8])
    test_length(my_list, 2)
    removed = my_list.remove(8)
    test_value(removed.number, 8)
    test_list(my_list.head, [6])
    test_length(my_list, 1)
    removed = my_list.remove(6)
    test_value(removed.number, 6)
    test_length(my_list, 0)
    assert my_list.is_empty() == True, "List should be empty"
    print("test 5: remove passed")

    # test 6: find max
    test_list(create_list([1, 4, 3, 2]).head, [1, 4, 3, 2])
    test_max(create_list([1, 4, 3, 2]), 4)
    test_max(create_list([9, 4, 3, 2]), 9)
    test_max(create_list([1, 4, 3, 8]), 8)
    test_max(create_list([1]), 1)
    print("test 6: find max passed")

    # test 7: Ninja - create linked list from list
    test_list(HedgehogList([1, 4, 3, 2]).head, [1, 4, 3, 2])
    test_list(HedgehogList([1, 4, 3, 2]).head, [1, 4, 3, 2])
    test_list(HedgehogList([9, 4, 3, 2]).head, [9, 4, 3, 2])
    test_list(HedgehogList([1, 4, 3, 8]).head, [1, 4, 3, 8])
    test_list(HedgehogList([1]).head, [1])
    print("test 7: Ninja - create linked list from list passed")
