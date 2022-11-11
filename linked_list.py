"""
Linked List:
    - Linked list is comprised of a series of nodes.
    - The nodes contain a link to the next node.
    - Can be unidirectional or bidirectional.
    - The head node is the node at the beginning of the list.
    - This last node is called the tail node.
    - Have a single head node, which serves as the first node in the list.

"""

from node import Node

class LinkedList:
    """
    LinkedList Class
    """

    def __init__(self, head_node: Node) -> None:
        self.head_node = head_node
