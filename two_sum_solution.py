# Two Sum Problem Solution

def two_sum(nums, target):
    """Find two indices of numbers that add up to a specific target.

    Args:
        nums (List[int]): List of integers.
        target (int): The target sum.

    Returns:
        List[int]: Indices of the two numbers that add up to target.
    """
    # Initialize a hashmap to store the indices of the numbers
    index_map = {}

    # Loop through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        # Check if the complement exists in the hashmap
        if complement in index_map:
            # If it does, return the indices
            return [index_map[complement], i]
        # Store the current number's index in the hashmap
        index_map[num] = i
    # If no solution is found, return an empty list
    return []

# Example test cases
if __name__ == '__main__':
    # Test case 1: should return [0, 1]
    print(two_sum([2, 7, 11, 15], 9))
    # Test case 2: should return [1, 2]
    print(two_sum([3, 2, 4], 6))
    # Test case 3: should return [0, 1]
    print(two_sum([3, 3], 6))