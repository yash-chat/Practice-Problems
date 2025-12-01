
# Brute Force Solution

def isBrutePalindrome(s):
    filtered = ""

    # Step 1: build filtered (manual alphanumeric + lowercase)
    for ch in s:
        # manual alphanumeric check
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
            # manual lowercase
            if 'A' <= ch <= 'Z':
                filtered += chr(ord(ch) + 32)
            else:
                filtered += ch

    # Step 2: manual palindrome check
    left, right = 0, len(filtered) - 1
    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1

    return True

# Example usage:
print(isBrutePalindrome("A man, a plan, a canal: Panama"))  # True
print(isBrutePalindrome("race a car"))                      # False

# Time complexity: O(n)
# Space complexity: O(n)

# Optimal Two-Pointer Solution

def isOptimalPalindrome(s: str) -> bool:
    
    def is_alpha_num(ch):
        # manual alphanumeric check
        return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')

    def to_lower(ch):
        # convert uppercase to lowercase manually
        if 'A' <= ch <= 'Z':
            return chr(ord(ch) + 32)
        return ch

    left, right = 0, len(s) - 1

    while left < right:

        # move left until alphanumeric
        while left < right and not is_alpha_num(s[left]):
            left += 1

        # move right until alphanumeric
        while left < right and not is_alpha_num(s[right]):
            right -= 1

        # compare after converting to lowercase manually
        if to_lower(s[left]) != to_lower(s[right]):
            return False

        left += 1
        right -= 1

    return True

# Example usage:
print(isOptimalPalindrome("A man, a plan, a canal: Panama"))  # True
print(isOptimalPalindrome("race a car"))                      # False

# Time complexity: O(n)
# Space complexity: O(1)