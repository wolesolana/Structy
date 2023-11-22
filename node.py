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

    def reverse_list(self):
        previous = None
        current = self

        if self.value is None:
            return None

        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous

    def zip_lists(self, other):
        current_1 = self
        current_2 = other

        while current_1 is not None and current_2 is not None:
            next_1 = current_1.next
            next_2 = current_2.next

            current_1.next = current_2
            if next_1 is not None:
                current_2.next = next_1

            current_1 = next_1
            current_2 = next_2

        return self
