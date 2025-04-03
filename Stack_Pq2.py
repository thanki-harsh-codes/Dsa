# 1. Parentheses Positioning Error

def first_mismatch(s):
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return i  # First mismatched closing parenthesis
    return stack[0] if stack else -1  # First unmatched opening parenthesis

# Example Usage
print(first_mismatch("((())"))   # Output: 0 (Unmatched '(' at position 0)
print(first_mismatch("(()))"))   # Output: 4 (Unmatched ')' at position 4)
print(first_mismatch("(())"))    # Output: -1 (Balanced)


# 2. Parentheses in a Long String

def balanced_positions(s):
    stack, valid = [], set()
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                open_idx = stack.pop()
                valid.add(open_idx)
                valid.add(i)

    return sorted(valid)  # Return sorted valid positions

# Example Usage
print(balanced_positions("a(b)c)d(e(f)g)"))  # Output: [2, 4, 8, 10, 11, 13]


# 3. Minimum Number of Parentheses to Add

def min_add_to_make_valid(s):
    stack, count = [], 0

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                count += 1  # Unmatched ')'

    return count + len(stack)  # Unmatched '(' + unmatched ')'

# Example Usage
print(min_add_to_make_valid("()))(("))  # Output: 4


# 4. Longest Valid Parentheses Substring

def longest_valid_parentheses(s):
    stack, max_len = [-1], 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)

    return max_len

# Example Usage
print(longest_valid_parentheses(")()())"))  # Output: 4
