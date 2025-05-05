import user_array_input as user

def insertstion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j= i-1
        while j >= 0 and arr[j]> key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    arr = user.get_integer_input()
    print("Unsorted array:", arr)
    sorted_arr = insertstion_sort(arr)
    print("Sorted array:", sorted_arr)
