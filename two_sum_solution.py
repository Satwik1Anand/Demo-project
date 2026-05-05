# two_sum_solution.py

"""
Optimized solution for the Two Sum problem.

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

Time Complexity: O(n) - One pass hashmap solution.
Space Complexity: O(n) - Storing elements in the hashmap.
"""

def two_sum(nums, target):
    """
    Function to find the indices of the two numbers that add up to target.
    :param nums: List of integers.
    :param target: Integer target value.
    :return: List of indices of the two numbers.
    """
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []  # Return empty if no solution


# Example test cases
if __name__ == '__main__':
    # Test case 1
    print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
    # Test case 2
    print(two_sum([3, 2, 4], 6))  # Output: [1, 2]
    # Test case 3
    print(two_sum([3, 3], 6))  # Output: [0, 1]
