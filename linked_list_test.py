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
    if head_node is None:
        raise Exception('head_node is none')
    next_node = head_node.next_node
    if next_node is None:
        raise Exception('next_node of head_node is none')
    assert next_node.get_value() == value_1

def test_link_none_to_new_head() -> None:
    """set none as next node of new head node if does not exists
    """
    value_2: int = 20
    linked_list: LinkedList = LinkedList()
    linked_list.add_new_head(value_2)
    head_node = linked_list.head_node
    if head_node is None:
        raise Exception('head_node is none')
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
    if result_next_node is None:
        raise Exception('next_node of head_node is none')
    assert result_next_node.get_value() == value_1


# append_node()

def test_append_as_head_node() -> None:
    """if list is empty, append node from given_value as head node
    """
    value_1: int = 10
    linked_list: LinkedList = LinkedList()
    linked_list.append_node(value_1)
    head_node = linked_list.head_node
    if head_node is None:
        raise Exception('head_node is none')
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
    previous_node = linked_list.get_head_node()
    if previous_node is None:
        raise Exception('head_node is None')
    # head node
    assert previous_node.get_value() == value_1
    current_node = previous_node.get_next_node()
    while current_node:
        previous_node = current_node
        current_node = current_node.get_next_node()
    # tail node
    assert previous_node.get_value() == value_3

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
    result: list[str] | list[int] = linked_list.as_list()
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
    if head_node is None:
        raise Exception("head node is none")
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
    if result is None:
        raise Exception('returned node is none')
    assert result.get_value() == value_2
