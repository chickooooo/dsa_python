"""
LinkedList class unit tests

- __init__
    - set linked list head node as None if no value is provided
    - set linked list head node as node with provided value

- get_head_node
    - return None if head node does not exist
    - return head node of linked list if exists

- add_new_head
    - add node from given value as new head node
    - set previous head node as next node of new head node if previous head node exists
    - set none as next node of new head node if does not exists
    - return new head node

- append_node
    - if list is empty, append node from given_value as head node
    - append node from given_value at the end of linked list
    - return newly added node

- as_list
    - return linked list in form of python list

- remove_node
    - return None if list is empty
    - return None if node with given value not found
    - if node to remove is head node, replace head node
    - else remove node with given value from the list
    - return removed node

- get_length
    - return 0 if no items
    - return number of items

- node_present
    - return False if list is empty
    - return False if node not found
    - return True if node found

- access_node_by_index
    - return None if list is empty
    - return None if index out of range
    - return node at index
    - return None if negative index out of range
    - return node from tail if negative index

- update_at_index
    - return None if list is empty
    - return None if index out of range
    - return updated node
    - return None if negative index out of range
    - return updated node from tail if negative index

- swap_nodes
    - return False if list is empty
    - return False if same values
    - return False if either of the value is not present in the list
    - return True when swapping with head node
    - return True when swapping with non head node


"""

from node import Node
from linked_list import LinkedList


# __init__()

def test_no_head_node() -> None:
    """set linked list head node as None if no value is provided
    """
    linked_list: LinkedList = LinkedList()
    assert linked_list.head_node is None

def test_set_head_node() -> None:
    """set linked list head node as node with provided value
    """
    given_value: int = 123
    linked_list: LinkedList = LinkedList(given_value)
    assert isinstance(linked_list.head_node, Node)
    assert linked_list.head_node.get_value() == given_value
    assert linked_list.head_node.get_next_node() is None


# get_head_node()

def test_get_no_head_node() -> None:
    """return None if head node does not exist
    """
    linked_list: LinkedList = LinkedList()
    assert linked_list.get_head_node() is None

def test_get_head_node() -> None:
    """return head node of linked list
    """
    given_value: int = 123
    linked_list: LinkedList = LinkedList(given_value)
    assert isinstance(linked_list.head_node, Node)
    assert linked_list.head_node.get_value() == given_value
    assert linked_list.head_node.get_next_node() is None


# add_new_head()

def test_add_new_head() -> None:
    """add node from given value as new head node
    """
    value_1: int = 10
    value_2: int = 20
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.add_new_head(value_2)
    assert isinstance(linked_list.head_node, Node)
    assert linked_list.head_node.get_value() == value_2

def test_link_old_head_to_new_head() -> None:
    """set previous head node as next node of new head node if previous head node exists
    """
    value_1: int = 10
    value_2: int = 20
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.add_new_head(value_2)
    head_node = linked_list.head_node
    assert isinstance(head_node, Node)
    next_node = head_node.next_node
    assert isinstance(next_node, Node)
    assert next_node.get_value() == value_1

def test_link_none_to_new_head() -> None:
    """set none as next node of new head node if does not exists
    """
    value_2: int = 20
    linked_list: LinkedList = LinkedList()
    linked_list.add_new_head(value_2)
    head_node = linked_list.head_node
    assert isinstance(head_node, Node)
    assert head_node.get_next_node() is None

def test_return_new_head_node() -> None:
    """return newly added head node
    """
    value_1: int = 10
    value_2: int = 20
    linked_list: LinkedList = LinkedList(value_1)
    result: Node = linked_list.add_new_head(value_2)
    assert isinstance(result, Node)
    assert result.get_value() == value_2
    result_next_node = result.get_next_node()
    assert isinstance(result_next_node, Node)
    assert result_next_node.get_value() == value_1


# append_node()

def test_append_as_head_node() -> None:
    """if list is empty, append node from given_value as head node
    """
    value_1: int = 10
    linked_list: LinkedList = LinkedList()
    linked_list.append_node(value_1)
    head_node = linked_list.head_node
    assert isinstance(head_node, Node)
    assert head_node.get_value() == value_1

