"""
    - convert unsorted array to sorted array
    - pivot and partition
    - divide and conquer
    - time complexity:
        -- worst case: O(n^2)
            --- worst case is when pivot is always the smallest or largest element
            --- worst case is when the array is sorted
        -- average case: O(nlogn)
"""

def quick_sort(array: list[int]) -> list[int]:
    """Quick sort using last element as pivot.

    Args:
        array (list[int]): Unsorted array.

    Returns:
        list[int]: Sorted array.
    """
    pivot: int = array[-1]
    pivot_count: int = array.count(pivot)

    left: list[int] = [element for element in array if element < pivot]
    if left != []:
        left = quick_sort(left)

    right: list[int] = [element for element in array if element > pivot]
    if right != []:
        right = quick_sort(right)

    return left + [pivot]*pivot_count + right


def quick_sort_2(array: list[int]) -> list[int]:
    """Quick sort using first element as pivot.

    Args:
        array (list[int]): Unsorted array.

    Returns:
        list[int]: Sorted array.
    """
    pivot: int = array[0]
    pivot_count: int = array.count(pivot)

    left: list[int] = [element for element in array if element < pivot]
    if left != []:
        left = quick_sort_2(left)

    right: list[int] = [element for element in array if element > pivot]
    if right != []:
        right = quick_sort_2(right)

    return left + [pivot]*pivot_count + right


def reverse_quick_sort(array: list[int]) -> list[int]:
    """Quick sort in descending order using last element as pivot.

    Args:
        array (list[int]): Unsorted array.

    Returns:
        list[int]: Sorted array.
    """
    pivot: int = array[-1]
    pivot_count: int = array.count(pivot)

    left: list[int] = [element for element in array if element > pivot]
    if left != []:
        left = reverse_quick_sort(left)

    right: list[int] = [element for element in array if element < pivot]
    if right != []:
        right = reverse_quick_sort(right)

    return left + [pivot]*pivot_count + right


array = [6, 3, 1, 9, 6, 7, 2, 8, 5, 8, 2, 8]
print(reverse_quick_sort(array))
