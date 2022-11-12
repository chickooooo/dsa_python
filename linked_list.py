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
        previous_node: Node | None = self.head_node
        if previous_node is None:
            self.head_node = new_node
            return self.head_node
        current_node: Node | None = previous_node.get_next_node()
        while current_node:
            previous_node = current_node
            current_node = current_node.get_next_node()
        previous_node.set_next_node(new_node)
        return new_node

    def as_list(self) -> list[str | int]:
        """return linked list in form of list

        Returns:
            list[str | int]: list of str of list of int. Depending on dtype of value
        """
        item_list: list[str | int] = []
        current_node: Node | None = self.head_node
        while current_node:
            value: int | str = current_node.get_value()
            item_list.append(value)
            current_node = current_node.get_next_node()
        return item_list

    def remove_node(self, value: str | int) -> Node | None:
        """remove node with given value from the list

        Args:
            value (str | int): value to remove

        Returns:
            Node | None: returns removed node or None if not found
        """
        previous_node: Node | None = self.head_node
        if previous_node is None:
            return None
        if previous_node.get_value() == value:
            self.head_node = previous_node.get_next_node()
            return previous_node
        current_node: Node | None = previous_node.get_next_node()
        while current_node:
            if current_node.get_value() == value:
                previous_node.set_next_node(current_node.get_next_node())
                return current_node
            current_node = current_node.get_next_node()
        return None

    def get_length(self) -> int:
        """get number of items in the list

        Returns:
            int: item count
        """
        counter: int = 0
        current_node: Node | None = self.head_node
        while current_node:
            counter += 1
            current_node = current_node.get_next_node()
        return counter

    def node_present(self, value: int | str) -> bool:
        """check if node with given value is present in the list

        Args:
            value (int | str): value of node to find

        Returns:
            bool: True if node is present else False
        """
        current_node: Node | None = self.head_node
        while current_node:
            if current_node.get_value() == value:
                return True
            current_node = current_node.get_next_node()
        return False

    def access_node_by_index(self, index: int) -> Node | None:
        """get node from list by index

        Args:
            index (int): index of the node. Negative index also works

        Returns:
            Node | None: return node if found else None
        """
        counter: int = 0 if index >= 0 else (self.get_length() * -1)
        current_node: Node | None = self.head_node
        while current_node:
            if counter == index:
                return current_node
            counter = counter + 1
            current_node = current_node.get_next_node()
        return None

    def update_at_index(self, index: int, new_value: int | str) -> Node | None:
        """update node at index with the given new_value

        Args:
            index (int): index of the node. Negative index also works
            new_value (int | str): new value of the node

        Returns:
            Node | None: return updated node if found else None
        """
        previous_node: Node | None = self.head_node
        if previous_node is None:
            return None
        if index in (0, self.get_length() * -1):
            new_node: Node = Node(new_value)
            new_node.set_next_node(previous_node.get_next_node())
            self.head_node = new_node
            return new_node
        counter: int = 1 if index >= 0 else ((self.get_length() * -1) + 1)
        current_node: Node | None = previous_node.get_next_node()
        while current_node:
            if counter == index:
                new_node: Node = Node(new_value)
                new_node.set_next_node(current_node.get_next_node())
                previous_node.set_next_node(new_node)
                return new_node
            counter = counter + 1
            previous_node = current_node
            current_node = current_node.get_next_node()
        return None
