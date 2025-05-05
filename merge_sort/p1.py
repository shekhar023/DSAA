# Merge Sort Algorithm

def merge(arr, left, mid, right):
    n_l = mid - left + 1 # lenght of temp left array
    n_r = right - mid # length of temp right array

    arr_left = [0] * n_l # temp array to store the left part of the array of length n_l
    arr_right = [0] * n_r  # temp array to store the right part of the array of length n_r

    # copy the orignal array on to left temp array
    for i in range(0,n_l):
        arr_left[i] = arr[left + i]

    # copy the orignal array to the right temp array
    for j in range(0,n_r):
        arr_right[j] = arr[mid + 1 + j]
    
    i = 0 # index for the smallest value in left array
    j = 0 # index for the smallest value in right array
    k = left # index value of the orignal subarray a[p:r]

    # merge the array back into a[p:r]
    while i < n_l and j < n_r:
        if arr_left[i] <= arr_right[j]:
            arr[k] = arr_left[i]
            i += 1
        else:
            arr[k] = arr_right[j]
            j += 1
        k += 1

    # add the remaining elements from left array to orignal array
    while i < n_l:
        arr[k] = arr_left[i]
        i += 1
        k += 1

    # add the remaining elements from right arrat to orignal array
    while j < n_r:
        arr[k] = arr_right[j]
        j += 1
        k += 1
    

def merge_sort(arr, p ,r):
    if p < r:
        q = (p + r)//2
        merge_sort(arr, p , q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array is", arr)
