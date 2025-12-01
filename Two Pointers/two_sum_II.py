# Brute Force Solution

def BrutetwoSum(numbers, target):
    length = len(numbers)
    
    for i in range(length):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

# Example usage:
print(BrutetwoSum([2,7,11,15], 9))  # [1,2]
print(BrutetwoSum([2,3,4], 6)) # [1,3]

# Time complexity: O(n^2)
# Space complexity: O(1)

# Optimal Two-Pointer Solution

def OptimaltwoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # +1 because the problem uses 1-based indexing
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1   # increase sum by moving left pointer right

        else:
            right -= 1  # decrease sum by moving right pointer left

# Example usage:
print(OptimaltwoSum([2,7,11,15], 9))  # [1,2]
print(OptimaltwoSum([2,3,4], 6)) # [1,3]

# Time complexity: O(n)
# Space complexity: O(1)