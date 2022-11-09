"""
Node class unit tests

- __init__
    - create node with value
    - next node is None if no value is provided
    - next node is set to given node

- get_value
    - return the value of the node

- get_next_node
    - return None if no next node
    - return next node if node is present

- set_next_node
    - set next node to given node
    - return given node

"""

import unittest
from node import Node


class TestNode(unittest.TestCase):
    """
    Testing class for Node class
    """
    # __init__()

    def test_create_node_with_value(self):
        """create node with value
        """
        given_value = 'abc'
        node = Node(value=given_value)
        self.assertEqual(node.value, given_value)

    def test_next_node_none(self):
        """next node is None if no value is provided
        """
        node = Node(value=123)
        self.assertEqual(node.next_node, None)

    def test_given_next_node(self):
        """next node is set to given node
        """
        node_1 = Node(value=1)
        node_2 = Node(value=2, next_node=node_1)
        self.assertEqual(node_2.next_node, node_1)


    # get_value()

    def test_get_value(self):
        """return the value of the node
        """
        given_value = "xyz"
        node = Node(value=given_value)
        self.assertEqual(node.get_value(), given_value)


    # get_next_node()

    def test_get_next_node_none(self):
        """return None if no next node
        """
        node = Node(value=12)
        self.assertEqual(node.get_next_node(), None)

    def test_get_next_node(self):
        """return next node if node is present
        """
        node_1 = Node(value=1)
        node_2 = Node(value=2, next_node=node_1)
        self.assertEqual(node_2.get_next_node(), node_1)


    # set_next_node()

    def test_set_next_node(self):
        """set next node to given node
        """
        node_1 = Node(value=1)
        node_2 = Node(value=2)
        node_2.set_next_node(next_node=node_1)
        self.assertEqual(node_2.next_node, node_1)

    def test_set_next_node_return_node(self):
        """return given node
        """
        node_1 = Node(value=1)
        node_2 = Node(value=2)
        result = node_2.set_next_node(next_node=node_1)
        self.assertEqual(result, node_1)
