import user_array_input as user

def insertion_sort():
    arr = user.get_integer_input()
    print("Entered array: ", arr)
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j > 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    print("Sorted array: ", arr)


if __name__=="main":
    insertion_sort()