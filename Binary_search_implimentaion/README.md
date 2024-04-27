# . Binary Search

* Binary search is an efficient search algorithm used to find a specific element in a sorted array.
* Binary search continuously divides the array using the middle element until the element is found.
* The time complexity of binary search is O(log n), and the space complexity is O(1).

# How to Implement the Binary Search Algorithm

* Example: Find the target element in an array using binary search.

* To implement binary search, follow these steps:

        arr = [2, 4, 6, 8, 10, 12, 14, 16]

        def binary_search(arr, target):
            #intialize the pointers
            left = 0
            right = len(arr) - 1
            #loop till elemtns found
            while left <= right:
                #split the array
                mid = (left + right) // 2
                
                #return mid if target and mid is same
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return -1

def binary_search(arr,target):



# 1. Define the Function:
* Create a function named binary_search(array, target) that takes an array and a target element as arguments

# 2. Initialize Pointers:
Initialize two pointers, left and right, representing the left and right indices of the array, respectively.

# 3. Search Process:
* While the left pointer is less than or equal to the right pointer, perform the following steps:

        * 1. Calculate the middle index as (left + right) // 2.

        * 2. If the middle element is equal to the target, return the middle index.

        * 3. If the middle element is less than the target, update the left pointer to mid + 1.

        * 4. If the middle element is greater than the target, update the right pointer to mid - 1.

* 4. If target vaue does not found returne -1


# Time Complexity:

*  The time complexity of binary search is O(log n), where n is the number of elements in the array.   This is because with each iteration, the search space is halved.

# Space Complexity:
    The space complexity of binary search is O(1)