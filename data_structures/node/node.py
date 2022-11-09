"""
Nodes:
    - Nodes are the fundamental building blocks of many computer science data structures.
    - An individual node contains data and links to other nodes.
    - Nodes contain data, which can be a variety of data types.
    - If a node has no links, or they are all null, you have reached the end
      of the path you were following.
    - If the only link to a node is removed, that node becomes orphaned node.

"""
from __future__ import annotations


class Node:
    """Node class
    """

    def __init__(self, value: int | str, next_node: Node | None = None) -> None:
        """creates a node with immutable value and a link to next node

        Args:
            value int | str: value of the node
            next_node (Node, optional): next node that will be linked. Defaults to None
        """
        self.value = value
        self.next_node = next_node


    def get_value(self) -> int | str:
        """get value of current node

        Returns:
          int | str: value of current node
        """
        return self.value


    def get_next_node(self) -> Node | None:
        """get next linked node

        Returns:
          Node | None: next linked node
        """
        return self.next_node


    def set_next_node(self, next_node: Node) -> Node:
        """update value of next_node

        Args:
            next_node (Node): next node to be linked

        Returns:
            Node: updated next_node
        """
        self.next_node = next_node
        return self.next_node
