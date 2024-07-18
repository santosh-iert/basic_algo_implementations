from sys import maxsize

from searching_algos import binary_search

sum_a = lambda a, b: a + b
max_numer = lambda a, b: a if a > b else b
square = lambda x: x * x


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        Right_arr = arr[len(arr) // 2:]
        merge_sort(left_arr)  # Recursive call on left array
        merge_sort(Right_arr)  # recursive call on right array
        i = j = k = 0
        while i < len(left_arr) and j < len(Right_arr):
            if left_arr[i] < Right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = Right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(Right_arr):
            arr[k] = Right_arr[j]
            j += 1
            k += 1
    return arr


# arr = [2, 3, 5, 7, 8, 9, 11, 12, 1]
def quick_sort_partition(arr, low, high):
    pivot_value = arr[high]
    i = low - 1
    for j in range(low, high - 1):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        partition_index = quick_sort_partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = 0
        for j in range(0, n - i - 1):  # because i elements are already in placed
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = 1
        if swapped == 0:
            return arr


def max_heapify(arr, n, i):
    largest = i  # Initializing root as a largest element
    left_child = 2 * i + 1  # Left child address = 2*i + 1
    right_child = 2 * i + 2  # Right child address = 2*i + 2
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Here we are building max heap, since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Extracting elements one by one from heap and building max heap on remaining elements.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


def selection_sort(array):
    """
    Selection Sort choosing min element first and placing that to right position
    :param array:
    :return:
    """
    if len(array) <= 1:
        return array
    for i in range(len(array)):
        min_element_index = i
        for j in range(i + 1, len(array)):
            min_element_index = j if array[j] < array[min_element_index] else min_element_index
        array[i], array[min_element_index] = array[min_element_index], array[i]
    return array


if __name__ == "__main__":
    c = 8
    d = 7
    l1 = [2, 1, 3, 4, 5, 0]
    low = 0
    high = len(l1) - 1
    print(l1)
    # heap_sort(l1)
    print(selection_sort(l1))
