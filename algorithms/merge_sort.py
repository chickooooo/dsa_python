"""
    - convert unsorted array to sorted array
    - divide and conquer
    - time complexity:
        -- worst case: O(n^2)
            --- worst case is when pivot is always the smallest or largest element
            --- worst case is when the array is sorted
        -- average case: O(nlogn)
"""

def merge_sort(array: list[int]) -> list[int]:    
    pass

array = [6, 3, 1, 9, 6, 7, 2, 8, 5, 8, 2, 8]
# array = [6, 3, 1, 9, 7, 2, 8]
print(merge_sort(array))
