def two_sum(nums, target):
    """
    Returns the indices of the two numbers that add up to the target.
    Utilizes a hashmap to achieve an optimized solution with O(n) time complexity.

    Parameters:
    nums (list): List of integers.
    target (int): The target sum.

    Returns:
    list: Indices of the two numbers that add up to target.

    Example:
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]  # Because nums[0] + nums[1] == 9
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # Return empty list if no solution found