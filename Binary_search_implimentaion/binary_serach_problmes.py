"""
Count Pairs Whose Sum is Less than Target

Given a 0-indexed integer array nums of length n and an integer target,
return the number of pairs (i, j) where 0 <= i < j < n and nums:[i] + nums[j] < target.
 
"""

class CountPairs:
    def count(self, arr, target):
        arr.sort()
        count = 0  # corrected variable name from counter to count
        # Length of arr
        n = len(arr)
        # Initialize the pointers
        left = 0
        right = n - 1

        while left < right:
            if arr[left] + arr[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

obj = CountPairs()
arr = [-1, 1, 2, 3, 1]
target = 2
res = obj.count(arr, target)
# print(res)


def smaller_numbers_than_current(nums):
    # Count the frequency of each number
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Calculate the cumulative count of numbers smaller than current number
    print(frequency)
    cumulative_count = {}
    smaller_count = 0
    for num in sorted(frequency.keys()):
        cumulative_count[num] = smaller_count
        smaller_count += frequency[num]

    # Generate the result list using the cumulative count
    result = [cumulative_count[num] for num in nums]
    return result

# Example usage:
nums = [8, 1, 2, 2, 3]
# print(smaller_numbers_than_current(nums))  # Output: [4, 0, 1, 1, 3]


def sum_array():
    result = []
    nums = [1,2,3,4]
    sum = 0
    for i in nums:
        sum+=i
        result.append(sum)
    print(result)
    return result


sum_array()
