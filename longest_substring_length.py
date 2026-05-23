def length_of_longest_substring(s):
    i, j = 0, 0
    max_length = 0
    substring = set()

    while(j < len(s)):
        if s[j] in substring:
            substring.remove(s[i])
            i += 1
        else:
            substring.add(s[j])
            j += 1
        
        if max_length < (j - i):
            max_length = j - i

    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # Expected: 3
print(length_of_longest_substring("bbbbb"))     # Expected: 1
print(length_of_longest_substring("pwwkew"))    # Expected: 3
print(length_of_longest_substring(""))          # Expected: 0