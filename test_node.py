import unittest
from node import Node


class TestNode(unittest.TestCase):
    def test_node_sets_next_to_none_by_default(self):
        node = Node(3)

        self.assertIsNone(node.next)
        self.assertEqual(node.value, 3)

    def test_node_sets_value_of_next(self):
        node = Node(3)
        node.next = Node(4)

        self.assertEqual(node.next.value, 4)
        self.assertIsNone(node.next.next)

    def test_node_evaluates_if_two_nodes_are_equal(self):
        node1 = Node(3)
        node2 = Node(3)

        self.assertEqual(node1, node2)

    def test_node_evaluates_if_two_nodes_are_not_equal(self):
        node1 = Node(3)
        node2 = Node(4)

        self.assertNotEqual(node1, node2)

    def test_node_evaluates_if_one_node_is_less_than_another(self):
        node1 = Node(3)
        node2 = Node(4)

        self.assertLess(node1, node2)

    def test_node_evaluates_if_one_node_is_greater_than_another(self):
        node1 = Node(3)
        node2 = Node(4)

        self.assertGreater(node2, node1)

    def test_sum_list_returns_the_sum_of_all_values_in_a_linked_list(self):
        a = Node(2)
        b = Node(8)
        c = Node(3)
        d = Node(-1)
        e = Node(7)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertEqual(a.sum_list(), 19)

    def test_sum_list_returns_node_value_for_single_node_list(self):
        a = Node(2)

        self.assertEqual(a.sum_list(), 2)

    def test_sum_list_returns_zero_for_empty_list(self):
        self.assertEqual(Node(None).sum_list(), 0)

    def test_reverse_list_returns_a_reversed_linked_list(self):
        a = Node(2)
        b = Node(8)
        c = Node(3)
        d = Node(-1)
        e = Node(7)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        a.reverse_list()

        self.assertEqual(e.next, d)
        self.assertEqual(d.next, c)
        self.assertEqual(c.next, b)
        self.assertEqual(b.next, a)
        self.assertIsNone(a.next)

    def test_reverse_list_for_a_single_node_list_returns_itself(self):
        a = Node(2)

        a.reverse_list()

        self.assertIsNone(a.next)

    def test_reverse_list_for_an_empty_list_returns_none(self):
        self.assertIsNone(Node(None).reverse_list())


if __name__ == "__main__":
    unittest.main()