def test_append_node() -> None:
    """append node from given_value at the end of linked list
    """
    # arrange
    value_1: int = 10
    value_2: int = 20
    value_3: int = 30
    linked_list: LinkedList = LinkedList(value_1)
    # act
    linked_list.append_node(value_2)
    linked_list.append_node(value_3)
    # assert
    assert linked_list.as_list() == [10, 20, 30]

def test_return_appended_node() -> None:
    """return appended node
    """
    # arrange
    value_1: int = 10
    value_2: int = 20
    linked_list: LinkedList = LinkedList(value_1)
    # act
    result = linked_list.append_node(value_2)
    assert isinstance(result, Node)
    assert result.get_value() == value_2
    assert result.get_next_node() is None


# as_list()

def test_return_in_list_form() -> None:
    """return linked list in form of python list
    """
    # arrange
    value_1: int = 10
    value_2: int = 20
    value_3: int = 30
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    linked_list.append_node(value_3)
    # act
    result: list[str | int] = linked_list.as_list()
    # assert
    assert result == [10, 20, 30]


# remove_node()

def test_none_if_empty_list() -> None:
    """return None if list is empty
    """
    linked_list: LinkedList = LinkedList()
    result: Node | None = linked_list.remove_node("abc")
    assert result is None

def test_none_if_not_found() -> None:
    """return None if node with given value not found
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.remove_node("c")
    assert result is None

def test_remove_head_node() -> None:
    """remove node with given value from the list
    """
    value_1: str = 'a'
    value_2: str = 'b'
    value_3: str = 'c'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    linked_list.append_node(value_3)
    linked_list.remove_node(value_1)
    result = linked_list.as_list()
    head_node = linked_list.head_node
    assert isinstance(head_node, Node)
    assert head_node.get_value() == value_2
    assert result == ['b', 'c']

def test_remove_node() -> None:
    """remove node with given value from the list
    """
    value_1: str = 'a'
    value_2: str = 'b'
    value_3: str = 'c'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    linked_list.append_node(value_3)
    linked_list.remove_node(value_2)
    result = linked_list.as_list()
    assert result == ['a', 'c']

def test_return_removed_node() -> None:
    """remove node with given value from the list
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.remove_node(value_2)
    assert isinstance(result, Node)
    assert result.get_value() == value_2


# get_length()

def test_0_length() -> None:
    """return 0 if no items
    """
    linked_list: LinkedList = LinkedList()
    result: int = linked_list.get_length()
    assert result == 0

def test_get_length() -> None:
    """return number of items
    """
    linked_list: LinkedList = LinkedList()
    for i in range(10):
        linked_list.append_node(i)
    result: int = linked_list.get_length()
    assert result == 10


# node_present()

def test_node_present_empty() -> None:
    """return False if list is empty
    """
    linked_list: LinkedList = LinkedList()
    result: bool = linked_list.node_present("abc")
    assert result is False

def test_node_present_false() -> None:
    """return False if node found
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: bool = linked_list.node_present("c")
    assert result is False

def test_node_present_true() -> None:
    """return True if node not found
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: bool = linked_list.node_present("b")
    assert result is True


# access_node_by_index()

def test_access_node_empty() -> None:
    """return None if list is empty
    """
    linked_list: LinkedList = LinkedList()
    result: Node | None = linked_list.access_node_by_index(4)
    assert result is None

def test_access_node_out_of_range() -> None:
    """return None if index out of range
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.access_node_by_index(4)
    assert result is None

def test_access_node_by_index() -> None:
    """return node at index
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.access_node_by_index(1)
    assert isinstance(result, Node)
    assert result.get_value() == value_2
    result: Node | None = linked_list.access_node_by_index(0)
    assert isinstance(result, Node)
    assert result.get_value() == value_1

def test_access_node_out_of_range_negative() -> None:
    """return None if index out of range
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.access_node_by_index(-3)
    assert result is None

def test_access_node_by_index_negative() -> None:
    """return node from tail if negative index
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.access_node_by_index(-1)
    assert isinstance(result, Node)
    assert result.get_value() == value_2
    result: Node | None = linked_list.access_node_by_index(-2)
    assert isinstance(result, Node)
    assert result.get_value() == value_1


# update_node_at_index()

def test_update_node_empty() -> None:
    """return None if list is empty
    """
    linked_list: LinkedList = LinkedList()
    result: Node | None = linked_list.update_at_index(4, 'abc')
    assert result is None

