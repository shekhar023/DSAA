import user_array_input as user

def insertion_sort(arr):
    print("Initial Array: ", arr)
    n = len(arr)
    print("Length of the array: ", n)

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    print("Sorted Array: ", arr)


# 👇 Only runs if this file is executed directly
if __name__ == "__main__":
    arr = user.get_integer_input()
    insertion_sort(arr)

