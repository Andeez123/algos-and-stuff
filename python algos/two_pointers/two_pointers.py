# Given an array sorted in ascending order, and a target, find if there exists any pair of elements such that their sum is equal to the target

# Naive method: O(n^2) time and O(1) space
def two_sum_naive(arr: list, target: int) -> bool:
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                print(f"{arr[i]} + {arr[j]}")
                return True
    
    return False

# Better approaches: Binary search and hashing

# Better approach: Using two-pointer technique, O(n) time and O(1) space
# works only when the array is sorted in ascending order
def two_pointers(arr: list, target: int) -> bool:
    """
    Time complexity: O(n) as the loops run at most n times, either increase left, decrease right or stop the loop
    Auxiliary space: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            print(f"{arr[left]} + {arr[right]}")
            return True
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1
    
    return False

if __name__ == "__main__":
    arr = [10, 20, 30]
    target = 70

    print(two_pointers(arr, target))