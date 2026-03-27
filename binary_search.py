def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.

    Args:
        arr (list): A sorted list of elements
        target: The element to search for

    Returns:
        int: The index of the target element if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    """
    Perform binary search recursively on a sorted array.

    Args:
        arr (list): A sorted list of elements
        target: The element to search for
        left (int): Left boundary (optional, defaults to 0)
        right (int): Right boundary (optional, defaults to len(arr)-1)

    Returns:
        int: The index of the target element if found, -1 otherwise
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Example usage
if __name__ == "__main__":
    # Test the binary search functions
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Test iterative version
    target = 7
    result = binary_search(sorted_array, target)
    print(f"Iterative: Target {target} found at index {result}")

    target = 4
    result = binary_search(sorted_array, target)
    print(f"Iterative: Target {target} found at index {result}")

    # Test recursive version
    target = 13
    result = binary_search_recursive(sorted_array, target)
    print(f"Recursive: Target {target} found at index {result}")

    target = 20
    result = binary_search_recursive(sorted_array, target)
    print(f"Recursive: Target {target} found at index {result}")