"""
Optimized solution for the Two Sum problem.

This function returns the indices of the two numbers from the given array that add up to the target.

The function uses a hashmap to achieve O(n) time complexity.

Example:
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)  # result will be [0, 1]

Parameters:
    nums (List[int]): List of integers.
    target (int): Target integer.

Returns:
    List[int]: Indices of the two numbers.
"""

def two_sum(nums, target):
    # Initialize a hashmap to store the indices of the numbers
    hashmap = {}

    # Iterate over the list of numbers
    for index, number in enumerate(nums):
        complement = target - number  # Calculate the complement
        if complement in hashmap:
            return [hashmap[complement], index]  # Return indices if found
        hashmap[number] = index  # Store the index of the number

    return []  # Return an empty list if no solution is found

# Example test cases
if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))  # Should return [0, 1]
    print(two_sum([3, 2, 4], 6))      # Should return [1, 2]
    print(two_sum([3, 3], 6))         # Should return [0, 1]