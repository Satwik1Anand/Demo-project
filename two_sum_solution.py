# Two Sum Solution

def two_sum(nums, target):
    """
    Given an array of integers and a target integer,
    return the indices of the two numbers such that they add up to the target.

    Parameters:
    nums (list): List of integers
    target (int): Target integer to find in nums

    Returns:
    list: A list containing the indices of the two numbers
    """
    # Create a hashmap to store the indices of the numbers
    hashmap = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], index]
        hashmap[num] = index
    raise ValueError("No two sum solution")

# Example test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test case 1 result: {two_sum(nums1, target1)}") # Expected output: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test case 2 result: {two_sum(nums2, target2)}") # Expected output: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test case 3 result: {two_sum(nums3, target3)}") # Expected output: [0, 1]