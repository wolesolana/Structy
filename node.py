class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def sum_list(self):
        sum = 0
        head = self

        if head.value is None:
            return sum

        while head is not None:
            sum += head.value
            head = head.next

        return sum