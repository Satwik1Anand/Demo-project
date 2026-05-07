def two_sum(nums, target):
    """
    Function to find two indices of the numbers in the list `nums`
    that add up to the `target` value.
    
    Args:
    nums (List[int]): List of integers.
    target (int): Target integer to achieve by summing two numbers.
    
    Returns:
    List[int]: List containing the indices of the two numbers.
    
    Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3, 3], 6)
    [0, 1]
    """
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []  # return empty list if no solution found

# Example Test Cases
if __name__ == "__main__":
    # Test cases to validate the solution
    print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(two_sum([3, 2, 4], 6))       # Output: [1, 2]
    print(two_sum([3, 3], 6))          # Output: [0, 1]