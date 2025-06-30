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



if __name__ == "__main__":
    unsorted_arr = [7,8,2,1,3,4,6,5]
    print(insertion_sort(unsorted_arr))
