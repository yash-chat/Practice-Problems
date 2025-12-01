# Brute Force Solution

def BrutethreeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    target = 0
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = sorted([nums[i], nums[j], nums[k]]) # Make all triplets consistent so duplicates can be detected
                    if triplet not in result: # Prevent storing the same triplet multiple times
                        result.append(triplet)
    return result

# Example usage:
print(BrutethreeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(BrutethreeSum([0,1,1])) # []

# Time complexity: O(n^3)
# Space complexity: O(1)

# Optimal Two-Pointer Solution

def OptimalthreeSum(nums):
    ans = []
    nums.sort()  # Sort the array to enable two-pointer technique and easy duplicate skipping
    
    for i in range(len(nums)):
        # Skip duplicates for the first element of the triplet to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        j = i + 1  # Left pointer starts right after i
        k = len(nums) - 1  # Right pointer starts at the end
        
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                # Found a valid triplet, add it to the answer
                ans.append([nums[i], nums[j], nums[k]])
                j += 1  # Move left pointer right
                k -= 1  # Move right pointer left
                # Skip duplicates for j: move j until it's different from the previous value
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                # Skip duplicates for k: move k until it's different from the next value (since we decremented)
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif total < 0:
                # Sum is too small, increase the sum by moving left pointer right
                j += 1
            else:
                # Sum is too large, decrease the sum by moving right pointer left
                k -= 1
    
    return ans

# Example usage:
print(OptimalthreeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(OptimalthreeSum([0,1,1])) # []

# Time complexity: O(n log n) + O(n) * O(n) = O(n²)
# Space complexity: O(1)