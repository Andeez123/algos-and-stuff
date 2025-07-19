def linear_search(arr: list, item: int) -> int:
    """
    Used for unsorted arrays
    Complexity: O(n)
    """
    n = len(arr)

    for i in range(n):
        if arr[i] == item:
            return i
    return None

def iterative_binary_search(arr: list, item: int) -> int:
    """
    Find middle element, if mid elem == item, return index
    If mid elem > item: shorten right search space, right = mid - 1
    If mid elem < itm: move left search space up, left = mid + 1
    Time complexity: O(logn), the search space is havled every iteration
    """
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == item:
            return mid
        
        elif arr[mid] > item:
            right = mid - 1

        elif arr[mid] < item:
            left = mid + 1
    return None


 

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(iterative_binary_search(arr, 10))
