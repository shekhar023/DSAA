
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [4 ,2, 1, 3, 5]
    print("Unsorted array: ", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)