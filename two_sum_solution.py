def two_sum(nums, target):
    """
    Given an array of integers 'nums' and an integer 'target', return the indices of the two numbers such that they add up to 'target'.

    Parameters:
    nums (List[int]): The list of integers.
    target (int): The target sum we are looking for.

    Returns:
    List[int]: The indices of the two numbers adding up to target.
    """
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []  # In case there is no solution


# Example test cases
test_cases = [
    ([2, 7, 11, 15], 9),  # Expected output: [0, 1]
    ([3, 2, 4], 6),      # Expected output: [1, 2]
    ([3, 3], 6)          # Expected output: [0, 1]
]

for nums, target in test_cases:
    result = two_sum(nums, target)
    print(f'Two Sum for nums={nums} and target={target}: Indices={result}')