def test_update_node_out_of_range() -> None:
    """return None if index out of range
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.update_at_index(4, 'abc')
    assert result is None

def test_update_node_at_index() -> None:
    """return updated node
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.update_at_index(1, 'B')
    assert isinstance(result, Node)
    assert result.get_value() == 'B'
    assert linked_list.as_list() == ['a', 'B']
    result: Node | None = linked_list.update_at_index(0, 'A')
    assert isinstance(result, Node)
    assert result.get_value() == "A"
    assert linked_list.as_list() == ['A', 'B']

def test_update_node_out_of_range_negative() -> None:
    """return None if index out of range
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.access_node_by_index(-3)
    assert result is None

def test_update_node_by_index_negative() -> None:
    """return updated node from tail if negative index
    """
    value_1: str = 'a'
    value_2: str = 'b'
    linked_list: LinkedList = LinkedList(value_1)
    linked_list.append_node(value_2)
    result: Node | None = linked_list.update_at_index(-1, 'B')
    assert isinstance(result, Node)
    assert result.get_value() == 'B'
    assert linked_list.as_list() == ['a', 'B']
    result: Node | None = linked_list.update_at_index(-2, 'A')
    assert isinstance(result, Node)
    assert result.get_value() == "A"
    assert linked_list.as_list() == ['A', 'B']


# update_node_at_index()

def test_swap_nodes_empty() -> None:
    """return False if list is empty
    """
    linked_list: LinkedList = LinkedList()
    result: bool = linked_list.swap_nodes(4, 1)
    assert result is False

def test_swap_nodes_same() -> None:
    """return False if same values
    """
    linked_list: LinkedList = LinkedList()
    for i in range(10):
        linked_list.append_node(i)
    result: bool = linked_list.swap_nodes(4, 4)
    assert result is False

def test_swap_nodes_no_value() -> None:
    """return False if either of the value is not present in the list
    """
    linked_list: LinkedList = LinkedList()
    for i in range(10):
        linked_list.append_node(i)
    result: bool = linked_list.swap_nodes(10, 0)
    assert result is False
    result: bool = linked_list.swap_nodes(4, 15)
    assert result is False

def test_swap_nodes_one_head() -> None:
    """return True when swapping with head node
    """
    linked_list: LinkedList = LinkedList()
    for i in range(10):
        linked_list.append_node(i)
    # first and middle
    result: bool = linked_list.swap_nodes(0, 8)
    assert result is True
    assert linked_list.as_list() == [8, 1, 2, 3, 4, 5, 6, 7, 0, 9]
    # first and adjacent
    result: bool = linked_list.swap_nodes(8, 1)
    assert result is True
    assert linked_list.as_list() == [1, 8, 2, 3, 4, 5, 6, 7, 0, 9]
    # middle and first
    result: bool = linked_list.swap_nodes(3, 1)
    assert result is True
    assert linked_list.as_list() == [3, 8, 2, 1, 4, 5, 6, 7, 0, 9]
    # last and first
    result: bool = linked_list.swap_nodes(3, 9)
    assert result is True
    assert linked_list.as_list() == [9, 8, 2, 1, 4, 5, 6, 7, 0, 3]
    # adjacent and first
    result: bool = linked_list.swap_nodes(8, 9)
    assert result is True
    assert linked_list.as_list() == [8, 9, 2, 1, 4, 5, 6, 7, 0, 3]

def test_swap_nodes_non_head() -> None:
    """return True when swapping with head node
    """
    linked_list: LinkedList = LinkedList()
    for i in range(10):
        linked_list.append_node(i)
    # case 1
    result: bool = linked_list.swap_nodes(3, 8)
    assert result is True
    assert linked_list.as_list() == [0, 1, 2, 8, 4, 5, 6, 7, 3, 9]
    # case 2
    result: bool = linked_list.swap_nodes(4, 5)
    assert result is True
    assert linked_list.as_list() == [0, 1, 2, 8, 5, 4, 6, 7, 3, 9]
    # case 3
    result: bool = linked_list.swap_nodes(7, 2)
    assert result is True
    assert linked_list.as_list() == [0, 1, 7, 8, 5, 4, 6, 2, 3, 9]
    # case 4
    result: bool = linked_list.swap_nodes(6, 4)
    assert result is True
    assert linked_list.as_list() == [0, 1, 7, 8, 5, 6, 4, 2, 3, 9]
