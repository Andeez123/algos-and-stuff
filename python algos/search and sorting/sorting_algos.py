# selection sort
def selection_sort(arr: list) -> list:
    """
    Finds the smallest elem in the list, and swap to its correct position for that iteration
    Time complexity: O(n^2)
    Not a stable algorithm
    """
    n = len(arr)
    for i in range(n - 1):

        #assume the current position has the min elem
        min_idx = i

        # find actual min from the list
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        #move min elem to its correct position by swapping
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr: list) -> list:
    """
    Repeatedly swapping the adjacent elements if they are in the wrong order
    Every pass the largest elem remaining goes to the end
    Time complexity: O(n^2) (terrible for large datasets)
    """
    n = len(arr)

    #traverse through all elems
    for i in range(n):
        swapped = False

        #last i elems are in place, skip them
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    return arr

def insertion_sort(arr: list) -> list:
    """
    Insertion sort, assumes the first element is sorted, start from the second element, if the sorted element > second element, swap positions
    and increase the sorted part of the array
    Worst case: O(n^2), if the list is in reverse order
    """
    n = len(arr)

    for i in range(1, n):
        current_elem = arr[i]
        
        for j in range(i-1, -1, -1):
            if arr[j] > current_elem:
                arr[j+1], arr[j] = arr[j], current_elem
    return arr

def merge_arrays(arr: list, start: int, mid: int, end: int, tmp: list) -> None:
    p_a = start
    p_b = mid + 1

    for i in range(start, end+1):
        if p_a > mid: # first half finished, continue on with second half
            tmp[i] = arr[p_b]
            p_b += 1
        elif p_b > end: # second half finished, continue with first half
            tmp[i] = arr[p_a]
            p_a += 1
        elif arr[p_a] <= arr[p_b]: # copy arr[p_a]
            # print(tmp[i])
            # print(arr[i])
            tmp[i] = arr[p_a]
            p_a += 1
        else:
            tmp[i] = arr[p_b] # copy arr[p_b]
            p_b += 1    

def merge_sort_aux(arr: list, start: int, end: int, tmp: list) -> None:
    # pointers dont meet, 2 or more items left to sort
    if not start == end:
        mid = (start + end) // 2

        # split into two halves
        merge_sort_aux(arr, start, mid, tmp)
        merge_sort_aux(arr, mid+1, end, tmp)

        # merge
        merge_arrays(arr, start, mid, end, tmp)

        for i in range(start, end+1):
            arr[i] = tmp[i]


def merge_sort(arr: list) -> list:
    """
    Time complexity: O(nlogn) * CompEq
    """
    tmp = [0] * len(arr)

    start = 0
    end = len(arr) - 1

    merge_sort_aux(arr, start, end, tmp)
    return arr

def swap(arr: list, high: int, low: int) -> int:
    """
    Method to swap elements
    """
    arr[high], arr[low] = arr[low], arr[high]

def partition(arr: list, high: int, low: int):
    """
    Quick sort partition function
    """
    mid = (high+low) // 2 
    pivot = arr[mid] # selecting pivot as median element
    swap(arr, high, mid) # swap the median element to the front end of array

    boundary = high # set boundary at front of array

    for k in range(high + 1, low + 1): # loop for all elements except from the first, which is where the pivot is
        if arr[k] < pivot: # if element is less than pivot
            boundary += 1 # increase boundary range
            swap(arr, k, boundary) # swap element k to boundary 
    swap(arr, high, boundary) # swap the median value back to the boundary point, which is the final position of the median
    return boundary
    

def quick_sort_aux(arr: list, high: int, low: int) -> None:
    """
    Recursive quick sort function
    """
    if (high < low): # if start and end are not the same points
        boundary = partition(arr, high, low) # setup initial boundary
        quick_sort_aux(arr, high, boundary - 1) 
        quick_sort_aux(arr, boundary + 1, low)

def quick_sort(arr:list) -> list:
    """
    Quick sort entry point
    Best case: always pick median as pivot: O(nlogn) * CompEq
    Worst case: always pick min/max as pivot: O(n^2) * CompEq
    """
    start = 0
    end = len(arr) - 1
    quick_sort_aux(arr, start, end)
    return arr

if __name__ == "__main__":
    unsorted_arr = [2,3,1,4]
    print(quick_sort(unsorted_arr))
