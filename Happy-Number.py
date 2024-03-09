
def isHappy(n):
    # Set to store seen numbers to detect cycles
    is_seen = set()
    
    # Loop until we encounter 1 (happy number) or a cycle
    while n != 1:
        # If we encounter a number we've seen before, it's not happy
        if n in is_seen:
            return False
        
        # Add current number to the set
        is_seen.add(n)
        
        # Calculate the sum of squares of digits
        n_str = str(n)
        n = sum(int(digit)**2 for digit in n_str)
    
    # If we reach here, it means we encountered 1, so the number is happy
    return True

# Example usage:

# Example 1: n = 19
# This number eventually leads to 1, so it's a happy number
print(isHappy(19))  # Output: True

# Example 2: n = 2
# This number enters a cycle: 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
# Since it's in a cycle and never reaches 1, it's not a happy number. 
#The set looks like this if continued: seen = {2, 4, 16, 37, 58, 89, 145, 42, 20, 4, 16, 37, 58, 89, 145, 42, 20, 4}
print(isHappy(2))   # Output: False

# Example 3: n = 7
# This number eventually leads to 1, so it's a happy number
print(isHappy(7))   # Output: True
