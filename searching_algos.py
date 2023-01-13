def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "Element not present"


# Note Binary search is applicable on sorted elements only

# Binary search with recursion
def binary_search(arr, low, high, target):
    if low <= high:
        middle_index = low + (high - low) // 2
        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] > target:
            return binary_search(arr, low, middle_index - 1, target)
        else:
            return binary_search(arr, middle_index + 1, high, target)
    return "Element Not present"


# Binary search without recursion
def binary_search_without_recursion(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        middle_index = low + (high - low) // 2
        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] < target:
            low = middle_index + 1
        else:
            high = middle_index - 1
    return "Element Not present"
