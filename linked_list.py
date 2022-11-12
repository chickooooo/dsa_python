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

    def __init__(self, head_node_value: int | str | None = None) -> None:
        """create linked list with given value as head node

        Args:
            head_node_value (int | str | None, optional): value for head node of the list.
            Defaults to None.
        """
        if head_node_value is None:
            self.head_node: Node | None = None
        else:
            head_node = Node(head_node_value)
            self.head_node: Node | None = head_node

    def get_head_node(self) -> Node | None:
        """get head node of linked list

        Returns:
            Node | None: returns node if present else None
        """
        return self.head_node

    def add_new_head(self, head_node_value: int | str) -> Node:
        """adds new head node to the list

        Args:
            head_node_value (int | str): value of new head node

        Returns:
            Node: new head node
        """
        new_node: Node = Node(head_node_value)
        if self.head_node is not None:
            new_node.set_next_node(self.head_node)
        self.head_node = new_node
        return self.head_node

    def append_node(self, new_node_value: int | str) -> Node:
        """append node with given value at the end of the list

        Args:
            new_node_value (int | str): value of new node

        Returns:
            Node: newly appended node
        """
        new_node: Node = Node(new_node_value)
        previous_node = self.head_node
        if previous_node is None:
            self.head_node = new_node
            return self.head_node
        current_node = previous_node.get_next_node()
        while current_node:
            previous_node = current_node
            current_node = current_node.get_next_node()        
        previous_node.set_next_node(new_node)
        return new_node
