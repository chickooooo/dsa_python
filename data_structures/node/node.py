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
    """creates a node with immutable value and link to next node
    """

    def __init__(self, value: any, next_node: Node = None) -> None:
        """creates a node with immutable value and a link to next node

        Args:
            value (any): value of the node
            next_node (Node, optional): next node that will be linked. Defaults to None

        Raises:
            Exception: if value is None
            Exception: if next_node is not of type Node
        """
        if value is None:
            raise Exception('value is required')
        self.value = value

        if next_node is not None and not isinstance(next_node, Node):
            raise Exception('next_node should be of type Node')
        self.next_node = next_node


    def get_value(self) -> any:
        """get value of current node

        Returns:
          any: value of current node
        """
        return self.value


    def get_next_node(self) -> Node:
        """get next linked node

        Returns:
          Node: next linked node
        """
        return self.next_node


    def set_next_node(self, next_node: Node) -> Node:
        """update value of next_node

        Args:
            next_node (Node): next node to be linked

        Raises:
            Exception: if next_node is not of type Node

        Returns:
            Node: updated next_node
        """
        if next_node is not None:
            return None

        if isinstance(next_node, Node):
            self.next_node = next_node
            return self.next_node
        raise Exception('next_node should be of type Node')
