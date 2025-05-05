
# Binary search algorthim is used in a sorted array by repeatedly dividing the array in half.
# The main idea behind this algorithm is to use the sorted array and reduce the time complexity to O(logn)

# To apply Binary Search algorithm

    # The data structure must be sorted.
    # Access to any element of the data structure should take constant time.

def binary_search(arr, low, high, key):

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        
        # if the key is greater than mid element then we ignore the left half
        elif arr[mid] < key:
            low = mid + 1

        # if key is lesser than the mid element then we ignore the right half
        else:
            high = mid - 1

    return -1 # if the element is not present in the array


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    key = 40
    low = 0
    high = len(arr) - 1

    result = binary_search(arr, low, high, key)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

