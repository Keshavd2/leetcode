def min_length(s):
    stack = []
    for letter in s:
        if stack and letter == 'B':
            stack.pop()
            continue
        stack.append(letter)
    return len(stack)


print(min_length("BABB"))   # Expected: 0
print(min_length("AABBB"))  # Expected: 1
print(min_length("AAAA"))   # Expected: 4
print(min_length("AB"))     # Expected: 0
print(min_length("BA"))     # Expected: 2