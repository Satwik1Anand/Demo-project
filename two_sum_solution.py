# Two Sum Problem Solution

def two_sum(nums, target):
    """
    Given an array of integers `nums` and an integer `target`, 
    return indices of the two numbers such that they add up to `target`.

    Args:
        nums (List[int]): List of integers.
        target (int): The target integer to sum up to.

    Returns:
        List[int]: Indices of the two numbers adding up to target.

    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
        >>> two_sum([3, 3], 6)
        [0, 1]
    """
    num_map = {}  # Store index of each number
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], index]
        num_map[num] = index
    return []  # Return empty list if no solution found

# Example Test Cases
if __name__ == '__main__':
    assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Test case 1 failed"
    assert two_sum([3, 2, 4], 6) == [1, 2], "Test case 2 failed"
    assert two_sum([3, 3], 6) == [0, 1], "Test case 3 failed"
    print("All test cases pass")