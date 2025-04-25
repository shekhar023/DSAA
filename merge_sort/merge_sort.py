

# Merge Sort Algorithm
def merge(arr, p, q, r):
    n_l = q - p + 1 # size of left subarray
    n_r = r - q # size of right subarray

    # create temp arrays
    # left[] and right[] are the temporary arrays
    # left[] is the left subarray
    # right[] is the right subarray
    left = [0] * n_l
    right = [0] * n_r

    # copy data to temp arrays left[] and right[]
    for i in range(0, n_l):
        left[i] = arr[p + i]

    # copy data to temp arrays left[] and right[]
    for j in range(0, n_r):
        right[j] = arr[q + 1 + j]

    
    i = 0 # index for the smallest element in left[]
    j = 0 # index for the smallest element in right[]
    k = p # index for the merged subarray A[p:r]

    # merge the temp arrays back into arr[p..r]
    while i < n_l and j < n_r:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    
    # copy the remaining elements of left[], if there are any 
    # if there are any elements left in the left subarray
    # copy them to the merged array      
    while i < n_l:
        arr[k] = left[i] # copy the remaining elements of left[]
        i += 1 # increment the index of left[]
        k += 1 # increment the index of merged array

    
    # copy the remaining elements of right[], if there are any
    while j < n_r:
        arr[k] = right[j]
        j += 1
        k += 1


# Python program to implement merge sort
# This function divides the array into two halves, sorts them and merges them
# The merge function is responsible for merging two sorted subarrays into a single sorted array
# The merge_sort function is the main function that divides the array and calls the merge function
# Time complexity: O(n log n)
# Space complexity: O(n)
# Merge sort is a divide-and-conquer algorithm that sorts an array by recursively dividing it into two halves,
# sorting each half, and then merging the sorted halves back together.
# It is efficient for large datasets and has a guaranteed time complexity of O(n log n).
# Merge sort is a stable sort, meaning that it preserves the relative order of equal elements.
# It is also a non-adaptive sort, meaning that it does not take advantage of existing order in the input.
# Merge sort is not an in-place sort, as it requires additional space for the temporary arrays used during the merge process.
# Merge sort is a stable sort, meaning that it preserves the relative order of equal elements.
def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)



if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array is", arr)
# This code implements the merge sort algorithm, which is a divide-and-conquer algorithm for sorting an array.
# It recursively divides the array into two halves, sorts each half, and then merges the sorted halves back together.
# The merge function is responsible for merging two sorted subarrays into a single sorted array.
# The merge_sort function is the main function that divides the array and calls the merge function. 